Project - EventAPI

To build a simplified event management API for an admin panel, where it supports role-based access (Admin and User), event creation, and basic ticket purchases.

* Setting up Django Project
1. Install all the Required Packages
    - pip install -r requirements.txt
2. Create the Django Project
    - django-admin startproject EventAPI
    - cd EventAPI
3. Create the App
    - python manage.py startapp api

* Set up MySQL Database
    - Create a db named eventapi_db
    - Update db details in settings.py

* Run migrations after setting up your models
    - python manage.py makemigrations
    - python manage.py migrate

* Run the server
    - python manage.py runserver


API Endpoints:-
1. User Registration:
    HTTP method : POST
    url - http://127.0.0.1:8000/api/register/
    payload - {
    "username": "<testuser>", 
    "password": "<testpassword>", 
    "role": "<admin/user>"
    }

2. Event Management:
   a. Create a new event (Admin only)
    - Create JWT token for authorization
        HTTP method : POST 
        url - http://127.0.0.1:8000/api/token/
        payload - {
        "username": "<admin-username>",
        "password": "<admin-password>"
        }

    - Create new event
      HTTP method : POST
      url - http://127.0.0.1:8000/api/events/
      Authorization - Bearer Token - paste token generated from JWT
      payload - {
       "name": "<event-name>",
       "date": "<date>",
       "total_tickets": <total-tickets>,
       "tickets_sold": <total-sold-tickets> #optional
        }
    
    b. Fetch all events 
       HTTP method : GET
       url - http://127.0.0.1:8000/api/events/

3. Ticket Purchase:
    - Create JWT token for authorization
        HTTP method : POST 
        url - http://127.0.0.1:8000/api/token/
        payload - {
        "username": "<user-username>",
        "password": "<user-password>"
        }

    - Purchase tickets for an event
      HTTP method : POST
      url - http://127.0.0.1:8000/api/events/{id}/purchase/
      Authorization - Bearer Token - paste token generated from JWT
      payload - {
       "quantity": <number_of_tickets>
        }

4. Custom SQL Query:
    - Create JWT token for authorization
        HTTP method : POST 
        url - http://127.0.0.1:8000/api/token/
        payload - {
        "username": "<user-username>",
        "password": "<user-password>"
        }
    - To fetch the total tickets sold for all events along with event details and return the top 3 events by tickets sold
      HTTP method : GET
      url - http://127.0.0.1:8000/api/top-events/
      Authorization - Bearer Token - paste token generated from JWT
      SQL Query - 
            SELECT id, name, date, total_tickets, tickets_sold
            FROM api_event
            ORDER BY tickets_sold DESC
            LIMIT 3;
    
