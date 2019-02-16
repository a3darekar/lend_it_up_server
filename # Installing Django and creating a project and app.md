# Installing Django and creating a project and app

First, make sure you have Django installed along with other dependancies. Assuming you are using virtualenv, a simple "pip install -r requirement.txt" should suffice.

Enter into the directory with manage.py and run 
	```./manage.py migrate``` 
to initialize database tables in SQLite

Now run 
	```	./manage.py createsuperuser ```
command to initialize an administrator account over the system.

finally run 
	```./manage.py runserver 0.0.0.0:8000```
to initialize the RESTful API for interaction with Angular App.


