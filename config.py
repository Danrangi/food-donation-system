import os

base_dir = os.environ.get('FOODBRIDGE_DB_DIR', os.path.abspath(os.path.dirname(__file__)))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'foodbridge-secret-key-2024')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir, 'food_donation.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
