# MySchoolHub - MealsHub Module


# 🏫 Overview



MySchoolHub is a modular digital platform designed to support key areas of school life through simple, accessible tools.
This project focuses on the first core module: MealsHub, a student‑driven meal‑ordering system that helps schools manage daily meal selections more efficiently.

MealsHub allows students to log in and choose their meals for the week, while kitchen staff receive accurate daily totals broken down by meal type and dietary requirements. This reduces manual counting, minimises food waste, and supports smoother kitchen planning. The system is designed to be clear, user‑friendly, and appropriate for a school environment.

Although this project focuses on the MealsHub module, MySchoolHub is intentionally designed to be scalable. Future modules may include attendance tracking, communication tools, and a safeguarding system similar to CPOMS (SafeGuardHub). This modular approach ensures the platform can grow over time while keeping each section focused and manageable.

---

# 🎯 Project Rationale
Many schools still rely on manual processes for collecting meal choices, which can lead to errors, delays, and unnecessary food waste. Since meals are currently free and students select their own meals, MealsHub provides a simple digital solution that:

Gives students an easy way to choose meals

Provides kitchen staff with clear, accurate totals

Reduces administrative workload

Supports dietary needs and menu planning

MealsHub forms the foundation of the wider MySchoolHub ecosystem, demonstrating how digital tools can streamline everyday school operations.

---


# 🧩 Features

**Student Features**

- View weekly menu
- Select meals for each day
- Change or cancel selections
- View dietary information
- Kitchen Staff Features
- View daily meal totals
- Breakdown by meal type (vegetarian, vegan, halal, gluten‑free)
- Dietary alerts
- Optional print/export summary

**Admin Features**

- Add/edit meals
- Set availability dates
- Manage dietary tags

---

# 🗂️ Database Structure

**users**

- id
- name
- email
- password
- role (student, kitchen, admin)


**meals**

- id
- name
- description
- dietary_type
- date_available

**orders**

- id
- user_id
- meal_id
- date
- created_at

---

# 🖥️ User Interface Mockups


**Student Dashboard**


Monday

• Chicken Pasta        [ Select Meal ] 

• Veggie Wrap (V)      [ Select Meal ]

• Jacket Potato (GF)   [ Select Meal ]


**Kitchen Dashboard**

Total Meals Today: 142

Roast Chicken .......... 68

Quorn Roast (V) ........ 41

Tomato Pasta (V) ....... 33

---

# 🌱 Future Enhancements

**Parent Ordering**

Parents will be able to log in, view menus, and select meals for their children.

**SafeGuardHub (CPOMS‑Style Module)**

A secure safeguarding and behaviour logging system for authorised staff only.

Features may include:

- Logging concerns
- Recording disclosures
- Tracking follow‑up actions
- Behaviour incident history

**AttendanceHub**

Digital registers and absence tracking.

**CommsHub**

Messaging, announcements, and parent communication.

**UniformHub**

School shop for uniform orders.

---

# 🛠️ Technologies Used

- **Python** - core programming language
- **Django** - web framework for models, views, admin, and routing
- **HTML/CSS** - fromt-end structure and styling
- **SQLite** - default development database
- **Virtual environment (.venv)** - dependency isolation

---

## 🧱 Tech Stack Diagram 

```mermaid
flowchart TD

    subgraph UserSide[User Interface]
        Student[Student\nSelects Meals]
        Kitchen[Kitchen Staff\nViews Totals]
        Admin[Admin\nManages Meals]
    end

    subgraph DatabaseLayer[Database]
        SQLite[(SQLite Database<br>db.sqlite3)]
    end

    Student --> Views
    Kitchen --> Views
    Admin --> AdminPanel

    Views --> Templates
    Views --> Models
    AdminPanel --> Models

    Models --> SQLite

```
---



# 📦 Setup & Installation

### 1. Create and activate a virtual enviroment

**Navigate to the project folder**

```
cd C:\Users\mosso\Documents\my_school_hub
```

**Create a virtual enviroment (only needed the first time)**

```
python -m venv venv
```

**Activate it**

```
venv\Scripts\activate
```

(You should now see (venv) at the start of your terminal prompt.)

### 2. Install project dependencies

**Once the virtual environment is active, install required packages;**

```
pip install -r requirements.txt
```

### 3. Run the application

**Start the Django development server:**

```
python manage.py runserver
```

**You should see:**

```
Starting development server at http://127.0.0.1:8000/
```

### 4. Open the local server in your browser 

**Visit:**

```
http://127.0.0.1:8000/
```

**Or go straight to the weekly menu:**

```
http://127.0.0.1:8000/menu/1/
```

### Quick Daily Workflow ###

```
cd C:\Users\mosso\Documents\my_school_hub
venv\Scripts\activate
python manage.py runserver
```

---

# 🧪 Testing
Testing will include:

Form validation

CRUD operations

Role‑based access

Meal selection logic

Totals calculation

Error handling

A full testing table can be added later.



👤 Author
Alison Mossop  
MySchoolHub — MealsHub Module