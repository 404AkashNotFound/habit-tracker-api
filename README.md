# 🧠 Habit Tracker API

A simple Habit Tracker built using **Flask**, **MongoDB**, and a basic **HTML + JS** frontend.  
Built during the Keploy GitHub Learning Program to practice REST API design, database integration, and full-stack basics.

---

## 🚀 Features

- 🛠️ Custom REST API with 5 endpoints  
- 🧾 CRUD operations on habits  
- 🧮 MongoDB backend  
- 🌐 HTML + JavaScript frontend  
- 🔐 Environment variables support  

---

## 📁 Project Structure

\`\`\`
habit-tracker/
├── app.py                 # Main Flask app
├── config.py              # MongoDB connection
├── routes/
│   └── habit_routes.py    # API endpoints
├── templates/
│   └── index.html         # Frontend
├── static/
│   └── style.css          # CSS
├── .env                   # Environment config
├── requirements.txt       # Python deps
└── README.md              # This file
\`\`\`

---

## 📦 Tech Stack

- **Backend:** Flask (Python)  
- **Frontend:** HTML, JavaScript  
- **Database:** MongoDB  
- **Tools:** dotenv, Flask-CORS  

---

## 🌐 API Documentation

| Method | Endpoint                        | Description              |
|--------|---------------------------------|--------------------------|
| GET    | `/habits`                       | Get all habits           |
| GET    | `/habits/<user>`                | Get habits by user       |
| POST   | `/habits`                       | Add a new habit          |
| PUT    | `/habits/<user>/<habit>`        | Update an existing habit |
| DELETE | `/habits/<user>/<habit>`        | Delete a habit           |

---

## 📥 Sample Requests

### ➕ Add Habit

\`\`\`bash
curl -X POST http://localhost:5000/habits \
-H "Content-Type: application/json" \
-d '{"user": "akash", "habit": "Coding", "frequency": "Daily"}'
\`\`\`

### 🔍 Get Habits

\`\`\`bash
curl http://localhost:5000/habits/akash
\`\`\`

### ✏️ Update Habit

\`\`\`bash
curl -X PUT http://localhost:5000/habits/akash/Coding \
-H "Content-Type: application/json" \
-d '{"frequency": "Weekly"}'
\`\`\`

### ❌ Delete Habit

\`\`\`bash
curl -X DELETE http://localhost:5000/habits/akash/Coding
\`\`\`

---

## 🛠️ Setup

### Prerequisites

- Python 3.x  
- MongoDB installed locally (or use MongoDB Atlas)  
- pip installed  

### Steps

1. **Clone the repo**

\`\`\`bash
git clone https://github.com/your-username/habit-tracker.git
cd habit-tracker
\`\`\`

2. **Create a `.env` file**

\`\`\`env
MONGO_URI=mongodb://localhost:27017
PORT=5000
\`\`\`

3. **Install dependencies**

\`\`\`bash
pip install -r requirements.txt
\`\`\`

4. **Run the server**

\`\`\`bash
python app.py
\`\`\`

5. **Visit the UI**  
Open `http://localhost:5000` in your browser.

---

## 💬 What I Learned

- How to build and structure a Flask API  
- Performing CRUD with MongoDB via PyMongo  
- Connecting frontends with REST APIs  
- Using Blueprints for modular route management  

---

## 🎯 Next Goals

I’m excited to start contributing to **Python** and **TypeScript** open-source projects. This project gave me the confidence to explore more real-world APIs and backends.

---

## 📬 Author

**Akash Kumar**  
B.Tech ECSE @ KIIT  
🔗 [GitHub](https://github.com/404AkashNotFound)

---

## 🙌 Special Thanks

Thanks to **Keploy** for this hands-on learning experience 🙏  
Check them out: [keploy/public-apis-collection](https://github.com/keploy/public-apis-collection)

---


