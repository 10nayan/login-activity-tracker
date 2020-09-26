# User authentication and activity tracker API using Django and deployed in Heroku
## Introduction
This application is built with Django which is a python framework for web development.
You can check out this application clicking here, https://fullthrottlenayan.herokuapp.com/signin
This application has basic features of signin,signout and signup. User information after signup is stored in heroku postgres database. After  signin and signout of every user the activity duration
along with timezone is stored in another model Activity and user is redirects to to home page where user activity API is generated. As soon as user sign in timezone,start_time and end_time 
is fenerated in API, after signout end_time is updated with current time.
## Files in the project
- **/ftl/views.py**: This is the app file that contains the logic of all the view functions in the backend which generate dynamic contents to HTML template and API.
- **/ftl/models.py**: Contains Django models used for storing user activity data.
- **/ftl/forms.py**: python app file  required for creating form in this appliation.
- **/ftl/urls.py**: python app file  required for url mapping to all the view functions.
- **/ftl/admin.py**: python app file  required for registering models to django-administration of this appliation.
- **/ftl/tests.py**: python app file  required for testing of this appliation.
- **/ftl/signals.py**: python app file  required for sending signin and signout signals.
- **/ftl/apps.py**: python app file  required for registering the ftl app to django movie_site project of this appliation.
- **/ftl_assignment/**: python main project folder in which movie app is created.
- **Procfile**: file required for deployment in heroku.
- **requirements.txt**: list of Python packages installed (also required for Heroku)
- **ftl/templates/**: folder with all HTML files
