


This is boilerplate code in django to enable clients to upload files and for the company admin to download and delete the files.\

How to launch application:

``` bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser  # Create an admin user
python manage.py runserver
 # Run these line by line in terminal
```

Login to localhost:8000/admin and login with your superuser credentials which you created in terminal.

Create user. If you want the user credentials to be used by client, create the user (Enter a username and password), then navigate to that user by clicking the URL and then check the checkbox isClient = True. Dont check any other checkbox

If you want to create an admin user (Not the same as superuser), do the same process and check the checkbox isAdmin = True. Dont check any other checkbox

After creating your user, go to localhost:8000/login

If you are logging as client, login with client credentials. You will get option to upload file. You can upload the file

If you are loggin in as admin, login with admin credentials. You can download and delete files. (Not properly implemented yet)

Adding Azure Blob Storage

In `file_management\file_management\settings.py` add your azure account details. You can access these details after creating your azure storage account by going to security and networking. You can create a new container by going to data storage and then containers and creating a new container. You can access all this on portal.azure.com


Features to add:

- Design
- Multi file upload functionality
- Download and delete functionality for admin fix bugs