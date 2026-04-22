# Personal Website

Portfolio site built with Django. Displays projects, skills, education, experience, and a contact form. Supports English and Dutch with automatic browser language detection.

## Stack

- **Backend** — Django 5.2
- **Frontend** — Server-rendered templates, vanilla JS, custom CSS
- **Database** — SQLite (local) / PostgreSQL (production)
- **Static files** — WhiteNoise
- **Deployment** — Railway

## Local setup

```bash
git clone https://github.com/Bernd-Slagter/personal-website-2026.git
cd personal-website-2026
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000.

## Admin panel

Create a superuser to manage content (projects, skills, education, etc.):

```bash
python manage.py createsuperuser
```

Then visit http://127.0.0.1:8000/admin.

## Environment variables

| Variable | Required | Description |
|---|---|---|
| `SECRET_KEY` | Production | Django secret key |
| `DEBUG` | No | Set to `False` in production (default `True`) |
| `RAILWAY_PUBLIC_DOMAIN` | Railway | Set automatically by Railway |
| `ALLOWED_HOSTS` | No | Comma-separated extra allowed hosts |
| `DATABASE_URL` | Production | PostgreSQL connection string |

## Deployment (Railway)

Push to `main`. Railway runs the build and start commands defined in `railway.json` automatically:

- **Build** — `pip install -r requirements.txt && python manage.py collectstatic --noinput`
- **Start** — `python manage.py migrate --noinput && gunicorn portfolio.wsgi`

To create an admin user on the live deployment, set these env vars temporarily in the Railway dashboard and run `python manage.py createsuperuser --noinput` via the Railway shell:

```
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=you@example.com
DJANGO_SUPERUSER_PASSWORD=yourpassword
```

## i18n

The site supports English (`en`) and Dutch (`nl`). Language is auto-detected from the browser's `Accept-Language` header and can be switched via the selector in the footer.

Translation strings live in `locale/nl/LC_MESSAGES/django.po`. After editing, recompile with:

```bash
python manage.py compilemessages
```
