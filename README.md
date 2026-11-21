# Keerthana J — Personal Portfolio

A responsive blue-themed personal portfolio made with Django, SQLite, HTML, CSS, JavaScript, and Bootstrap 5. It includes animated navigation and reveal effects, education, skill and soft-skill cards, project detail pages, a certificate section, downloadable resume, and a contact form that stores messages in SQLite.


## Quick start (Windows)

1. Extract the ZIP file.
2. Open the extracted `portfolio_project` folder in VS Code.
3. Open the VS Code terminal (`Terminal > New Terminal`).
4. Create a virtual environment:

   ```bat
   py -m venv .venv
   ```
5. Activate it:

   ```bat
   .venv\Scripts\activate
   ```
   ### Configure environment variables

Create a `.env` file in the project root (the same folder as `manage.py`).

Generate a new Django secret key using:

```powershell
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Add the following settings to `.env`:

```env
DJANGO_SECRET_KEY=your_generated_secret_key
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost
```

Replace `your_generated_secret_key` with your generated key.

Never upload the `.env` file to GitHub.
6. Install dependencies:

   ```bat
   pip install -r requirements.txt
   ```
7. Apply database migrations:

   ```bat
   py manage.py migrate
   ```
8. Create an admin account:

   ```bat
   py manage.py createsuperuser
   ```
   Follow the prompts to set the username and password.
9. Start the local server:

   ```bat
   py manage.py runserver
   ```
10. Open the portfolio: **http://127.0.0.1:8000/**. Admin: **http://127.0.0.1:8000/admin/**.

## Contact form

The form validates fields on the server, includes CSRF protection, and saves messages to the SQLite database. Email is optional. To review messages, sign into Django Admin and open Contact messages.


## Included assets

- `static/images/profile.jpg` — supplied profile photo
- `static/documents/python_essentials_1.pdf` — supplied original certificate copy for direct preview/download
- `media/certificates/python_essentials_1.pdf` — original certificate asset retained in media
- `static/documents/keerthana_resume.pdf` — generated one-page resume; update placeholders/contact details if needed


## Notes

- This project is intended for local development. Before deployment, set `DEBUG = False`, use a secure secret key, configure allowed hosts, and follow Django deployment security guidance.
- Bootstrap and Font Awesome are loaded from CDNs, so their icons/framework styling require an internet connection when viewing the site.
- Skill tiles intentionally do not show proficiency percentages because exact proficiency levels were not provided.
- Project descriptions and technologies are kept to the supplied details.
