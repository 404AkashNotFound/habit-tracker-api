from flask import Blueprint, request, jsonify
from config import habits_collection

habit_routes = Blueprint("habit_routes", __name__)

@habit_routes.route("/habits", methods=["GET"], endpoint="get_all_habits")
def get_habits():
    """
    Get all habits
    ---
    responses:
      200:
        description: A list of all habits
    """
    habits = list(habits_collection.find({}, {"_id": 0}))
    return jsonify(habits), 200

@habit_routes.route("/habits/<string:user>", methods=["GET"], endpoint="get_user_habits")
def get_user_habits(user):
    """
    Get habits by user
    ---
    parameters:
      - name: user
        in: path
        type: string
        required: true
    responses:
      200:
        description: Habits for the user
    """
    habits = list(habits_collection.find({"user": user}, {"_id": 0}))
    return jsonify(habits), 200

@habit_routes.route("/habits", methods=["POST"], endpoint="add_habit")
def add_habit():
    """
    Add a new habit
    ---
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            user:
              type: string
            habit:
              type: string
            frequency:
              type: string
    responses:
      201:
        description: Habit added
    """
    data = request.json
    if not all(key in data for key in ("user", "habit", "frequency")):
        return jsonify({"error": "Missing required fields"}), 400
    habits_collection.insert_one(data)
    return jsonify({"message": "Habit added"}), 201

@habit_routes.route("/habits/<string:user>/<string:habit>", methods=["PUT"], endpoint="update_habit")
def update_habit(user, habit):
    """
    Update an existing habit
    ---
    parameters:
      - name: user
        in: path
        type: string
        required: true
      - name: habit
        in: path
        type: string
        required: true
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            frequency:
              type: string
    responses:
      200:
        description: Habit updated
    """
    data = request.json
    result = habits_collection.update_one(
        {"user": user, "habit": habit},
        {"$set": data}
    )
    if result.matched_count == 0:
        return jsonify({"error": "Habit not found"}), 404
    return jsonify({"message": "Habit updated"}), 200

@habit_routes.route("/habits/<string:user>/<string:habit>", methods=["DELETE"], endpoint="delete_habit")
def delete_habit(user, habit):
    """
    Delete a habit
    ---
    parameters:
      - name: user
        in: path
        type: string
        required: true
      - name: habit
        in: path
        type: string
        required: true
    responses:
      200:
        description: Habit deleted
    """
    result = habits_collection.delete_one({"user": user, "habit": habit})
    if result.deleted_count == 0:
        return jsonify({"error": "Habit not found"}), 404
    return jsonify({"message": "Habit deleted"}), 200
