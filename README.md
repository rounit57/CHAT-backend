# Contact Page Backend API

This repository contains the **backend service** for the organization’s **Contact Us** page.

The backend handles:
- Receiving contact form submissions from the website
- Validating incoming data
- Storing submissions in a MySQL database
- Sending notification emails to the support team
- Providing REST APIs for frontend integration

The system is designed to be **reliable, secure, and production-ready**.

---

## 🚀 Features

- REST API built with **FastAPI**
- MySQL database integration using **SQLAlchemy**
- Email notifications via **SMTP (Outlook / Microsoft 365)**
- Clear separation of concerns (routes, services, models)
- Centralized logging and error handling
- Swagger API documentation for easy testing
- Environment-based configuration

---

## 🧠 How the System Works

### Contact Form Flow

1. User submits the Contact form from the website
2. Backend validates the request payload
3. Submission is **saved in the database**
4. A **notification email** is sent to the support mailbox
5. Backend responds with success to the frontend

> **Important:**  
> The database is the source of truth.  
> Even if email sending fails, the contact submission is still stored.

---

## 🛠️ Tech Stack

- Python 3.10+
- FastAPI
- Uvicorn
- SQLAlchemy
- MySQL
- PyMySQL
- SMTP (Outlook / Microsoft 365)

---

## 📁 Project Structure

backend/
├── app/
│ ├── main.py # FastAPI app entry point
│ ├── config.py # Environment configuration
│ ├── database.py # Database connection setup
│ ├── models.py # SQLAlchemy models
│ ├── schemas.py # Pydantic request schemas
│ ├── logger.py # Logging configuration
│ ├── routes/
│ │ └── contact.py # Contact form API routes
│ └── services/
│ └── email_service.py # Email notification logic
│
├── tests/
│ └── test_contact_flow.py # Test script (no frontend needed)
│
├── requirements.txt
├── .gitignore
├── README.md
└── .env # Environment variables (not committed)

---

## 📌 API Details

### Endpoint

POST /api/contact


---

### Request Payload

{
  "inquiry_type": "General",
  "first_name": "Ravi",
  "last_name": "Kumar",
  "email": "ravi@email.com",
  "state": "Tamil Nadu",
  "city": "Chennai",
  "zipcode": "600036",
  "message": "We would like to collaborate with your organization."
}

Required Fields
inquiry_type (General or Collaboration)
first_name
email
message
Optional fields:
last_name
state
city
zipcode

###Success Response
{
  "success": true,
  "message": "Thank you for contacting us."
}

⚙️ Local Setup Instructions

1️⃣ Prerequisites
Python 3.10 or above
MySQL Server (running locally or remotely)
Git

2️⃣ Clone the Repository
bash
git clone https://github.com/<your-username>/chat-backend.git
cd chat-backend

3️⃣ Create & Activate Virtual Environment
Windows
bash
Copy code
python -m venv env
env\Scripts\activate
macOS / Linux
bash
Copy code
python3 -m venv env
source env/bin/activate

4️⃣ Install Dependencies
pip install -r requirements.txt

5️⃣ Create .env File
Create a .env file in the project root:
APP_ENV=local

DB_HOST=localhost
DB_PORT=3306
DB_NAME=chat_db
DB_USER=CHAT_user
DB_PASSWORD=CHAT123

EMAIL_SENDER=support@yourorg.com
EMAIL_PASSWORD=<APP_PASSWORD_FROM_IT>
EMAIL_RECEIVER=support@yourorg.com

ALLOWED_ORIGINS=*
⚠️ Never commit .env to GitHub.

6️⃣ Create Database
Login to MySQL and run:
CREATE DATABASE chat_db;
Database tables are created automatically when the app starts.

7️⃣ Start the Backend Server
python -m uvicorn app.main:app --reload
Backend will be available at:
http://127.0.0.1:8000

📘 API Documentation (Swagger)
Open in your browser:
http://127.0.0.1:8000/docs

Use Swagger to:
Test APIs
Inspect request/response formats
Debug frontend integration

🧪 Testing Without Frontend
You can test the API without any frontend using:
python tests/test_contact_flow.py
Or directly through Swagger UI.






