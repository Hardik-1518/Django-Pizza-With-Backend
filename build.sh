#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Create persistent database folder and copy initial db if not already present
if [ -d "/data" ] && [ ! -f "/data/db.sqlite3" ]; then
  echo "Initializing persistent SQLite database from repository preloaded data..."
  cp db.sqlite3 /data/db.sqlite3
fi

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput
