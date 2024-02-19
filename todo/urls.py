from django.urls import path

from . import views

app_name = "todo"

urlpatterns = [
    # create task
    path("", views.CreateTask.as_view(), name="create_task_api"),
    
    # RUD task
    path("<int:pk>/", views.RUDTask.as_view(), name="rud_task_api"),
    
    # bulk delete
    path("bulk_delete/", views.bulk_delete, name="bulk_delete_api"),
    
    # list all user's tasks
    path("user_tasks/", views.ListAllUserTasks.as_view(), name="list_user_tasks"),
    
    # list all user's tasks in specific date
    path("user_tasks/<int:year>/<int:month>/<int:day>/"
        , views.SpecificDateUserTasks.as_view(), name="specific_date_user_tasks"),
]
