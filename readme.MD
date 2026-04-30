# steps 
1. systems plan (diagrams )
2. set up my virtual environment for the project
`python 3 -m venv` venv and activate with `source venv/bin/activate`
3. install django framework 
`pip isntall django`
>optionally verify the installation by running `djangonadmin --version` or `python3 -m django --version`
4. Create the django project `django-admin startproject taxes`
5. change the directory into the project folder  `cd taxes`
> optionally test your server  `python3 manage.py runserver`
6.Create the django app `django-admin startapp web`
7. register the django applictions in the `settings.py` under the `installed Apps` array

## working with the URLS views and templates 
p