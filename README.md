# Naveen Travels — basic Django authentication

Simple email/password registration, login, and logout with SQLite and basic HTML/CSS templates. The landing page is public; the welcome page at `/home/` requires login. No travel booking features are included yet.

## Run

```bash
cd /Applications/XAMPP/xamppfiles/htdocs/github/7-python/3-learn-agent-skill/2-minipro/snit-mini-projects/naveen_travelsite
source /Applications/XAMPP/xamppfiles/htdocs/github/7-python/venv/bin/activate
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/ for the landing page, then click Login or Register.

## How it works

- `accounts/views.py`: plain function views for registration, login, home, and logout.
- `accounts/urls.py`: page addresses.
- `accounts/templates/accounts/`: basic templates sharing `base.html`.
- Django's built-in User model stores the normalized email as the username, so no custom model or login backend is needed.
- `create_user()` hashes passwords; `authenticate()` checks them and `login()` starts a session.
- Registration requires matching passwords of at least 8 characters. Forms include CSRF protection.

This is a local learning project. Generated development settings use DEBUG and a development secret key.
