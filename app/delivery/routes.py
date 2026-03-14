from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models import db, Donation
from functools import wraps

delivery_bp = Blueprint('delivery', __name__, url_prefix='/delivery')


def delivery_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.role != 'delivery':
            flash('Access denied.', 'danger')
            return redirect(url_for('auth.dashboard_redirect'))
        return f(*args, **kwargs)
    return decorated_function


@delivery_bp.route('/dashboard')
@login_required
@delivery_required
def dashboard():
    assigned_tasks = Donation.query.filter_by(
        delivery_person_id=current_user.id,
        status='assigned'
    ).order_by(Donation.created_at.desc()).all()

    completed_tasks = Donation.query.filter_by(
        delivery_person_id=current_user.id,
        status='completed'
    ).order_by(Donation.updated_at.desc()).all()

    return render_template('delivery/dashboard.html',
                           assigned_tasks=assigned_tasks,
                           completed_tasks=completed_tasks)


@delivery_bp.route('/complete/<int:donation_id>', methods=['POST'])
@login_required
@delivery_required
def complete(donation_id):
    donation = Donation.query.get_or_404(donation_id)

    if donation.delivery_person_id != current_user.id:
        flash('This task is not assigned to you.', 'danger')
        return redirect(url_for('delivery.dashboard'))

    donation.status = 'completed'
    db.session.commit()

    flash('Task marked as completed!', 'success')
    return redirect(url_for('delivery.dashboard'))
