# Disease Prediction System

A web-based healthcare application that combines disease prediction from symptoms with hospital booking functionality.

## Project Overview

This system is built as a PHP web application with a MySQL backend, plus a Python machine learning component for disease prediction. Users can sign up, log in, browse hospitals, book appointments, and submit symptoms for a predicted illness.

The project includes:
- Public landing page and user authentication
- Hospital listing and booking system
- Symptom-based disease prediction via a Python ML model
- Database setup and auto-creation logic in `db.php`

## Features

- User registration and login
- Hospital display and booking
- View and cancel booked hospitals
- Symptom input and disease prediction
- Contact form storage
- Python-based ML prediction server

## Technology Stack

- PHP
- HTML / CSS / JavaScript
- MySQL / MariaDB
- Python 3
- Flask (prediction API)
- Machine learning models stored as `.pkl` files

## Repository

GitHub: https://github.com/sandeep6386510-ship-it/Disease-Prediction

## Requirements

- Windows / Linux / macOS with a PHP web server
- MySQL or MariaDB
- Python 3
- PHP extensions: `mysqli`, `curl`
- Python packages: `flask`, `numpy`, `joblib`

## Setup Instructions

### 1. Install the web environment

Recommended installers:
- XAMPP: https://www.apachefriends.org/
- WAMP: https://www.wampserver.com/
- Laragon: https://laragon.org/

### 2. Place the project in the web root

For XAMPP:
1. Copy the folder into `C:\xampp\htdocs\Disease-Prediction`
2. Start Apache and MySQL from the XAMPP Control Panel

For WAMP:
1. Copy the folder into `C:\wamp64\www\Disease-Prediction`
2. Start Apache and MySQL services

### 3. Configure the database

The application uses `db.php` to automatically create the database and tables on first access.

Default credentials in `db.php`:
- Host: `localhost`
- User: `root`
- Password: `` (empty)
- Database: `hospitals_db`

### 4. Install Python dependencies

If you want to use the disease prediction feature, install Python 3 and required packages:

```powershell
python -m pip install flask numpy joblib
```

### 5. Start the Flask prediction server

Open a terminal in the project folder and run:

```powershell
python app.py
```

The server listens on `http://127.0.0.1:5000/predict` by default.

> Note: `predict2.php` sends symptom data to this Flask endpoint. The prediction page will not work unless this server is running.

## Run the application

1. Open the browser
2. Visit:
   - `http://localhost/Disease-Prediction/index.php`
3. Use the navigation links to:
   - Sign up (`signup.php`)
   - Log in (`login.php`)
   - Browse hospitals (`homepage.php`)
   - Predict disease (`predict.php`)
   - Book hospital appointments (`bookhospital.php`)
   - View booked hospitals (`bookedhospital.php`)

## How to Use

### Register and log in
1. Open `signup.php`
2. Create a new user account
3. Log in using `login.php`

### Browse hospitals
- After login, open `homepage.php`
- View hospital listings and descriptions
- Click `Book Hospital` to make a reservation

### Book a hospital
- Choose a hospital from the homepage
- Fill in the booking details and submit
- The booking is saved in the database

### Predict disease from symptoms
1. Open `predict.php`
2. Enter up to 5 symptoms from the symptom list
3. Submit the form
4. View the predicted disease on `predict2.php`

## Key Files

- `index.php` — public landing page
- `signup.php` — user registration
- `login.php` — user login
- `homepage.php` — logged-in dashboard with hospitals
- `predict.php` — symptom input page
- `predict2.php` — sends data to Flask and shows result
- `bookhospital.php` — create hospital bookings
- `bookedhospital.php` — view/cancel bookings
- `db.php` — database connection and table creation
- `app.py` — Flask prediction server
- `predict.py` — loads ML model and predicts disease
- `visualization.py` — extra data visualization script

## Database Tables

Created automatically by `db.php`:
- `signup`
- `contact`
- `hospital`
- `bookedhospital`

## Notes and Improvements

- The current app uses plain PHP sessions for authentication
- Passwords are stored as plain text in the database; this should be improved with password hashing
- The Flask URL in `predict2.php` is hard-coded to `http://127.0.0.1:5000/predict`
- If you want to change the prediction server host or port, update `predict2.php`

## GitHub Commit

This project has been initialized and pushed to the repository:

`https://github.com/sandeep6386510-ship-it/Disease-Prediction`

---

If you want, I can also add a shorter `REPORT.md` version or clean up sensitive files before publishing.