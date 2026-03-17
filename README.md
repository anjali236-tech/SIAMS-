# SIAMS – Smart Inventory and Asset Management System

## 📌 Overview

SIAMS is a web-based application developed to manage and track assets in a college environment, such as server rooms and asset storage areas.
It helps in monitoring asset availability, tracking usage, and maintaining inventory efficiently.

---

## 🚀 Features

* View all assets and their status
* Track availability (Available / In Use)
* Simple dashboard interface
* Backend-connected database for real-time updates

---

## 🛠️ Tech Stack

* **Backend:** Python (Flask)
* **Frontend:** HTML, CSS
* **Database:** MySQL

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/your-username/SIAMS.git
cd SIAMS
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Setup MySQL

* Create a database named `siams`
* Create a table:

```
CREATE TABLE assets (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    status VARCHAR(50)
);
```

### 4. Run the application

```
python app.py
```

### 5. Open in browser

```
http://127.0.0.1:5000/
```

---

## 📸 Screenshots
<img width="1923" height="912" alt="image" src="https://github.com/user-attachments/assets/8b334030-d7ed-4401-ae81-e9300728d040" />
<img width="1905" height="858" alt="image" src="https://github.com/user-attachments/assets/d8d369f2-c8d7-4a52-bb97-eb935c7cbc3d" />
<img width="1906" height="395" alt="image" src="https://github.com/user-attachments/assets/26e0999f-15a4-41fc-a54e-2d987f8674b8" />





---

## ⚠️ Note

This project currently runs on a local MySQL server (localhost).
It is not deployed online yet. Future improvements include cloud deployment and database hosting.

---

## 🔮 Future Enhancements

* Migration to Java (Spring Boot, Hibernate)
* User authentication system
* Role-based access (Admin/User)
* Cloud deployment with live database

---

## 👤 Author

**Anjali Muralidharan**
🔗 LinkedIn: https://linkedin.com/in/anjali-muralidharan-824559327
💻 GitHub: https://github.com/anjali236-tech

---

## ⭐ Acknowledgment

This project was built as part of academic learning to apply concepts of web development, database management, and backend integration.
