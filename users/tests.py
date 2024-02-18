from django.contrib.auth import get_user_model

from rest_framework.test import APITestCase
from rest_framework import status



Users = get_user_model()

class SuccessUserCreateTestCase(APITestCase):
    
    def test_unauthenticated_user_sign_up(self):
        url = "/api/v1/users/sign_up/"
        response = self.client.post(
            path=url,
            data=dict(full_name="Maamoun Haj Najeeb", email="maamoun3911@gmail.com"
                , password="sv_gtab101enter", re_password="sv_gtab101enter"
                ) 
            )
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json().get("email"), "maamoun3911@gmail.com")


class FailUserCreateTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = Users.objects.create_user(
            email="teachermaamoun@hotmail.com", password="sv_gtab101enter", full_name="Maamoun Haj Najeeb")
        
    def sign_in(self) -> str:
        url = "/api/v1/users/sign_in/"
        response = self.client.post(
            path=url,
            data=dict(email="teachermaamoun@hotmail.com", password="sv_gtab101enter")
            )
        access = response.json().get("access")
        return access
        
    def test_unauthenticated_user_sign_up(self):
        url = "/api/v1/users/sign_up/"
        response = self.client.post(
            path=url,
            headers={"Authorization": f"Bearer {self.sign_in()}"},
            data=dict(email="maamounteacher@hotmail.com", password="sv_gtab101enter"
                    , re_password="sv_gtab101enter", full_name="Maamoun Haj Najeeb"
                )
            )
        
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class BadRequestUserCreateTestCase(APITestCase):
    def test_bad_request_user_creation(self):
        url = "/api/v1/users/sign_up/"
        
        keys = ["password", "re_password", "email", "full_name"]
        for index in range(4):
            data = dict(email="maamounteacher@hotmail.com", password="sv_gtab101enter"
                    , re_password="sv_gtab101enter", full_name="Maamoun Haj Najeeb")
            data.pop(keys[index])
            
            response = self.client.post(path=url, data=data)
            
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class NotSamePasswordUserCreateTestCase(APITestCase):
    def test_bad_request_user_creation(self):
        url = "/api/v1/users/sign_up/"
        data = dict(email="maamounteacher@hotmail.com", password="sv_gtab101enter"
                , re_password="sv_gtab101ente", full_name="Maamoun Haj Najeeb")
        
        response = self.client.post(path=url, data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class RepeatedEmailUserCreateTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = Users.objects.create_user(
            email="maamounteacher@hotmail.com", password="sv_gtab101enter", full_name="Maamoun Haj Najeeb")
    
    def test_bad_request_user_creation(self):
        url = "/api/v1/users/sign_up/"
        data = dict(email="maamounteacher@hotmail.com", password="sv_gtab101enter"
                , re_password="sv_gtab101enter", full_name="Maamoun Haj Najeeb")
        
        response = self.client.post(path=url, data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class LongPasswordUserCreateTestCase(APITestCase):
    def test_bad_request_user_creation(self):
        url = "/api/v1/users/sign_up/"
        data = dict(email="maamounteacher@hotmail.com", password="1"*129
                , re_password="1"*129, full_name="Maamoun Haj Najeeb")
        
        response = self.client.post(path=url, data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class RefreshTokenTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = Users.objects.create_user(
            email="maamoun3911@gmail.com", password="sv_gtab101enter", full_name="Maamoun Haj Najeeb")
    
    def sign_in(self):
        url = "/api/v1/users/sign_in/"
        response = self.client.post(
            path=url, data=dict(email="maamoun3911@gmail.com", password="sv_gtab101enter"))
        return response.json().get("access"), response.json().get("refresh")
    
    def test_refresh_token(self):
        url = "/api/v1/users/refresh_token/"
        response = self.client.post(
            path=url, headers=dict(Authorization=f"Bearer {self.sign_in()[0]}")
            , data=dict(refresh=self.sign_in()[1]))
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 2)


class ValidateCurrentPasswordTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = Users.objects.create_user(
            email="maamoun3911@gmail.com", password="sv_gtab101enter", full_name="Maamoun Haj Najeeb")
    
    def sign_in(self):
        url = "/api/v1/users/sign_in/"
        response = self.client.post(
            path=url, data=dict(email="maamoun3911@gmail.com", password="sv_gtab101enter"))
        return response.json().get("access"), response.json().get("refresh")
    
    def test_check_current_password(self):
        url = "/api/v1/users/validate_current_password/"
        response = self.client.post(
            path=url, data=dict(password="sv_gtab101enter")
            , headers=dict(Authorization=f"Bearer {self.sign_in()[0]}"))
        
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)


class UnAuthorizedValidateCurrentPasswordTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = Users.objects.create_user(
            email="maamoun3911@gmail.com", password="sv_gtab101enter", full_name="Maamoun Haj Najeeb")
    
    def test_check_current_password(self):
        url = "/api/v1/users/validate_current_password/"
        response = self.client.post(path=url, data=dict(password="sv_gtab101enter"))
        
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class BadRequestValidateCurrentPasswordTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = Users.objects.create_user(
            email="maamoun3911@gmail.com", password="sv_gtab101enter", full_name="Maamoun Haj Najeeb")
    
    def sign_in(self):
        url = "/api/v1/users/sign_in/"
        response = self.client.post(
            path=url, data=dict(email="maamoun3911@gmail.com", password="sv_gtab101enter"))
        return response.json().get("access"), response.json().get("refresh")
    
    def test_check_current_password(self):
        url = "/api/v1/users/validate_current_password/"
        response = self.client.post(path=url, headers=dict(authorization=f"Bearer {self.sign_in()[0]}"))
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class NotAcceptableValidateCurrentPasswordTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = Users.objects.create_user(
            email="maamoun3911@gmail.com", password="sv_gtab101enter", full_name="Maamoun Haj Najeeb")
    
    def sign_in(self):
        url = "/api/v1/users/sign_in/"
        response = self.client.post(
            path=url, data=dict(email="maamoun3911@gmail.com", password="sv_gtab101enter"))
        return response.json().get("access"), response.json().get("refresh")
    
    def test_check_current_password(self):
        url = "/api/v1/users/validate_current_password/"
        response = self.client.post(path=url, data=dict(password="sb_gtab101enter")
                , headers=dict(authorization=f"Bearer {self.sign_in()[0]}"))
        
        self.assertEqual(response.status_code, status.HTTP_406_NOT_ACCEPTABLE)


class ChangePasswordTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = Users.objects.create_user(
            email="maamoun3911@gmail.com", password="sv_gtab101enter", full_name="Maamoun Haj Najeeb")
    
    def sign_in(self):
        url = "/api/v1/users/sign_in/"
        response = self.client.post(
            path=url, data=dict(email="maamoun3911@gmail.com", password="sv_gtab101enter"))
        return response.json().get("access"), response.json().get("refresh")
    
    def test_change_password(self):
        url = "/api/v1/users/new_password/"
        data = dict(password="sb_gtab101enter", re_password="sb_gtab101enter")
        response = self.client.post(
            path=url, data=data, headers=dict(Authorization=f"Bearer {self.sign_in()[0]}"))
        
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertEqual(response.json().get("Success"), "Password changed successfully")


class DifferentFieldsChangePasswordTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = Users.objects.create_user(
            email="maamoun3911@gmail.com", password="sv_gtab101enter", full_name="Maamoun Haj Najeeb")
    
    def sign_in(self):
        url = "/api/v1/users/sign_in/"
        response = self.client.post(
            path=url, data=dict(email="maamoun3911@gmail.com", password="sv_gtab101enter"))
        return response.json().get("access"), response.json().get("refresh")
    
    def test_change_password(self):
        url = "/api/v1/users/new_password/"
        data = dict(password="sb_gtab101enter1", re_password="sb_gtab101enter")
        response = self.client.post(
            path=url, data=data, headers=dict(Authorization=f"Bearer {self.sign_in()[0]}"))
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json().get("Error")[0], "Password and re_password fields must be the same")


class RequiredFieldErrorChangePasswordTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = Users.objects.create_user(
            email="maamoun3911@gmail.com", password="sv_gtab101enter", full_name="Maamoun Haj Najeeb")
    
    def sign_in(self):
        url = "/api/v1/users/sign_in/"
        response = self.client.post(
            path=url, data=dict(email="maamoun3911@gmail.com", password="sv_gtab101enter"))
        return response.json().get("access"), response.json().get("refresh")
    
    def test_change_password(self):
        url = "/api/v1/users/new_password/"
        data = dict(password="sb_gtab101enter1")
        response = self.client.post(
            path=url, data=data, headers=dict(Authorization=f"Bearer {self.sign_in()[0]}"))
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UnAuthorizedFieldsChangePasswordTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = Users.objects.create_user(
            email="maamoun3911@gmail.com", password="sv_gtab101enter", full_name="Maamoun Haj Najeeb")
    
    def test_change_password(self):
        url = "/api/v1/users/new_password/"
        data = dict(password="sb_gtab101enter1", re_password="sb_gtab101enter")
        response = self.client.post(path=url, data=data)
        
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class UsersTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = Users.objects.create_user(
            email="maamoun3911@gmail.com", password="sv_gtab101enter", full_name="Maamoun Haj Najeeb")
    
    def sign_in(self):
        url = "/api/v1/users/sign_in/"
        response = self.client.post(
            path=url, data=dict(email="maamoun3911@gmail.com", password="sv_gtab101enter"))
        return response.json().get("access"), response.json().get("refresh"), response.json().get("user_id")
    
    def test_get(self):
        url = f"/api/v1/users/{self.sign_in()[2]}/"
        response = self.client.get(
            path=url, headers=dict(Authorization=f"Bearer {self.sign_in()[0]}"))
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get("email"), "maamoun3911@gmail.com")
    
    def test_patch(self):
        url = f"/api/v1/users/{self.sign_in()[2]}/"
        response = self.client.patch(
            path=url, headers=dict(Authorization=f"Bearer {self.sign_in()[0]}")
            , data=dict(email="teachermaamoun@hotmail.com"))
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get("email"), "teachermaamoun@hotmail.com")
    
    def test_delete(self):
        url = f"/api/v1/users/{self.sign_in()[2]}/"
        response = self.client.delete(
            path=url, headers=dict(Authorization=f"Bearer {self.sign_in()[0]}"))
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class PermissionDeniendUsersTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = Users.objects.create_user(
            email="maamoun3911@gmail.com", password="sv_gtab101enter", full_name="Maamoun Haj Najeeb")
        self.second_user = Users.objects.create_user(
            email="computerscience.magic@gmail.com", password="sv_gtab101enter", full_name="Khaled Zetoun")
    
    def sign_in(self):
        url = "/api/v1/users/sign_in/"
        response = self.client.post(
            path=url, data=dict(email="maamoun3911@gmail.com", password="sv_gtab101enter"))
        second_response = self.client.post(
            path=url, data=dict(email="computerscience.magic@gmail.com", password="sv_gtab101enter"))
        return response.json().get("access"), second_response.json().get("access"), response.json().get("user_id")
    
    def test_get(self):
        url = f"/api/v1/users/{self.sign_in()[2]}/"
        response = self.client.get(
            path=url, headers=dict(Authorization=f"Bearer {self.sign_in()[1]}"))
        
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_patch(self):
        url = f"/api/v1/users/{self.sign_in()[2]}/"
        response = self.client.patch(
            path=url, headers=dict(Authorization=f"Bearer {self.sign_in()[1]}")
            , data=dict(email="teachermaamoun@hotmail.com"))
        
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_delete(self):
        url = f"/api/v1/users/{self.sign_in()[2]}/"
        response = self.client.delete(
            path=url, headers=dict(Authorization=f"Bearer {self.sign_in()[1]}"))
        
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class PermissionDeniendUsersTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = Users.objects.create_user(
            email="maamoun3911@gmail.com", password="sv_gtab101enter", full_name="Maamoun Haj Najeeb")
        self.second_user = Users.objects.create_user(
            email="computerscience.magic@gmail.com", password="sv_gtab101enter", full_name="Khaled Zetoun")
    
    def sign_in(self):
        url = "/api/v1/users/sign_in/"
        response = self.client.post(
            path=url, data=dict(email="maamoun3911@gmail.com", password="sv_gtab101enter"))
        return response.json().get("access"), response.json().get("user_id")
    
    def test_get(self):
        url = f"/api/v1/users/{self.sign_in()[1]}/"
        response = self.client.get(path=url)
        
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_patch(self):
        url = f"/api/v1/users/{self.sign_in()[1]}/"
        response = self.client.patch(path=url, data=dict(email="teachermaamoun@hotmail.com"))
        
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_delete(self):
        url = f"/api/v1/users/{self.sign_in()[1]}/"
        response = self.client.delete(path=url)
        
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class PostivePKNotFoundUsersTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = Users.objects.create_user(
            email="maamoun3911@gmail.com", password="sv_gtab101enter", full_name="Maamoun Haj Najeeb")
    
    def sign_in(self):
        url = "/api/v1/users/sign_in/"
        response = self.client.post(
            path=url, data=dict(email="maamoun3911@gmail.com", password="sv_gtab101enter"))
        return response.json().get("access")
    
    def test_get(self):
        url = f"/api/v1/users/200/"
        
        response = self.client.get(path=url, headers=dict(Authorization=f"Bearer {self.sign_in()}"))
        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.json().get("detail"), "Not found.")
    
    def test_patch(self):
        url = f"/api/v1/users/200/"
        response = self.client.patch(path=url, data=dict(email="teachermaamoun@hotmail.com")
                , headers=dict(Authorization=f"Bearer {self.sign_in()}"))
        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.json().get("detail"), "Not found.")
    
    def test_delete(self):
        url = f"/api/v1/users/200/"
        response = self.client.delete(path=url, headers=dict(Authorization=f"Bearer {self.sign_in()}"))
        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.json().get("detail"), "Not found.")


class NegativePKNotFoundUsersTestCase(APITestCase):
    """
    This test will make a request to un registred url, negative pk in urls are'nt same with positive ones
    """
    def setUp(self) -> None:
        self.user = Users.objects.create_user(
            email="maamoun3911@gmail.com", password="sv_gtab101enter", full_name="Maamoun Haj Najeeb")
    
    def sign_in(self):
        url = "/api/v1/users/sign_in/"
        response = self.client.post(
            path=url, data=dict(email="maamoun3911@gmail.com", password="sv_gtab101enter"))
        return response.json().get("access")
    
    def test_get(self):
        url = f"/api/v1/users/-200/"
        
        response = self.client.get(path=url, headers=dict(Authorization=f"Bearer {self.sign_in()}"))
        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_patch(self):
        url = f"/api/v1/users/-200/"
        response = self.client.patch(path=url, data=dict(email="teachermaamoun@hotmail.com")
                , headers=dict(Authorization=f"Bearer {self.sign_in()}"))
        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
    def test_delete(self):
        url = f"/api/v1/users/-200/"
        response = self.client.delete(path=url, headers=dict(Authorization=f"Bearer {self.sign_in()}"))
        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
