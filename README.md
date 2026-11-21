# Keerthana J — Personal Portfolio Website

## CODTECH Internship Details

- **Intern ID:** CIS72
- **Intern Name:** Keerthana J
- **Internship Duration:** 4 Weeks
- **Project Name:** Personal Portfolio Website
- **Project Type:** Web Development
- **Framework:** Django

## Project Description

A responsive blue-themed personal portfolio website developed using Django, SQLite, HTML, CSS, JavaScript, and Bootstrap 5.

The website showcases personal information, education, technical skills, soft skills, projects, certificates, and resume. It includes animated navigation, scroll-reveal effects, individual project detail pages, and a contact form that stores messages in an SQLite database.

## Technologies Used

- Python
- Django
- SQLite
- HTML5
- CSS3
- JavaScript
- Bootstrap 5
- Font Awesome

## Key Features

- Responsive blue-themed portfolio design.
- Animated navigation and reveal effects.
- Personal introduction and profile section.
- Education details.
- Technical skills and soft-skill cards.
- Project showcase with individual project detail pages.
- Certificate section.
- Downloadable resume.
- Contact form with server-side validation.
- CSRF protection.
- Contact messages stored in SQLite.
- Django Admin integration for managing contact messages.

## Project Structure

```text
portfolio_project/
│
├── portfolio/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── portfolio_project/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   ├── images/
│   │   ├── profile.jpg
│   │   └── python_certificate_preview.png
│   └── documents/
│       ├── keerthana_resume_redesigned.pdf
│       └── python_essentials_1.pdf
│
├── templates/
│   ├── base.html
│   └── portfolio/
│       ├── index.html
│       └── project_detail.html
│
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
```

## Installation and Setup (Windows)

### 1. Clone the repository

```bash
git clone https://github.com/keerthana3467/keerthana-personal-portfolio.git
```

### 2. Open the project folder

```bash
cd keerthana-personal-portfolio
```

Open the folder in VS Code.

### 3. Create a virtual environment

```bash
py -m venv .venv
```

### 4. Activate the virtual environment

```bash
.venv\Scripts\activate
```

### 5. Configure environment variables

Create a `.env` file in the project root (the same folder as `manage.py`).

Generate a Django secret key:

```powershell
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Add the following settings to `.env`:

```env
DJANGO_SECRET_KEY=your_generated_secret_key
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost
```

Replace the placeholder with your generated secret key.

**Important:** Never upload `.env` to GitHub.

### 6. Install dependencies

```bash
pip install -r requirements.txt
```

### 7. Apply database migrations

```bash
py manage.py migrate
```

### 8. Create an admin account-optional

```bash
py manage.py createsuperuser
```

Follow the prompts to create your administrator account.

### 9. Start the development server

```bash
py manage.py runserver
```

### 10. Open the website

Portfolio: http://127.0.0.1:8000/

Django Admin: http://127.0.0.1:8000/admin/

## Contact Form

The contact form validates submitted fields on the server, includes CSRF protection, and stores messages in the SQLite database.

Administrators can review submitted messages through Django Admin under Contact Messages.

## Included Assets

- `static/images/profile.jpg` — Profile photo.
- `static/images/python_certificate_preview.png` — Certificate preview image.
- `static/documents/python_essentials_1.pdf` — Python Essentials 1 certificate.
- `static/documents/keerthana_resume_redesigned.pdf` — Downloadable resume.

## Testing

The project was checked using Django's system check and automated tests.

**Test results:**
- Django system check: Passed.
- Automated tests: 5 passed.
- Test failures: 0.

## Security and Deployment Notes

- The project is configured for local development.
- Before production deployment, set `DEBUG=False`.
- Use a secure secret key.
- Configure allowed hosts appropriately.
- Never expose environment variables or credentials.
- Follow Django deployment security recommendations.

Bootstrap and Font Awesome are loaded through CDNs, so an internet connection is required for their external styling and icons.



