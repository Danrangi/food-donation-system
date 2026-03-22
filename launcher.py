import sys
import os
import threading
import webbrowser
import time
import signal

if getattr(sys, 'frozen', False):
    base_dir = sys._MEIPASS
    db_dir = os.path.dirname(sys.executable)
else:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_dir = base_dir

os.environ['FOODBRIDGE_DB_DIR'] = db_dir
os.environ['FOODBRIDGE_BASE_DIR'] = base_dir

db_path = os.path.join(db_dir, 'food_donation.db')
if not os.path.exists(db_path):
    import importlib.util
    seed_path = os.path.join(base_dir, 'seed.py')
    spec = importlib.util.spec_from_file_location("seed", seed_path)
    seed_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(seed_module)

def open_browser():
    time.sleep(2)
    webbrowser.open('http://localhost:5000/auth/login')

threading.Thread(target=open_browser, daemon=True).start()

from app import create_app
from flask import redirect, url_for

app = create_app()

@app.route('/')
def index():
    return redirect(url_for('auth.login'))

app.run(host='0.0.0.0', port=5000, debug=False, use_reloader=False)
