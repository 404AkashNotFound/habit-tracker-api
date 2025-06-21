from flask import Flask, render_template
from flask_cors import CORS
from dotenv import load_dotenv
import os

from routes import habit_routes

load_dotenv()  # Load env vars from .env file

app = Flask(__name__)
CORS(app)

# Register blueprint for API routes
app.register_blueprint(habit_routes)

# 👉 Frontend UI route
@app.route("/")
def index():
    return render_template("index.html")

# 👉 Optional API info route
@app.route("/api")
def api_info():
    return "🚀 Habit Tracker API is running! Hit a valid endpoint like /habits to get started."

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
