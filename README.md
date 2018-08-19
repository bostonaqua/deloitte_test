# Test app for Deloitte

## Simple user management web-service


### Used technologies:
* Framework: Flask
* DBMS: PostgreSQL

### Description:

Service have following functionality: 
* Login
* Adding new users (only logged in users can add new users)
* Removing existing users (only logged in users can remove users)
* Logout

Consists following pages:
* Login page (starting page, user can login through it using name and password)
* Adding/removing user page (after login page user gets here)

Project already have one superuser. This user can't be deleted. Superuser is:
```angular2html
Username: admin
Password: admin
```

### Setup instruction:

Clone project from GitHub:

```angular2html
git clone https://github.com/bostonaqua/deloitte_test.git
```

Create database in PosgreSQL and change credential data in config.py. For example:

```angular2html
db_name = 'deloitte'
db_user = 'postgres'
db_pass = 'postgres'
db_host = 'localhost'
```

Virtual environment is already in project and uses python3.6 interpreter.
Go to the project directory and run bash script for starting web-service:

```angular2html
cd deloitte_test/
bash run.sh
```

Open your browser and go to URL:
```angular2html
http://127.0.0.1:5000/
```
