from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.models import db, Donation
from functools import wraps

donor_bp = Blueprint('donor', __name__, url_prefix='/donor')


def donor_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.role != 'donor':
            flash('Access denied.', 'danger')
            return redirect(url_for('auth.dashboard_redirect'))
        return f(*args, **kwargs)
    return decorated_function


@donor_bp.route('/dashboard')
@login_required
@donor_required
def dashboard():
    donations = Donation.query.filter_by(donor_id=current_user.id)\
                              .order_by(Donation.created_at.desc()).all()
    return render_template('donor/dashboard.html', donations=donations)


@donor_bp.route('/new', methods=['GET', 'POST'])
@login_required
@donor_required
def new_donation():
    if request.method == 'POST':
        food_name = request.form.get('food_name', '').strip()
        quantity  = request.form.get('quantity', '').strip()
        location  = request.form.get('location', '').strip()

        if not food_name or not quantity or not location:
            flash('All fields are required.', 'danger')
            return redirect(url_for('donor.new_donation'))

        donation = Donation(
            food_name=food_name,
            quantity=quantity,
            location=location,
            donor_id=current_user.id,
            status='pending'
        )
        db.session.add(donation)
        db.session.commit()

        flash('Donation submitted successfully!', 'success')
        return redirect(url_for('donor.dashboard'))

    return render_template('donor/new_donation.html')
