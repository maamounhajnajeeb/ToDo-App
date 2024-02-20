from django.contrib.auth import get_user_model

from rest_framework.test import APITestCase
from rest_framework import status

from . import models, serializers

Users = get_user_model()
app_url = "/api/v1/todo/"
login_url = "/api/v1/users/sign_in/"



# class CreateTwoTasksTestCase(APITestCase):
#     def setUp(self) -> None:
#         self.user = Users.objects.create_user(
#             email="maamoun.haj.najeeb@gmail.com", password="17AiGz48rhe", full_name="Maamoun Haj Najeeb")
    
#     def create_access_token(self):
#         response = self.client.post(
#             path=login_url, data=dict(email="maamoun.haj.najeeb@gmail.com", password="17AiGz48rhe"))
        
#         return response.json().get("access")
    
#     def test_create_task(self):
#         data = {
#             "date": "2024-2-21",
#             "tasks": [
#                 {
#                     "time": 30,
#                     "piriority": "High",
#                     "title": "a new task"
#                 },
#                 {
#                     "time": 90,
#                     "piriority": "Med",
#                     "title": "an important task"
#                 }
#             ]
#         }
        
#         response = self.client.post(
#             path=app_url, data=data, format="json"
#             , headers=dict(Authorization=f"Bearer {self.create_access_token()}"))
        
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(len(response.json().get("tasks")), 2)
#         self.assertEqual(len(response.json().get("tasks")[0]), 8)


# class CreateTaskTestCase(APITestCase):
#     def setUp(self) -> None:
#         self.user = Users.objects.create_user(
#             email="maamoun.haj.najeeb@gmail.com", password="17AiGz48rhe", full_name="Maamoun Haj Najeeb")
    
#     def create_access_token(self):
#         response = self.client.post(
#             path=login_url, data=dict(email="maamoun.haj.najeeb@gmail.com", password="17AiGz48rhe"))
        
#         return response.json().get("access")
    
#     def test_create_task(self):
#         data = {
#             "date": "2024-2-21",
#             "tasks": [
#                 {
#                     "time": 30,
#                     "piriority": "High",
#                     "title": "a new task"
#                 }
#             ]
#         }
        
#         response = self.client.post(
#             path=app_url, data=data, format="json"
#             , headers=dict(Authorization=f"Bearer {self.create_access_token()}"))
        
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(len(response.json().get("tasks")), 1)
#         self.assertEqual(len(response.json().get("tasks")[0]), 8)


# class CreateTaskAuthenticationErrorTestCase(APITestCase):
#     def test_create_task(self):
#         data = {
#             "date": "2024-2-21",
#             "tasks": [
#                 {
#                     "time": 30,
#                     "piriority": "High",
#                     "title": "a new task"
#                 }
#             ]
#         }
        
#         response = self.client.post(path=app_url, data=data, format="json")
        
#         self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


# class CreateTaskWithoutTasksAttrTestCase(APITestCase):
#     def setUp(self) -> None:
#         self.user = Users.objects.create_user(
#             email="maamoun.haj.najeeb@gmail.com", password="17AiGz48rhe", full_name="Maamoun Haj Najeeb")
    
#     def create_access_token(self):
#         response = self.client.post(
#             path=login_url, data=dict(email="maamoun.haj.najeeb@gmail.com", password="17AiGz48rhe"))
        
#         return response.json().get("access")
    
#     def test_create_task(self):
#         data = {
#             "date": "2024-2-21",
#             }
        
#         response = self.client.post(
#             path=app_url, data=data, format="json"
#             , headers=dict(Authorization=f"Bearer {self.create_access_token()}"))
        
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#         self.assertEqual(response.json().get("tasks")[0], "This field is required.")


# class CreateTaskWithEmptyTasksAttrTestCase(APITestCase):
#     def setUp(self) -> None:
#         self.user = Users.objects.create_user(
#             email="maamoun.haj.najeeb@gmail.com", password="17AiGz48rhe", full_name="Maamoun Haj Najeeb")
    
#     def create_access_token(self):
#         response = self.client.post(
#             path=login_url, data=dict(email="maamoun.haj.najeeb@gmail.com", password="17AiGz48rhe"))
        
#         return response.json().get("access")
    
#     def test_create_task(self):
#         data = {
#             "date": "2024-2-21",
#             "tasks": []
#             }
        
#         response = self.client.post(
#             path=app_url, data=data, format="json"
#             , headers=dict(Authorization=f"Bearer {self.create_access_token()}"))
        
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#         self.assertEqual(response.json().get("Error"), "tasks attr must not be empty []")


