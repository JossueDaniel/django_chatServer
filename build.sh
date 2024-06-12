#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt

# Convert static asset files
python manage.py collectstatic --no-input --settings=chat_project.settings.prod

# Apply any outstanding database migrations
python manage.py migrate --settings=chat_project.settings.prod