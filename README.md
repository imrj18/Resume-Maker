# Resume Maker

The **Resume Maker** is a web application designed to help users create professional resumes easily. This project is built with **Django** and provides an intuitive interface for users to input their personal details, work experience, education, skills, and more to generate a well-structured resume.

## Features

- **User Authentication**: Sign up and log in to save and manage your resumes.
- **Resume Templates**: Choose from different resume templates to customize your resume.
- **Dynamic Form**: Input personal information, work experience, education, skills, and other sections.
- **PDF Export**: Download your generated resume as a PDF file.
- **Responsive Design**: The application is designed to work well on both desktop and mobile devices.

## Tech Stack

- **Backend**: Django
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite (default in Django, can be replaced with other DBs like PostgreSQL or MySQL)
- **PDF Generation**: ReportLab or a similar library for PDF export
- **Authentication**: Django's built-in authentication system

## Installation

### Prerequisites

Make sure you have **Python** and **pip** installed on your machine.

### Clone the Repository

Clone the project to your local machine:

```bash
git clone https://github.com/imrj18/Resume-Maker.git
cd Resume-Maker
```

### Set up Virtual Environment

Create a virtual environment and activate it:

```bash
python -m venv env
# On Windows
env\Scripts\activate
# On macOS/Linux
source env/bin/activate
```

### Install Dependencies

Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

### Database Setup

Run the following command to set up the database:

```bash
python manage.py migrate
```

### Run the Development Server

Start the development server:

```bash
python manage.py runserver
```

Your application will be accessible at `http://127.0.0.1:8000/`.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug fixes, feel free to fork the repository and create a pull request.
