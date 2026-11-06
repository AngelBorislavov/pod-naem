# Pod naem

Django application for managing rental records.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

For production, set `DJANGO_SECRET_KEY` to a secure, private value. The
development fallback in `config/settings.py` is not suitable for production.
