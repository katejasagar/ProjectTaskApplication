**Create an environment**

  For Windows:

  mkvirtualenv taskenvironment
  
  workon taskenvironment 

**Installing dependencies**

install django : pip install django

install restframework : pip install djangorestframework - for creating rest APIs

install cors-headers : pip install djangorestframework django-cors-headers - for connecting frontend to backend

install Pillow : pip install Pillow - for images

**To run the backend**

Step 1: Open your terminal

Step 2: clone the project using **git clone https://github.com/katejasagar/ProjectTaskBackend.git**

Step 3: Go to the ProjectTaskFolder

Step 4: Migrate the database using:

  1. python manage.py makemigrations

  2. python manage.py migrate

Step 5: Creating superuser

run **python manage.py createsuperuser**

  Enter the following details:

  Username:

  email:

  Password: 
  
  Confirm Password:
  
Step 6: Run the server

  1. python manage.py runserver

**Below is the table for URL endpoints**

  can be tested by Postman
  
|Endpoints|Requests|Function|
|------|-----|-----|
|/projects/|GET|To list all the projects|
|/projects/|POST|To create a new project|
|/tasks/|POST|To create new post|
|/projects/project_id|GET|To list specific projects with its tasks|
|/projects/project_id/tasks/task_id/|GET|To view specific task details|
|/projects/projects_id/update/|PUT|To update the specific project|
|/projects/projects_id/update/|DELETE|To delete the specific project|
|/tasks/task_id/update/|PUT|To update the specific task|
|/tasks/task_id/update/|DELETE|To delete the specific task|


