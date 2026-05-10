# MySchoolHub - MealsHub Module


# 🏫 Overview



MySchoolHub is the first modular of the **MySchoolHub** platform - a simple, school-friendly system that allows students (or parents) to select meals for the school week.  
It replaces manual paper-based meal choices with a clean digital workflow that reduces admin time, improves accuracy, and helps kitchen staff plan more efficiently.

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


# 🧩 Current Features

**Student Features**

- View weekly menu (Mon-Fri)
- Select **one meal per day**
- Submit all choices in one form
- "No Meal" option for each day
- Mobile-friendly layout

**Kitchen Staff Features**

- View **all order**
- View **daily totals**
- See meal names, classes, and week numbers

**Admin Features**

- Add/edit/delete meals
- Set meal day + week
- View all orders in admin

---

# 🗂️ Database Structure

## 🗂️ Database Structure (ERD)

```mermaid
flowchart TD

    subgraph MealsHubDB[MealsHub Database]
        Users[[
            Users
            ---
            id
            name
            email
            password
            role
        ]]

        Meals[[
            Meals
            ---
            id
            name
            description
            dietary_type
            day_available
            week_available
        ]]

        Orders[[
            Orders
            ---
            id
            user_id (FK)
            meal_id (FK)
            date
            created_at
        ]]
    end

    Users --> Orders
    Meals --> Orders
```


---

# 🖥️ Interface Preview (Current Bahaviour)

 **Weekly Menu Page**
- Days grouped Mon-Fri
- Each day shows avaiable meals
- One checkbox per meal
- "No Meal" option included
- Student name field at the top
- One "Submit Weekly Order" button

**Order Success Page**

- Simple confirmation screen


---

# 🌱 Planned Enhancements

**Short-Term**

- Two column mobile layout for meal options
- Order summary before submission
- Kitchen dashboard with totals

**Long-Term**
- Parent login system
- Student accounts
- SafeGauardHub (CPOMS-style module)
- AttendanceHub
- CommsHub
- UniformHub

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
# 📦 Deployment

### Local Deployment

1. Clone the repository
2. Create and activate a virtual enviorment
3. Install dependencies
4. Run migrations
5. Start the developement server

### Heroku Deployment

- App deployed using Herku
- Uses Gunicorn + Whitenoise
- Static files collected using ```collectstatic```
- Enviroment variables set in Heroku dashboard
- App accessible via live URL
---

# 🧪 Testing
| Feature | Test | Expected Result | Actual Result | Pass |
| --- | --- | --- | --- | --- |
| Weekly order form | Submit 5 meals (Mon–Fri) | All 5 orders saved | Works correctly | ✔ |
| Weekly order form | Select “No Meal” | Order saved with correct meal | Works correctly | ✔ |
| Day filter | Select Monday | Only Monday orders shown | Works correctly | ✔ |
| Day filter | Clear filter | All orders shown | Works correctly | ✔ |
| Daily totals | Filter by day | Totals update correctly | Works correctly | ✔ |
| Admin: Add meal | Add new meal | Appears in weekly form | Works correctly | ✔ |
| Admin: Edit meal | Change name/day | Updates in form + orders | Works correctly | ✔ |
| Mobile layout | View on phone | Table scrolls, dropdown readable | Works correctly | ✔ |


### Validation Testing

- HTML validatioed using W£C validator
- CSS validated using W£C CSS validator
- No major errors found

### User Story Testing

- Students can select meals for the week
- Kitchen staff can view totals
- Admin can manage meals
- All user stories met

---

# 📸 Screenshots

### Homepage
A screenshot showing the homepage with the logo, tagline, and navigation to MealsHub.

![Homepage Screenshot](documentation/homepage.png)


---
# 👤 Author
**Alison Mossop**  
MySchoolHub — MealsHub Module

[def]: documentation/screenshot/home_page.png