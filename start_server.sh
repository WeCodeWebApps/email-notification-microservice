#!/usr/bin/env sh

# inpired from https://github.com/wemake-services/wemake-django-template/blob/master/%7B%7Bcookiecutter.project_name%7D%7D/docker/django/gunicorn.sh

export DJANGO_SETTINGS_MODULE="src.settings"

set -o errexit
set -o nounset

# We are using `gunicorn` for production, see:
# http://docs.gunicorn.org/en/stable/configure.html

# Check that $DJANGO_ENV is set to "production",
# fail otherwise, since it may break things:
# echo "DJANGO_ENV is $DJANGO_ENV"
# if [ "$DJANGO_ENV" != 'production' ]; then
#   echo 'Error: DJANGO_ENV is not set to "production".'
#   echo 'Application will not start.'
#   exit 1
# fi

echo "using $DJANGO_SETTINGS_MODULE"

# Run python specific scripts:
# Running migrations in startup script might not be the best option, see:
# docs/pages/template/production-checklist.rst
python manage.py migrate --noinput
python manage.py collectstatic --noinput
# python /code/manage.py compilemessages  # not using translation for now

# Start gunicorn:
# Docs: http://docs.gunicorn.org/en/stable/settings.html
# Concerning `workers` setting see:
# https://github.com/wemake-services/wemake-django-template/issues/1022
gunicorn src.wsgi \
  --workers=${GUNICORN_WORKERS:-2} `# Sync worker settings` \
  --max-requests=2000 \
  --max-requests-jitter=400 \
  --bind="0.0.0.0:${PORT:-8000}" `# Run Django on 8000 port` \
  --log-file=- \
  --worker-tmp-dir="/dev/shm"