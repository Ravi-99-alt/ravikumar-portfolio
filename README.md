# Ravikumar Locharla — Personal Portfolio

A full-stack personal portfolio built with Flask, SQLAlchemy, MySQL, HTML, CSS and JavaScript.

## Features
- Responsive portfolio homepage
- About, education, technical skills, projects and contact sections
- Project cards loaded dynamically from the MySQL `projects` table
- Skills loaded dynamically from the MySQL `skills` table
- Flask health endpoint: `/api/health`
- MySQL connection check: `/api/db-check`

## Technology
- Frontend: HTML5, CSS3, JavaScript
- Backend: Python 3.12+, Flask
- ORM: Flask-SQLAlchemy
- Database: MySQL
- Driver: PyMySQL

## Project structure
```text
Ravikumar_Portfolio/
├── app.py
├── config.py
├── database.sql
├── requirements.txt
├── .env.example
├── .gitignore
├── models/
│   ├── __init__.py
│   ├── project.py
│   ├── skill.py
│   └── message.py
├── templates/
│   └── index.html
└── static/
    ├── css/style.css
    ├── js/script.js
    └── images/profile.jpg
```

## Setup locally (Windows PowerShell)

1. Install Python 3.12+ and MySQL.
2. Create the database and tables by running `database.sql` in MySQL Workbench.
3. Create and activate a virtual environment:

   ```powershell
   py -3.12 -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

4. Install dependencies:

   ```powershell
   python -m pip install -r requirements.txt
   ```

5. Create your local `.env` file from the example:

   ```powershell
   Copy-Item .env.example .env
   ```

6. Edit `.env` with your own local MySQL credentials and a private random `SECRET_KEY`. Never commit `.env`.
7. Start the app:

   ```powershell
   python app.py
   ```

8. Open `http://127.0.0.1:5000`.

## Database content
The `projects` table stores project title, description, technologies, image filename, GitHub URL and live URL. The `skills` table stores skill names, categories and self-assessed proficiency. The `contact_messages` table is included for future contact-form functionality.

Add project screenshots under `static/images/` and store only the image filename in `projects.image`. Project cards are rendered from database records; they are not hardcoded in the template.

## Deployment status
This repository is prepared for deployment, but deployment is **not completed by this source package**. Before publishing:
- Configure a production MySQL database.
- Set `SECRET_KEY` and database environment variables in the hosting provider's dashboard.
- Use a production WSGI server (for example, Gunicorn on a Linux host).
- Set `debug=False` in production.
- Configure the hosting provider's start command and verify the deployed `/api/health` and `/api/db-check` endpoints.

The profile photo is included in `static/images/profile.jpg`. Ensure you have the right to publish this image.
