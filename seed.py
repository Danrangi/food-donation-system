from app import create_app
from app.models import db, User, RecipientOrg

app = create_app()

with app.app_context():
    # --- Admin User ---
    if not User.query.filter_by(email='admin@fooddonation.com').first():
        admin = User(
            username='admin',
            email='admin@fooddonation.com',
            role='admin'
        )
        admin.set_password('admin1234')
        db.session.add(admin)
        print('Admin user created.')
    else:
        print('Admin user already exists.')

    # --- Recipient Organisations ---
    orgs = [
        {
            'name': 'Hope Foundation',
            'address': '12 Unity Road, Abuja',
            'contact': '0801*********'
        },
        {
            'name': 'Feed the Nation NGO',
            'address': '5 Garki District, Abuja',
            'contact': '0808*********'
        },
        {
            'name': 'Mercy Shelter',
            'address': '33 Wuse Zone 4, Abuja',
            'contact': '0701*********'
        },
        {
            'name': 'City Care Initiative',
            'address': '9 Maitama Close, Abuja',
            'contact': '0905*********'
        },
    ]

    for org_data in orgs:
        if not RecipientOrg.query.filter_by(name=org_data['name']).first():
            org = RecipientOrg(**org_data)
            db.session.add(org)
            print(f"Recipient org '{org_data['name']}' created.")
        else:
            print(f"Recipient org '{org_data['name']}' already exists.")

    db.session.commit()
    print('Seeding complete.')
