from flask import Flask
from flask_login import LoginManager
from app.models import db, User
from config import Config

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message_category = 'info'

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Register blueprints
    from app.auth.routes import auth_bp
    from app.donor.routes import donor_bp
    from app.admin.routes import admin_bp
    from app.delivery.routes import delivery_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(donor_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(delivery_bp)

    # Create tables
    with app.app_context():
        db.create_all()

    return app
