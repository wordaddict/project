# project

# Homeless Shelter Management Application (TEAM 4)

## 📋 Project Overview
This is a prototype application developed for a local community shelter. It helps track homeless individuals seeking assistance and provides services such as:

- Shelter
- Food
- Medical help
- Rehabilitation programs
- Volunteer management and shift tracking

---

## 🏗️ Features & Functional Modules

### ✅ Core Backend Components
- **SQLite Database** to persist data locally.
- **FastAPI**-based backend to serve and manage data operations.

### ✅ API Functionalities
- **User Management**
  - Register different users by role: staff, domain users, or front-desk reps.
- **Data Input**
  - Log services provided to individuals.
  - Record food/aid donations.
  - Register volunteer shifts.
- **Data Display**
  - Retrieve records relevant to an authenticated user.

---

## 👥 Stakeholder Roles
The system supports three user types:

1. **Front Desk Representatives**
   - Record incoming individuals and basic information.
2. **Domain Users**
   - Beneficiaries like elderly, volunteers, and donors.
3. **Employees / Staff (including CEO)**
   - View and manage operations at a higher level.

---

## 🚀 Getting Started

### 📦 Installation
```bash
git clone https://github.com/yourname/group4project.git
cd group4project
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Running the app
uvicorn backend.main:app --reload

## 🔒 Authentication
Login functionality is expected to be added separately via the Access Control Component.

## 📚 Notes
This is a lightweight research-focused prototype. Not intended for production use or multi-user concurrency with SQLite.

## Live URL:  https://project-group-4.onrender.com/

## Postman link: https://.postman.co/workspace/My-Workspace~62b2f8a5-e1a4-40e8-80d7-9aa208e44dad/collection/2558201-0873ed91-36dd-4a40-8d5e-fdba16734859?action=share&creator=2558201