from flask import Blueprint, request, jsonify
from config import habits_collection

habit_routes = Blueprint("habit_routes", __name__)

@habit_routes.route("/habits", methods=["GET"])
def get_habits():
    habits = list(habits_collection.find({}, {"_id": 0}))
    return jsonify(habits), 200

@habit_routes.route("/habits/<string:user>", methods=["GET"])
def get_user_habits(user):
    habits = list(habits_collection.find({"user": user}, {"_id": 0}))
    return jsonify(habits), 200

@habit_routes.route("/habits", methods=["POST"])
def add_habit():
    data = request.json
    if not all(key in data for key in ("user", "habit", "frequency")):
        return jsonify({"error": "Missing required fields"}), 400
    habits_collection.insert_one(data)
    return jsonify({"message": "Habit added"}), 201

@habit_routes.route("/habits/<string:user>/<string:habit>", methods=["PUT"])
def update_habit(user, habit):
    data = request.json
    result = habits_collection.update_one(
        {"user": user, "habit": habit},
        {"$set": data}
    )
    if result.matched_count == 0:
        return jsonify({"error": "Habit not found"}), 404
    return jsonify({"message": "Habit updated"}), 200

@habit_routes.route("/habits/<string:user>/<string:habit>", methods=["DELETE"])
def delete_habit(user, habit):
    result = habits_collection.delete_one({"user": user, "habit": habit})
    if result.deleted_count == 0:
        return jsonify({"error": "Habit not found"}), 404
    return jsonify({"message": "Habit deleted"}), 200
