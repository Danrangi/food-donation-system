from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_required, current_user
from app.models import db, Donation, User, RecipientOrg
from functools import wraps

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')


def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.role != 'admin':
            flash('Access denied.', 'danger')
            return redirect(url_for('auth.dashboard_redirect'))
        return f(*args, **kwargs)
    return decorated_function


@admin_bp.route('/dashboard')
@login_required
@admin_required
def dashboard():
    pending_count = Donation.query.filter_by(status='pending').count()
    assigned_count = Donation.query.filter_by(status='assigned').count()
    completed_count = Donation.query.filter_by(status='completed').count()
    return render_template('admin/dashboard.html',
                           pending_count=pending_count,
                           assigned_count=assigned_count,
                           completed_count=completed_count)


@admin_bp.route('/pool')
@login_required
@admin_required
def pool():
    donations        = Donation.query.filter_by(status='pending')\
                                     .order_by(Donation.created_at.desc()).all()
    delivery_persons = User.query.filter_by(role='delivery').all()
    recipient_orgs   = RecipientOrg.query.all()

    # Filter only available delivery persons (no active assigned task)
    available_delivery = [
        d for d in delivery_persons
        if d.deliveries_assigned.filter_by(status='assigned').count() == 0
    ]

    return render_template('admin/pool.html',
                           donations=donations,
                           delivery_persons=available_delivery,
                           recipient_orgs=recipient_orgs)


@admin_bp.route('/assign/<int:donation_id>', methods=['POST'])
@login_required
@admin_required
def assign(donation_id):
    donation            = Donation.query.get_or_404(donation_id)
    delivery_person_id  = request.form.get('delivery_person_id')
    recipient_org_id    = request.form.get('recipient_org_id')

    if not delivery_person_id or not recipient_org_id:
        flash('Please select both a delivery person and a recipient organisation.', 'danger')
        return redirect(url_for('admin.pool'))

    donation.delivery_person_id = int(delivery_person_id)
    donation.recipient_org_id   = int(recipient_org_id)
    donation.status             = 'assigned'
    db.session.commit()

    flash('Donation assigned successfully!', 'success')
    return redirect(url_for('admin.pool'))


@admin_bp.route('/all')
@login_required
@admin_required
def all_donations():
    donations = Donation.query.order_by(Donation.created_at.desc()).all()
    return render_template('admin/all_donations.html', donations=donations)


@admin_bp.route('/api/pending-count')
@login_required
@admin_required
def pending_count():
    count = Donation.query.filter_by(status='pending').count()
    return jsonify({'count': count})
