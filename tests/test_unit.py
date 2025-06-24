from unittest.mock import patch

def test_get_habits_mock(client):
    with patch("routes.habits_collection.find") as mock_find:
        mock_find.return_value = [{"user": "test", "habit": "Coding", "frequency": "Daily"}]
        response = client.get("/habits")
        assert response.status_code == 200
        assert response.get_json()[0]["habit"] == "Coding"

def test_add_habit_missing_fields(client):
    response = client.post("/habits", json={"user": "test"})
    assert response.status_code == 400
    assert "error" in response.get_json()
