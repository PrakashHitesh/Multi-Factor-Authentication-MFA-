# Multi-Factor Authentication (MFA)

This project implements a Multi-Factor Authentication (MFA) system using Python Django.


## Table of Contents

- [Features](#Features)
- [Technologies Used](#Technologies-used)
- [Installation](#Installation)
- [Usage](#Usage)
- [Endpoints](#Endpoints)
- [Contributing](#Contributing)



## Features

- User Signup
- User Login
- Generate MFA QR Code
- Verify MFA Token
- Secure handling of sensitive data
- Responsive web design for a seamless user experience

## Technologies Used

- Python
- Django
- HTML/CSS
- Bootstrap
- pyotp
- qrcode
- SQLite (default database)

## Installation

1. Create a virtual environment:
   
         python -m venv env

   
2. Activate the virtual environment:

         env\Scripts\activate.bat

3. Install dependencies:

         pip install django
         pip install pyotp
         pip install qrcode


4. Run migrations:

         python manage.py makemigrations
         python manage.py migrate

5. Run the server:

         python manage.py runserver
   

## Usage

  + Navigate to the /signup/ URL to create a new account.
  + After registration, log in at the /login/ URL.
  + Generate your MFA QR code at /generate_mfa/ after logging in.
  + Verify your MFA token at /verify_mfa/.


## Endpoints

  - /signup/: User registration page
  - /login/: User login page
  - /generate_mfa/: Generate MFA QR code
  - /verify_mfa/: Verify MFA token
  - /dashboard/: User dashboard (requires authentication)
  - /logout/: Log out of the application

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any feature requests or bug reports.
