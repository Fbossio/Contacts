![GitHub watchers](https://img.shields.io/github/watchers/Fbossio/contacts?style=plastic) ![GitHub language count](https://img.shields.io/github/languages/count/Fbossio/contacts?style=plastic) ![GitHub](https://img.shields.io/github/license/Fbossio/contacts?style=plastic)

# Contacts

Clean contact manager web application built with HTML, CSS, Bootstrap and Javascript on the Front end and Python/Flask on the Back end.
You can register an account, login add your contacts.  User information and contacts are stored in a Postgresql database.

## Backend dependencies
In order to use this code, you need to install PostgreSQL in your local machine

## Quick Start
1. Download the code locally

```
git clone https://github.com/Fbossio/contacts
cd contacts
```
2. create and activate a virtual environment

```
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
source venv/bin/activate
```

3. Install dependencies

```
pip install -r requirements.txt
```

4. Create a postgres database locally and set and environmental variable `DATABASE_URL`

```
# Option 1:
## Open the config.py file and change the SQLALCHEMY_DATABASE_URI attribute of the 
## DevelopmentConfig class to point to your database.
## Use the following pattern: 
postgresql://your_user:your_password@localhost:5432/your_database

# Option 2:
## Export the environmental variable DATABASE_URL in the console
export DATABASE_URL=postgresql://your_user:your_password@localhost:5432/your_database
```

5. Migrate the database

```
## Delete the migration folder and enter the following commands:
flask db init
flask db migrate -m "Initial migrate"
flask db upgrade
```

6. Deploy the app in development mode

```
## Export env variables:
export FLASK_APP=website
export FLASK_ENV=development

## Run the app
flask run
```