# class CreateTaskWithoutDateAttrTestCase(APITestCase):
#     def setUp(self) -> None:
#         self.user = Users.objects.create_user(
#             email="maamoun.haj.najeeb@gmail.com", password="17AiGz48rhe", full_name="Maamoun Haj Najeeb")
    
#     def create_access_token(self):
#         response = self.client.post(
#             path=login_url, data=dict(email="maamoun.haj.najeeb@gmail.com", password="17AiGz48rhe"))
        
#         return response.json().get("access")
    
#     def test_create_task(self):
#         data = {
#             "tasks": []
#             }
        
#         response = self.client.post(
#             path=app_url, data=data, format="json"
#             , headers=dict(Authorization=f"Bearer {self.create_access_token()}"))
        
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#         self.assertEqual(response.json().get("date")[0], "This field is required.")


# class GetTaskTestCase(APITestCase):
#     def setUp(self) -> None:
#         self.user = Users.objects.create_user(
#             email="maamoun.haj.najeeb@gmail.com", password="17AiGz48rhe", full_name="Maamoun Haj Najeeb")
        
#         tasks_data = {
#             "date": "2024-2-21",
#             "tasks": [
#                 {
#                     "time": 30,
#                     "piriority": "High",
#                     "title": "a new task"
#                 }
#             ]
#         }
        
#         tasks = self.client.post(path=app_url, data=tasks_data, format="json"
#             , headers=dict(Authorization=f"Bearer {self.create_access_token()}"))
    
#     def create_access_token(self):
#         response = self.client.post(
#             path=login_url, data=dict(email="maamoun.haj.najeeb@gmail.com", password="17AiGz48rhe"))
        
#         return response.json().get("access")
    
#     def test_get_first_task(self):
#         task_id = models.ToDo.objects.last().id
#         url = f"{app_url}{task_id}/"
#         response = self.client.get(path=url, headers=dict(Authorization=f"Bearer {self.create_access_token()}"))
#         task = models.ToDo.objects.get(id=task_id)
#         serialized_task = serializers.ToDoSerializer(task)
        
#         self.assertEqual(serialized_task.data, response.json())
#         self.assertEqual(response.status_code, status.HTTP_200_OK)


# class GetTaskDoubleCreationTestCase(APITestCase):
#     def setUp(self) -> None:
#         self.user = Users.objects.create_user(
#             email="maamoun.haj.najeeb@gmail.com", password="17AiGz48rhe", full_name="Maamoun Haj Najeeb")
        
#         tasks_data = {
#             "date": "2024-2-21",
#             "tasks": [
#                 {
#                     "time": 30,
#                     "piriority": "High",
#                     "title": "a new task"
#                 },
#                 {
#                     "time": 90,
#                     "piriority": "Med",
#                     "title": "an important task"
#                 }
#             ]
#         }
        
#         tasks = self.client.post(path=app_url, data=tasks_data, format="json"
#             , headers=dict(Authorization=f"Bearer {self.create_access_token()}"))
    
#     def create_access_token(self):
#         response = self.client.post(
#             path=login_url, data=dict(email="maamoun.haj.najeeb@gmail.com", password="17AiGz48rhe"))
        
#         return response.json().get("access")
    
#     def test_get_second_task(self):
#         task_id = models.ToDo.objects.last().id
#         url = f"{app_url}{task_id}/"
#         response = self.client.get(path=url, headers=dict(Authorization=f"Bearer {self.create_access_token()}"))
        
#         task = models.ToDo.objects.get(id=task_id)
#         serialized_task = serializers.ToDoSerializer(task)
        
#         self.assertEqual(serialized_task.data, response.json())
#         self.assertEqual(response.status_code, status.HTTP_200_OK)


# class GetTaskNotFoundTestCase(APITestCase):
#     def setUp(self) -> None:
#         self.user = Users.objects.create_user(
#             email="maamoun.haj.najeeb@gmail.com", password="17AiGz48rhe", full_name="Maamoun Haj Najeeb")
    
#     def create_access_token(self):
#         response = self.client.post(
#             path=login_url, data=dict(email="maamoun.haj.najeeb@gmail.com", password="17AiGz48rhe"))
        
#         return response.json().get("access")
    
#     def test_get_second_task(self):
#         url = f"{app_url}1/"
#         response = self.client.get(path=url, headers=dict(Authorization=f"Bearer {self.create_access_token()}"))
        
#         self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


