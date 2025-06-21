# Habit Tracker API

A simple REST API built with Flask and MongoDB to manage user habits.

## 📦 Tech Stack

- Backend: Flask
- Database: MongoDB
- Others: Python Dotenv, Flask-CORS

## 🚀 API Endpoints

### `GET /habits`
- Returns all habits in the database.

### `GET /habits/<user>`
- Returns all habits for a specific user.

### `POST /habits`
- Adds a new habit.
```json
{
  "user": "akash",
  "habit": "Reading",
  "frequency": "daily"
}
