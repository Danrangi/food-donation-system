from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id              = db.Column(db.Integer, primary_key=True)
    username        = db.Column(db.String(64), unique=True, nullable=False)
    email           = db.Column(db.String(120), unique=True, nullable=False)
    password_hash   = db.Column(db.String(256), nullable=False)
    role            = db.Column(db.String(20), nullable=False)  # donor | admin | delivery
    created_at      = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    donations_made      = db.relationship('Donation', foreign_keys='Donation.donor_id',
                                          backref='donor', lazy='dynamic')
    deliveries_assigned = db.relationship('Donation', foreign_keys='Donation.delivery_person_id',
                                          backref='delivery_person', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username} ({self.role})>'


class RecipientOrg(db.Model):
    __tablename__ = 'recipient_orgs'

    id         = db.Column(db.Integer, primary_key=True)
    name       = db.Column(db.String(128), nullable=False)
    address    = db.Column(db.String(256), nullable=False)
    contact    = db.Column(db.String(64), nullable=True)

    donations  = db.relationship('Donation', backref='recipient_org', lazy='dynamic')

    def __repr__(self):
        return f'<RecipientOrg {self.name}>'


class Donation(db.Model):
    __tablename__ = 'donations'

    id                  = db.Column(db.Integer, primary_key=True)
    food_name           = db.Column(db.String(128), nullable=False)
    quantity            = db.Column(db.String(64), nullable=False)
    location            = db.Column(db.String(256), nullable=False)
    status              = db.Column(db.String(20), default='pending')  # pending | assigned | completed
    created_at          = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at          = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    donor_id            = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    delivery_person_id  = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    recipient_org_id    = db.Column(db.Integer, db.ForeignKey('recipient_orgs.id'), nullable=True)

    def __repr__(self):
        return f'<Donation {self.food_name} [{self.status}]>'
