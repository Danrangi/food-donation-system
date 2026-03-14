import os

BASE_DIR = os.environ.get('APP_BASE_DIR', os.path.abspath(os.path.dirname(__file__)))
DB_DIR   = os.environ.get('APP_DB_DIR',   os.path.abspath(os.path.dirname(__file__)))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'food-donation-secret-key-2026')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(DB_DIR, 'food_donation.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = True
