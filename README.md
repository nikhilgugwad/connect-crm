# ConnectCRM

## Table of Contents

1. [Introduction](#introduction)
2. [Tech Stack Used](#tech-stack-used)
3. [Folder Structure](#folder-structure)
4. [Setup Instructions](#setup-instructions)
5. [API Endpoints](#api-endpoints)
6. [Authentication and Permissions](#authentication-and-permissions)
7. [Deployment](#deployment)
8. [Testing and Debugging](#testing-and-debugging)
9. [Future Improvements](#future-improvements)
10. [Collaborations and Contributions](#collaborations-and-contributions)

---

## 1. Introduction

Welcome to the **ConnectCRM Backend** project! ConnectCRM is a Customer Relationship Management (CRM) system designed to help manage customers, sales opportunities, and interactions in an organization. The backend is developed using **Django**, and it exposes RESTful APIs for easy communication between the frontend and the backend. This project is deployed on **Heroku** and uses **Amazon RDS** for database management.

### Core Features

- **User Roles**: Different roles like Admin, Salesperson, and Customer with distinct permissions.
- **Customer Management**: Create, update, and delete customer details.
- **Sales Opportunity Management**: Create, track, and manage sales opportunities.
- **Interaction Tracking**: Record various interactions with customers such as calls, meetings, and emails.

---

## 2. Tech Stack Used

- **Backend Framework**: Django 5.1
- **API Framework**: Django REST Framework (DRF)
- **Database**: MySQL (via Amazon RDS)
- **Authentication**: JWT (JSON Web Tokens) using `djangorestframework-simplejwt`
- **Deployment**: Heroku
- **Permissions**: Custom permissions for role-based access (Admin, Salesperson, Customer)
- **Environment Variables**: Managed via Heroku config for sensitive settings (e.g., `DJANGO_SECRET_KEY`, `DATABASE_URL`)

---

## 3. Folder Structure

The project is structured in a typical Django project format with some specific configurations for REST API development. Here is an overview of the folder structure:

```
connectcrm/
├── api/
│   ├── migrations/            # Auto-generated migrations for the database
│   ├── __init__.py            # Marks this directory as a Python package
│   ├── admin.py               # Registers models for the admin panel
│   ├── apps.py                # App configuration
│   ├── models.py              # Defines the models for the database (CustomUser, Customer, etc.)
│   ├── permissions.py         # Custom permission classes (IsAdmin, IsSalesperson, etc.)
│   ├── serializers.py         # Serializers for transforming data
│   ├── urls.py                # URL routing for the API endpoints
│   ├── views.py               # Views and API logic (viewsets)
├── connectcrm/
│   ├── __init__.py            # Marks this directory as a Python package
│   ├── settings.py            # Configuration settings for Django
│   ├── urls.py                # Project-level URL routing
│   ├── wsgi.py                # WSGI configuration for deployment
├── manage.py                  # Django's command-line utility
└── requirements.txt           # Python dependencies
```

### Breakdown of Important Files

1. **api/models.py**: Defines the models for `CustomUser`, `Customer`, `SalesOpportunity`, and `Interaction`. These are the core entities of the CRM system.
2. **api/serializers.py**: Contains serializers that convert complex data types (like model instances) into Python data types and vice versa.
3. **api/views.py**: Contains the viewsets that handle API requests for the resources like users, customers, and opportunities.
4. **api/permissions.py**: Custom permission classes that define access controls based on user roles (Admin, Salesperson, Customer).
5. **api/urls.py**: Defines the URL patterns for all the API endpoints related to the models.
6. **connectcrm/settings.py**: Configuration file for the Django settings like database configuration, middleware, installed apps, etc.
7. **requirements.txt**: Lists all Python dependencies for the project.

---

## 4. Setup Instructions

To set up the project locally or in a development environment, follow these steps:

### Prerequisites

- Python 3.9 or later
- pip (Python package manager)
- Virtual environment (recommended)
- MySQL (for local development, if not using RDS)
- Heroku CLI (if deploying to Heroku)

### Steps for Local Setup

1. **Clone the Repository**

   ```bash
   git clone <repo-url>
   cd connectcrm
   ```

2. **Set Up Virtual Environment**
   Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```

3. **Install Dependencies**
   Install the required dependencies from `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Database (for local setup)**
   If you are not using Amazon RDS, configure the local MySQL database in `settings.py` under `DATABASES`.

5. **Apply Database Migrations**
   Run the migrations to create the necessary database tables:

   ```bash
   python manage.py migrate
   ```

6. **Create a Superuser (Optional)**
   If you'd like to access the Django admin interface, create a superuser:

   ```bash
   python manage.py createsuperuser
   ```

7. **Run the Development Server**
   Start the local development server:

   ```bash
   python manage.py runserver
   ```

8. **Access the App Locally**
   Visit `http://127.0.0.1:8000` in your browser to access the API.

---

## 5. API Endpoints

### Base URL

The base URL for the API is:

```
https://connectcrm-bb1693933592.herokuapp.com/api/
```

### Authentication

- **Token-based Authentication**: The API uses JWT (JSON Web Tokens) for user authentication.
- **Obtain JWT Token**:
  - Endpoint: `POST /token/`
  - Required fields: `username`, `password`
  - Response: `{ "access": "JWT_TOKEN", "refresh": "REFRESH_TOKEN" }`

- **Refresh JWT Token**:
  - Endpoint: `POST /token/refresh/`
  - Required fields: `refresh_token`
  - Response: `{ "access": "NEW_JWT_TOKEN" }`

### Available API Endpoints

- **Users** (`/users/`): CRUD operations for users, accessible only by admins.
- **Customers** (`/customers/`): Create, read, update, and delete customers, accessible by admins and salespersons.
- **Sales Opportunities** (`/opportunities/`): Manage sales opportunities, accessible by admins and salespersons.
- **Interactions** (`/interactions/`): CRUD operations for interactions with customers, accessible by admins, salespersons, and customers (limited to their own interactions).

---

## 6. Authentication and Permissions

The project uses **JWT authentication**. Users need to authenticate using the `/token/` endpoint and send the token in the `Authorization` header for subsequent API requests.

### Custom Permissions

- **IsAdmin**: Only users with the `admin` role can access certain endpoints.
- **IsSalesperson**: Only users with the `sales` role can manage customers and opportunities.
- **IsCustomer**: Customers can only access their own interactions.

---

## 7. Deployment

### Deployment on Heroku

The ConnectCRM backend is deployed on Heroku. To deploy, we followed these steps:

1. **Heroku CLI Setup**: We used the Heroku CLI to push the code to the Heroku app:

   ```bash
   git push heroku main
   ```

2. **Database Configuration**: We connected the project to Amazon RDS for MySQL database management, setting up environment variables on Heroku for `DATABASE_URL` and `DJANGO_SECRET_KEY`.
3. **Migrations on Heroku**: After deployment, we ran the database migrations:

   ```bash
   heroku run python manage.py migrate
   ```

4. **Access the App**: The app is available at the URL: [https://connectcrm-bb1693933592.herokuapp.com/](https://connectcrm-bb1693933592.herokuapp.com/).

---

## 8. Testing and Debugging

- **Testing the API**: The API can be tested using tools like **Postman** or **curl** by sending requests to the API endpoints.
- **Logs**: For debugging, Heroku logs can be accessed using:

   ```bash
   heroku logs --tail
   ```

---

## 9. Future Improvements

- **Frontend Integration**: We can integrate a frontend (e.g., React, React Native) to provide a full-stack solution for CRM.
- **Role-based Views**: Enhance user roles with more granular permissions for better access control.
- **Analytics Dashboard**: Add features like reporting and analytics for sales and interactions.
- **Third-Party Integrations**: Integrate with third-party tools like email services, CRM platforms, or social media.

---

## 10. Collaborations and Contributions

This project was developed as part of a learning journey. Contributions are welcome! If you'd like to contribute, you can:

- Fork the repository and make your changes.
- Open a pull request with a clear description of the changes you’ve made.
