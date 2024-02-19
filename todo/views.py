from rest_framework import permissions, decorators
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.request import Request

from datetime import date

from . import serializers, models
from .helpers import catch, delete_objs, construct_message

from utils.permissions import owner_only



class CreateTask(generics.CreateAPIView):
    queryset = models.TaskDates.objects
    serializer_class = serializers.DateSerializer
    
    def get_serializer(self, *args, **kwargs):
        """
        Return the serializer instance that should be used for validating and
        deserializing input, and for serializing output.
        """
        serializer_class = self.get_serializer_class()
        kwargs.setdefault('context', self.get_serializer_context())
        kwargs.get("data").setdefault('user', self.request.user.id)
        return serializer_class(*args, **kwargs)
    
    def create(self, request: Request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class RUDTask(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.ToDoSerializer
    queryset = models.ToDo.objects
    permission_classes = (permissions.IsAuthenticated, owner_only.IsOwner, )
    
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


@decorators.api_view(["DELETE", ])
@decorators.permission_classes([permissions.IsAuthenticated, owner_only.IsOwner, ])
def bulk_delete(req: Request):
    todo_ids = req.query_params.get("ids")
    if not todo_ids:
        return Response({"Error": "attr 'ids' must be provided in the query_params"},
                status=status.HTTP_400_BAD_REQUEST)
    
    todo_ids = catch(todo_ids)
    counter, not_found = delete_objs(todo_ids, req.user)
    message = construct_message(todo_ids, not_found, counter)
    
    return Response({"message": message}, status=status.HTTP_200_OK)


class ListAllUserTasks(generics.ListAPIView):
    queryset = models.TaskDates.objects
    serializer_class = serializers.DateSerializer
    
    def get_queryset(self):
        queryset = self.queryset.filter(user=self.request.user.id).prefetch_related("related_tasks")
        return queryset


class SpecificDateUserTasks(generics.ListAPIView):
    queryset = models.TaskDates.objects
    serializer_class = serializers.DateSerializer
    
    def get_queryset(self):
        year, month, day = self.kwargs.get("year"), self.kwargs.get("month"), self.kwargs.get("day")
        queryset = self.queryset.filter(
            user=self.request.user.id, date=date(year, month, day)).prefetch_related("related_tasks")
        return queryset
