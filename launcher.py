import sys
import os
import time
import threading
import webbrowser

# ── Path fix for PyInstaller bundle ───────────────────────────
if getattr(sys, 'frozen', False):
    base_dir = sys._MEIPASS
    # Store database next to the .exe, not inside the bundle
    db_dir = os.path.dirname(sys.executable)
else:
    base_dir = os.path.abspath(os.path.dirname(__file__))
    db_dir = base_dir

os.environ['APP_BASE_DIR'] = base_dir
os.environ['APP_DB_DIR']   = db_dir

# ── Import app after env vars are set ─────────────────────────
from app import create_app
from app.models import db, User, RecipientOrg

app = create_app()


def seed_if_empty():
    with app.app_context():
        # Admin
        if not User.query.filter_by(email='admin@fooddonation.com').first():
            u = User(username='admin', email='admin@fooddonation.com', role='admin')
            u.set_password('admin1234')
            db.session.add(u)

        # Donor
        if not User.query.filter_by(email='freshbowl@foodbridge.com').first():
            u = User(username='freshbowl', email='freshbowl@foodbridge.com', role='donor')
            u.set_password('donor1234')
            db.session.add(u)

        # Delivery
        if not User.query.filter_by(email='quickride@foodbridge.com').first():
            u = User(username='quickride', email='quickride@foodbridge.com', role='delivery')
            u.set_password('delivery1234')
            db.session.add(u)

        # Recipient Orgs
        orgs = [
            {'name': 'Hope Foundation',     'address': '12 Unity Road, Abuja',       'contact': '08012345678'},
            {'name': 'Feed the Nation NGO', 'address': '5 Garki District, Abuja',    'contact': '08087654321'},
            {'name': 'Mercy Shelter',       'address': '33 Wuse Zone 4, Abuja',      'contact': '07011223344'},
            {'name': 'City Care Initiative','address': '9 Maitama Close, Abuja',     'contact': '09055667788'},
        ]
        for o in orgs:
            if not RecipientOrg.query.filter_by(name=o['name']).first():
                db.session.add(RecipientOrg(**o))

        db.session.commit()


def open_browser():
    time.sleep(2)
    webbrowser.open('http://localhost:5000')


def run_server():
    seed_if_empty()
    app.run(host='0.0.0.0', port=5000, debug=False, use_reloader=False)


if __name__ == '__main__':
    threading.Thread(target=open_browser, daemon=True).start()
    run_server()
