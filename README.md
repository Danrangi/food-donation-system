<div align="center">

# 🍱 FoodBridge
### *Connecting Surplus to Purpose*

![Python](https://img.shields.io/badge/Python-3.12-2e7d32?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0.3-2e7d32?style=for-the-badge&logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Local-2e7d32?style=for-the-badge&logo=sqlite&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-43a047?style=for-the-badge)
![Build](https://img.shields.io/badge/Build-Passing-43a047?style=for-the-badge&logo=githubactions&logoColor=white)

<br/>

> **FoodBridge** is a web-based food donation and delivery management system that connects hotels, restaurants, and event halls with people experiencing food insecurity — minimizing waste, maximizing impact.

<br/>

![FoodBridge Banner](https://via.placeholder.com/900x300/2e7d32/ffffff?text=FoodBridge+%7C+Reducing+Food+Waste%2C+One+Delivery+at+a+Time)

</div>

---

## 📌 Table of Contents

- [About the Project](#-about-the-project)
- [System Architecture](#-system-architecture)
- [Features](#-features)
- [User Roles](#-user-roles)
- [Workflow](#-workflow)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Default Credentials](#-default-credentials)
- [Building the Executable](#-building-the-executable)
- [Database Schema](#-database-schema)
- [Screenshots](#-screenshots)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🌍 About the Project

Every day, tonnes of perfectly edible food are discarded by hotels, restaurants, and event halls — while millions go hungry within the same communities.

**FoodBridge** was built to close that gap.

It is a fully offline-capable, LAN-deployable web application that digitizes the entire food donation lifecycle — from a donor submitting surplus food details, to an admin coordinating logistics, to a delivery person completing the drop-off at a registered recipient organization.

> Built as a Final Year Project at **Ibrahim Badamasi Babangida University Lapai (IBBUL)**, this system demonstrates how technology can be applied to solve real humanitarian challenges at the community level.

---

## 🏗 System Architecture

FoodBridge follows a clean **3-Tier N-Layer Architecture**:

```
┌─────────────────────────────────────────────────────┐
│           PRESENTATION LAYER (Frontend)              │
│     HTML · CSS · Vanilla JS · Jinja2 Templates       │
├─────────────────────────────────────────────────────┤
│          BUSINESS LOGIC LAYER (Backend)              │
│         Python · Flask · Flask-Login · WTF           │
│         Binds to 0.0.0.0 for LAN access              │
├─────────────────────────────────────────────────────┤
│           DATA ACCESS LAYER (Database)               │
│         SQLite · SQLAlchemy ORM · Local File         │
└─────────────────────────────────────────────────────┘
```

---

## ✨ Features

| Feature | Description |
|--------|-------------|
| 🔐 Role-Based Authentication | Three distinct roles — Donor, Admin, Delivery — each with protected dashboards |
| 📋 Donation Submission | Donors submit food name, quantity, and pickup location in seconds |
| 🗂 Admin Donation Pool | Admins see all pending donations in a live-updating pool |
| 🚚 Smart Dispatch | Admins assign only *available* delivery persons (no double-booking) |
| 🏢 Recipient Organisation Registry | Seeded list of registered NGOs and shelters for drop-off |
| ✅ Delivery Confirmation | Delivery persons mark tasks complete with a single click |
| 🔔 Live Badge Polling | Admin navbar badge auto-refreshes every 30 seconds — no page reload needed |
| 📊 Stats Dashboard | Admin sees pending, assigned, and completed counts at a glance |
| 💾 Fully Offline | Runs entirely on a local network — no internet required |
| 🖥 One-Click `.exe` | Double-click to launch — opens browser automatically |

---

## 👥 User Roles

### 🟢 Donor
Hotels, restaurants, canteens, and event halls that have surplus food to donate.
- Register and log in
- Submit a new donation (food name, quantity, pickup address)
- Track the status of all past donations

### 🔴 Admin
The system coordinator who manages the full pipeline.
- View all pending donations in the pool
- Assign a delivery person and recipient organisation to each donation
- Monitor all donations across all statuses
- See live stats on the dashboard

### 🔵 Delivery Person
Registered couriers who pick up and transport donations.
- View their currently assigned task with full pickup and drop-off details
- Mark a delivery as completed once done
- View their full delivery history

---

## 🔄 Workflow

```
  DONOR                    ADMIN                  DELIVERY PERSON
    │                        │                          │
    │  Submits donation       │                          │
    │ ──────────────────────► │                          │
    │                        │  Reviews pending pool     │
    │                        │  Selects delivery person  │
    │                        │  Selects recipient org    │
    │                        │ ────────────────────────► │
    │                        │                          │  Picks up food
    │                        │                          │  Delivers to org
    │                        │                          │  Marks complete
    │                        │ ◄──────────────────────  │
    │                        │                          │
```

**Status Flow:**
```
[PENDING] ──► [ASSIGNED] ──► [COMPLETED]
```

---

## 🛠 Tech Stack

| Layer | Technology |
|-------|-----------|
| Language | Python 3.12 |
| Web Framework | Flask 3.0.3 |
| Authentication | Flask-Login 0.6.3 |
| ORM | Flask-SQLAlchemy 3.1.1 |
| Forms & CSRF | Flask-WTF 1.2.1 |
| Database | SQLite (via SQLAlchemy) |
| Templating | Jinja2 (built into Flask) |
| Frontend | HTML5, CSS3, Vanilla JavaScript |
| Packaging | PyInstaller 6.x |
| CI/CD | GitHub Actions |

---

## 📁 Project Structure

```
food-donation-system/
│
├── app/
│   ├── __init__.py              # App factory & blueprint registration
│   ├── models.py                # SQLAlchemy models: User, Donation, RecipientOrg
│   │
│   ├── auth/
│   │   └── routes.py            # Login, Register, Logout, Role redirect
│   ├── donor/
│   │   └── routes.py            # Donor dashboard, new donation form
│   ├── admin/
│   │   └── routes.py            # Donation pool, assign, all donations, polling API
│   ├── delivery/
│   │   └── routes.py            # My tasks, mark complete
│   │
│   ├── static/
│   │   ├── css/main.css         # Green & white theme, full design system
│   │   └── js/poll.js           # Admin badge auto-polling (30s interval)
│   │
│   └── templates/
│       ├── base.html            # Shared layout, navbar, flash messages, footer
│       ├── auth/                # login.html, register.html
│       ├── donor/               # dashboard.html, new_donation.html
│       ├── admin/               # dashboard.html, pool.html, all_donations.html
│       └── delivery/            # dashboard.html
│
├── .github/
│   └── workflows/
│       └── build.yml            # GitHub Actions → builds FoodBridge.exe on Windows
│
├── config.py                    # App config, secret key, DB URI
├── run.py                       # Dev server entry point (0.0.0.0:5000)
├── launcher.py                  # Production launcher: starts server + opens browser
├── FoodBridge.spec              # PyInstaller build specification
├── seed.py                      # Seeds admin user + recipient organisations
├── requirements.txt             # Python dependencies
├── build.bat                    # One-click Windows build script
├── build.sh                     # One-click Mac/Linux build script
└── .gitignore
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- pip

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/food-donation-system.git
cd food-donation-system
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Seed the database

```bash
python seed.py
```

### 4. Run the development server

```bash
python run.py
```

### 5. Open in browser

```
http://localhost:5000
```

> To access from another device on the same network, use your machine's local IP address:
> `http://192.168.x.x:5000`

---

## 🔑 Default Credentials

| Role | Username | Email | Password |
|------|----------|-------|----------|
| 👤 Admin | `admin` | admin@fooddonation.com | `admin1234` |
| 🍽 Donor | `freshbowl` | freshbowl@foodbridge.com | `donor1234` |
| 🚚 Delivery | `quickride` | quickride@foodbridge.com | `delivery1234` |

> ⚠️ These credentials are seeded automatically on first launch. Change them before any public deployment.

---

## 📦 Building the Executable

FoodBridge can be packaged into a standalone `.exe` for Windows — no Python installation needed on the presentation machine.

### Option A — GitHub Actions (Recommended)

Every push to `main` automatically triggers a Windows build via GitHub Actions.

1. Push your code to GitHub
2. Go to the **Actions** tab on your repository
3. Wait for the **Build FoodBridge Windows Executable** workflow to complete ✅
4. Download **FoodBridge-Windows** from the **Artifacts** section

### Option B — Build Locally on Windows

```bat
build.bat
```

The `.exe` will be output to `dist/FoodBridge.exe`.

### How it works

```
Double-click FoodBridge.exe
        ↓
Flask server starts silently in background
        ↓
App waits until server is ready
        ↓
Default browser opens at http://localhost:5000
        ↓
Login page — ready to demo
```

---

## 🗄 Database Schema

```
┌──────────────────┐       ┌──────────────────────┐       ┌──────────────────┐
│      users       │       │      donations        │       │  recipient_orgs  │
├──────────────────┤       ├──────────────────────┤       ├──────────────────┤
│ id (PK)          │──┐    │ id (PK)               │  ┌──► │ id (PK)          │
│ username         │  │    │ food_name             │  │    │ name             │
│ email            │  ├──► │ quantity              │  │    │ address          │
│ password_hash    │  │    │ location              │  │    │ contact          │
│ role             │  │    │ status                │  │    └──────────────────┘
│ created_at       │  │    │ created_at            │  │
└──────────────────┘  │    │ updated_at            │  │
                      │    │ donor_id (FK) ─────────┘  │
                      └──► │ delivery_person_id (FK)    │
                           │ recipient_org_id (FK) ─────┘
                           └──────────────────────┘
```

---

## 🤝 Contributing

Contributions are welcome! Here's how:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

<div align="center">

Built with ❤️ at **Ibrahim Badamasi Babangida University Lapai**

*Reducing food waste, one delivery at a time.*

</div>
