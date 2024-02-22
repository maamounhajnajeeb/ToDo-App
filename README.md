# ToDo RestAPI
It's an API to schedule your tasks throught your life

## Motivation
As a Developer who wakes up at 5 AM every morning and has tons of tasks needed to be done, you really need a tool that simplifies sceduling (daily, weekly, monthly) goals and that's what I did.
A simple ToDo RestAPI Django app with robust features

## Cloning this project
Initially you need python 3.10 or higher installed on your local machine
Then:
- open a folder and build virtual environment within via these commands:
1. `virtualenv .venv`
2. `.venv\scripts\activate` for windows
if you are on mac on linux do this instead:
`source .venv/bin/activate`
- then clone the repo:
`git clone https://github.com/maamounhajnajeeb/ToDo-App.git`
- now it's dependencies time:
`pip install -r requirements.txt`
here  you have to wait for some time until the dependencies installed suucessfully
actually the dependencies aren't that much (you can check it form **requirements.txt** file)
- write the desired environment variables
actually you need to add: SECRET_KEY, ALLOWED_HOSTS and Database Configuaration
- after thar write Django magic commands:
`python manage.py migrate`
`python manage.py runserver`
**Note**: there's gunicorn dependecy in the requirements, but it's for production not development

## Website & docs
- Check the docs from here: 
- Web app:
- Mobile app:
- Mobile app source code:

