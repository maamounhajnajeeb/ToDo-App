from django.utils.timezone import make_aware

from rest_framework import serializers

from datetime import datetime

from . import models


class ToDoSerializer(serializers.ModelSerializer):
    due_date = serializers.StringRelatedField()
    
    class Meta:
        model = models.ToDo
        fields = ('id', 'title', 'checked', 'piriority', 'time', 'on_time', 'checked_at', 'due_date', )
    
    def validate(self, attrs):
        if attrs.get("checked") == True:
            attrs.setdefault("checked_at", make_aware(datetime.now()))
            
        return super().validate(attrs)
    
    def create(self, validated_data):
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)


class DateSerializer(serializers.ModelSerializer):
    tasks = ToDoSerializer(many=True)
    
    class Meta:
        model = models.TaskDates
        fields = ("id", "date", "user", "tasks", )
    
    def validate(self, attrs):
        return super().validate(attrs)
    
    def create(self, validated_data):
        user, date = validated_data.pop("user"), validated_data.pop("date")
        tasks = validated_data.get("tasks")
        if not tasks:
            raise serializers.ValidationError({"Error": "tasks attr must not be empty []"})
        
        task_date, created = models.TaskDates.objects.get_or_create(user=user, date=date)
        
        if len(tasks) > 1:
            self._create_tasks(tasks, task_date)
        else:
            self._create_task(tasks, task_date)
        
        return task_date
    
    def _create_tasks(self, tasks_validated_data, task_date):
        todos = []
        for task in tasks_validated_data:
            todos.append(models.ToDo(due_date=task_date, **task))
        result = models.ToDo.objects.bulk_create(todos)
    
    def _create_task(self, task_validated_data, task_date):
        result = models.ToDo.objects.create(**task_validated_data[0], due_date=task_date)
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
    
    def to_representation(self, instance: models.TaskDates):
        tasks = instance.related_tasks.all()
        serialized_tasks = ToDoSerializer(tasks, many=True)
        
        return {
            "id": instance.id, "user": instance.user.full_name
            , "date": instance.date, "tasks": serialized_tasks.data
        }