# class GetTaskNotAuthenticatedTestCase(APITestCase):
#     def setUp(self) -> None:
#         self.user = Users.objects.create_user(
#             email="maamoun.haj.najeeb@gmail.com", password="17AiGz48rhe", full_name="Maamoun Haj Najeeb")
        
#         tasks_data = {
#             "date": "2024-2-21",
#             "tasks": [
#                 {
#                     "time": 30,
#                     "piriority": "High",
#                     "title": "a new task"
#                 }
#             ]
#         }
        
#         tasks = self.client.post(path=app_url, data=tasks_data, format="json"
#             , headers=dict(Authorization=f"Bearer {self.create_access_token()}"))
    
#     def create_access_token(self):
#         response = self.client.post(
#             path=login_url, data=dict(email="maamoun.haj.najeeb@gmail.com", password="17AiGz48rhe"))
        
#         return response.json().get("access")
    
#     def test_get_second_task(self):
#         url = f"{app_url}1/"
#         response = self.client.get(path=url)
        
#         self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


# class DeleteTaskTestCase(APITestCase):
#     def setUp(self) -> None:
#         self.user = Users.objects.create_user(
#             email="maamoun.haj.najeeb@gmail.com", password="17AiGz48rhe", full_name="Maamoun Haj Najeeb")
        
#         tasks_data = {
#             "date": "2024-2-21",
#             "tasks": [
#                 {
#                     "time": 30,
#                     "piriority": "High",
#                     "title": "a new task"
#                 },
#                 {
#                     "time": 90,
#                     "piriority": "Med",
#                     "title": "an important task"
#                 }
#             ]
#         }
        
#         tasks = self.client.post(path=app_url, data=tasks_data, format="json"
#             , headers=dict(Authorization=f"Bearer {self.create_access_token()}"))
    
#     def create_access_token(self):
#         response = self.client.post(
#             path=login_url, data=dict(email="maamoun.haj.najeeb@gmail.com", password="17AiGz48rhe"))
        
#         return response.json().get("access")
    
#     def test_delete_second_task(self):
#         task_id = models.ToDo.objects.last().id
#         url = f"{app_url}{task_id}/"
#         response = self.client.delete(path=url, headers=dict(Authorization=f"Bearer {self.create_access_token()}"))
        
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
#     def test_delete_first_task(self):
#         task_id = models.ToDo.objects.first().id
#         url = f"{app_url}{task_id}/"
#         response = self.client.delete(path=url, headers=dict(Authorization=f"Bearer {self.create_access_token()}"))
        
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


# class DeleteTaskNotAuthorizedTestCase(APITestCase):
#     def setUp(self) -> None:
#         self.user = Users.objects.create_user(
#             email="maamoun.haj.najeeb@gmail.com", password="17AiGz48rhe", full_name="Maamoun Haj Najeeb")
        
#         tasks_data = {
#             "date": "2024-2-21",
#             "tasks": [
#                 {
#                     "time": 30,
#                     "piriority": "High",
#                     "title": "a new task"
#                 },
#                 {
#                     "time": 90,
#                     "piriority": "Med",
#                     "title": "an important task"
#                 }
#             ]
#         }
        
#         tasks = self.client.post(path=app_url, data=tasks_data, format="json"
#             , headers=dict(Authorization=f"Bearer {self.create_access_token()}"))
    
#     def create_access_token(self):
#         response = self.client.post(
#             path=login_url, data=dict(email="maamoun.haj.najeeb@gmail.com", password="17AiGz48rhe"))
        
#         return response.json().get("access")
    
#     def test_delete_task_not_authorized(self):
#         task_id = models.ToDo.objects.last().id
#         url = f"{app_url}{task_id}/"
#         response = self.client.delete(path=url)
        
#         self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


# class DeleteTaskNotFoundTestCase(APITestCase):
#     def setUp(self) -> None:
#         self.user = Users.objects.create_user(
#             email="maamoun.haj.najeeb@gmail.com", password="17AiGz48rhe", full_name="Maamoun Haj Najeeb")
        
#         tasks_data = {
#             "date": "2024-2-21",
#             "tasks": [
#                 {
#                     "time": 30,
#                     "piriority": "High",
#                     "title": "a new task"
#                 },
#                 {
#                     "time": 90,
#                     "piriority": "Med",
#                     "title": "an important task"
#                 }
#             ]
#         }
        
#         tasks = self.client.post(path=app_url, data=tasks_data, format="json"
#             , headers=dict(Authorization=f"Bearer {self.create_access_token()}"))
    
