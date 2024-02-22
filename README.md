# ToDo RestAPI
It's an API to schedule your tasks throught your life.

## Motivation
As a Developer who wakes up at 5 AM every morning and has tons of tasks needed to be done, you really need a tool that simplifies sceduling (daily, weekly, monthly) goals and that's what I did.
A simple ToDo RestAPI Django app with robust features.

## Cloning this project
Initially you need python 3.10 or higher installed on your local machine
Then:
- open a folder and build virtual environment within via these commands:
1. `virtualenv .venv`
2. `.venv\scripts\activate` for windows</br>
(if you are on mac or linux do this instead:
`source .venv/bin/activate`)
- then clone the repo:</br>
`git clone https://github.com/maamounhajnajeeb/ToDo-App.git`
- now it's dependencies time:</br>
`pip install -r requirements.txt`</br>
here  you have to wait for some time until the dependencies installed suucessfully</br>
actually the dependencies aren't that much (you can check it form **requirements.txt** file)
- write the desired environment variables
actually you need to add: SECRET_KEY, ALLOWED_HOSTS and Database Configuaration
- after that write Django magic commands:</br>
`python manage.py migrate`</br>
`python manage.py runserver`</br>
**Note**: there's gunicorn dependecy in the requirements, but it's for production not development.

## Website & docs
- Check Backend API docs from here: 
- Web app:
- Mobile app:
- Mobile app source code:

## Project Features
The project has two apps: Users app which responsible for authentication and Todo app which responsible for sceduling user task and other CRUD operation.

API hierarchy:</br>
Users App:</br>
|- `/api/v1/users/sign_up/`</br>
|- `/api/v1/users/sign_in/`</br>
|- `/api/v1/users/refresh_token/`</br>
|- `/api/v1/users/<int:user_id>/` (for read, update, delete operations)</br>
|- `/api/v1/users/validate_current_password/`</br>
|- `/api/v1/users/new_password/`</br>

ToDo App:</br>
|- `/api/v1/todo/` (to create task)</br>
|- `/api/v1/todo/<int:task_id>/` (for task read, update, delete operations)</br>
|- `/api/v1/todo/bulk_delete/`</br>
|- `/api/v1/todo/user_tasks/`</br>
|- `/api/v1/todo/search/<str:search_term>/` (for searching in the user's tasks via task title)</br>
|- `/api/v1/todo/user_tasks/<int:year>/<int:month>/<int:day>/` (users tasks on specified date)</br>
