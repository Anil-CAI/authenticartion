# 🔐 User Authentication Form - Flask Project 🚀

![Authentication](https://media.giphy.com/media/3o6Zt8cHq2W9lttqek/giphy.gif)

## Overview 🎯
This project implements a **User Authentication System** using **Flask** as the backend framework and **SQLite** as the database. It features user **registration** and **login** with **password hashing** for security. This system uses a single-page form for both user registration and login, providing a streamlined experience.

## Features ✨
- ✅ **User Registration**: Allows new users to sign up with their name, email, and password.
- ✅ **User Login**: Existing users can log in by providing their email and password.
- 🔒 **Password Security**: Passwords are hashed and securely stored in the database using **Werkzeug**.
- 🌐 **Flask Backend**: A lightweight backend built with Flask to handle the routing and form submission.
- 🧑‍💻 **SQLite Database**: A simple SQLite database to store user data.
- 🔁 **Seamless Experience**: Both registration and login are handled from the same form page with easy navigation.

## Tech Stack 🛠️
- **Backend**: Flask (Python)
- **Database**: SQLite
- **Password Hashing**: Werkzeug (Python library)
- **Frontend**: HTML, CSS (Embedded in Python)

## 🚀 Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/YourUsername/user-authentication-flask.git
cd user-authentication-flask
```
2️⃣ Install Dependencies
Install the required Python libraries using pip:
```
pip install flask werkzeug
```
3️⃣ Run the Flask Application 🏃‍♂️
To run the Flask application locally, execute:
```
python app.py
The server will start running at: http://127.0.0.1:5000/
```
4️⃣ Access the Authentication Form 🌐
Open your browser and navigate to http://127.0.0.1:5000/ to access the authentication form.

##💡 How it Works

**Registration Flow:

- The user enters their name, email, and password.

- the password is hashed using Werkzeug's generate_password_hash function to ensure security.

- The system checks if the email is already registered in the database.

- If the email is not found, a new user is added to the database with the hashed password.

- A success message is shown after registration, or an error is shown if the email already exists.

**Login Flow:

- The user enters their email and password.

- The system retrieves the stored password hash for the given email from the database.

- The entered password is verified by comparing it with the stored hash using Werkzeug's check_password_hash.

- If the credentials are correct, the user is redirected to the test page.

- If the login fails, an error message is shown, prompting the user to try again.

🎯 File Structure
```bash
📁 user-authentication-flask
├── 📝 app.py            # Main Flask application with form handling and routes
├── 🌍 templates
│   └── form.html       # HTML code for the user authentication form
└── 📜 README.md         # Project documentation
```
**app.py

The main backend file that contains:

- The routes for registration, login, and test page.

- The logic for password hashing and user verification.

- The embedded HTML form for user interaction.

**form.html

A simple HTML form for both registration and login, embedded within app.py.

**🎯 Example API Endpoint
- POST /submit: This endpoint handles both the registration and login.

Registration: The user provides name, email, and password.

Login: The user provides email and password to log in.

Request Body (for registration):
```
json
Copy
Edit
{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "mypassword123"
}
```
Response (successful registration):
```
json
Copy
Edit
{
  "message": "Registration successful!"
}
```
Request Body (for login):
```
json
Copy
Edit
{
  "email": "john@example.com",
  "password": "mypassword123"
}
```
Response (successful login):
```
json
Copy
Edit
{
  "message": "Welcome to the test page!"
}
```
📊 Database Schema

The SQLite database (data.db) contains a single table users with the following columns:

- name: The full name of the user (TEXT)

- email: The user's email (TEXT, unique)

- password: The hashed password (TEXT)

🖼️ UI Preview

- Here’s a preview of the user authentication form:

🎯 Future Enhancements
🚀 Add email verification before registration is complete.

🔒 Implement 2FA (Two-Factor Authentication) for additional security.

🌍 Deploy the application on platforms like Heroku or Render.

🌎 Design a more sophisticated front-end interface with Bootstrap or Tailwind CSS.

📜 License
- This project is licensed under the MIT License.

👨‍💻 Developed by [Anil-CAI] 🚀