#     def create_access_token(self):
#         response = self.client.post(
#             path=login_url, data=dict(email="maamoun.haj.najeeb@gmail.com", password="17AiGz48rhe"))
        
#         return response.json().get("access")
    
#     def test_delete_second_task(self):
#         task_id = 1000000
#         url = f"{app_url}{task_id}/"
#         response = self.client.delete(path=url, headers=dict(Authorization=f"Bearer {self.create_access_token()}"))
        
#         self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


# class BulkDeleteAttrNameErrorTestCase(APITestCase):
#     def setUp(self) -> None:
#         self.user = Users.objects.create_user(
#             email="maamoun.haj.najeeb@gmail.com", password="17AiGz48rhe", full_name="Maamoun Haj Najeeb")
    
#     def create_access_token(self):
#         response = self.client.post(
#             path=login_url, data=dict(email="maamoun.haj.najeeb@gmail.com", password="17AiGz48rhe"))
        
#         return response.json().get("access")
    
#     def test_ids_attr_error(self):
#         url = f"{app_url}bulk_delete/"
#         response = self.client.delete(
#             path=url, headers=dict(Authorization=f"Bearer {self.create_access_token()}")
#             , data={"todo_ids":[1,2]})
        
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#         self.assertEqual(response.json().get("Error")
#             , "attr 'ids' must be provided in the request data and it must not be empty")


# class BulkDeleteSuccessfullDeletionTestCase(APITestCase):
#     def setUp(self) -> None:
#         self.user = Users.objects.create_user(
#             email="maamoun.haj.najeeb@gmail.com", password="17AiGz48rhe", full_name="Maamoun Haj Najeeb")
        
#         tasks_data = {
#             "date": "2024-2-21",
#             "tasks": [
#                 {
#                     "time": 30,
#                     "piriority": "High",
#                     "title": "a new task"
#                 },
#                 {
#                     "time": 90,
#                     "piriority": "Med",
#                     "title": "an important task"
#                 }
#             ]
#         }
        
#         tasks = self.client.post(path=app_url, data=tasks_data, format="json"
#             , headers=dict(Authorization=f"Bearer {self.create_access_token()}"))
    
#     def create_access_token(self):
#         response = self.client.post(
#             path=login_url, data=dict(email="maamoun.haj.najeeb@gmail.com", password="17AiGz48rhe"))
        
#         return response.json().get("access")
    
#     def test_bulk_delete_task(self):
#         ids = [str(todo.id) for todo in models.ToDo.objects.all()]
#         url = f"{app_url}bulk_delete/"
#         response = self.client.delete(path=url, data={"ids": ", ".join(ids)}
#             , headers=dict(Authorization=f"Bearer {self.create_access_token()}"))
        
#         self.assertEqual(response.json().get("message"), "All elements deleted successfully")
#         self.assertEqual(response.status_code, status.HTTP_200_OK)


# class BulkDeleteUnAuthorizedTestCase(APITestCase):
#     def test_bulk_delete_task(self):
#         url = f"{app_url}bulk_delete/"
#         response = self.client.delete(path=url, data={"ids": "1, 2"})
        
#         self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


# class BulkDeleteNotFoundIdsTestCase(APITestCase):
#     def setUp(self) -> None:
#         self.user = Users.objects.create_user(
#             email="maamoun.haj.najeeb@gmail.com", password="17AiGz48rhe", full_name="Maamoun Haj Najeeb")
        
#         tasks_data = {
#             "date": "2024-2-21",
#             "tasks": [
#                 {
#                     "time": 30,
#                     "piriority": "High",
#                     "title": "a new task"
#                 },
#                 {
#                     "time": 90,
#                     "piriority": "Med",
#                     "title": "an important task"
#                 }
#             ]
#         }
        
#         tasks = self.client.post(path=app_url, data=tasks_data, format="json"
#             , headers=dict(Authorization=f"Bearer {self.create_access_token()}"))
    
#     def create_access_token(self):
#         response = self.client.post(
#             path=login_url, data=dict(email="maamoun.haj.najeeb@gmail.com", password="17AiGz48rhe"))
        
#         return response.json().get("access")
    
#     def test_bulk_delete_task(self):
#         url = f"{app_url}bulk_delete/"
#         response = self.client.delete(path=url, data=dict(ids="32, 22")
#             , headers=dict(Authorization=f"Bearer {self.create_access_token()}"))
        
#         self.assertEqual(response.json().get("message")
#             , "0 item has been deleted, this ids [32, 22] doesn't exist in the database")
#         self.assertEqual(response.status_code, status.HTTP_200_OK)


