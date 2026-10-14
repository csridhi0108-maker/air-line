"""Production entry point for gunicorn (Render): gunicorn wsgi:app"""
from app import create_app

app = create_app()
