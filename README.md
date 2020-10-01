## Description
Sample project to test the Flask module and create a simple API

This project is not production ready, it is a simple showcase of the technology


## Install
You will need to have python installed in your system

Clone the repository and go to the project folder

First you will need to create the virtual enviroment
```bash
python -m venv .venv
```
__Note__: You can install the virtual enviroment in wherever path you want, but '.env' is in the '.gitignore' file

Activate the virtual enviroment and install the dependencies 
```
source .venv/bin/activate
pip install -e api_python/
```
Create your '.env' file, an '.env.example' is provided, it should be created at the same level that the example

Init the database and add some users to test the API
```
flask init-db
flask add-user EMAIL PASSWORD USER_TYPE
```
Where the type of user can be 'user' or 'admin'

Now you just have to run the application with
```
flask run
```
And the application will be running in port 5000

__Note:__ each time you want to run the application you need to activate the virtual enviroment, and run the 'flask run' command, the other steps are not necessary


## Application
It is a restful API with two resources 'public' and 'private', the resources have the same two fields and the operations allowed in each one are the same, only the necessary credentials to operate them change.

You can make POST (create), GET (read), PUT (update), DELETE (delete) requests to '/public/\<public-id>' or '/private/\<private-id>' to interact with them (if no id provided in read all the resources are returned). See 'api_python/routes/' for further details

Credentials needed for each request are:
|        | public    | private |
|--------|-----------|---------|
| GET    | no needed | admin   |
| POST   | user      | admin   |
| PUT    | user      | admin   |
| DELETE | admin     | admin   |


This app uses JWT (more info in https://jwt.io/) for authorization, to get the token you will need to log in sending a POST request to 'auth/login' with the body (you need to indicate the body is a json in the header too)
```json
{
	"email": email,
	"password": password
}
```
This will give you the token which provides your credentials, you have to add it in the header of the requests like
```json
{
	"Authorization": "Bearer " + JWT
}
```