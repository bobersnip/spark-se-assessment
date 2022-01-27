web: gunicorn --chdir project/server __init__:app
heroku ps:scale web=1
release: python project/server/manage.py db upgrade

