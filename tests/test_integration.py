def test_add_and_get_habit(client, clear_db):
    # Add habit
    client.post("/habits", json={
        "user": "john",
        "habit": "Reading",
        "frequency": "Daily"
    })
    # Get habit
    resp = client.get("/habits/john")
    data = resp.get_json()
    assert resp.status_code == 200
    assert any(h["habit"] == "Reading" for h in data)

def test_update_habit(client, clear_db):
    client.post("/habits", json={"user": "anna", "habit": "Yoga", "frequency": "Weekly"})
    resp = client.put("/habits/anna/Yoga", json={"frequency": "Daily"})
    assert resp.status_code == 200
    get_resp = client.get("/habits/anna")
    assert get_resp.get_json()[0]["frequency"] == "Daily"

def test_delete_habit(client, clear_db):
    client.post("/habits", json={"user": "max", "habit": "Jogging", "frequency": "Weekly"})
    resp = client.delete("/habits/max/Jogging")
    assert resp.status_code == 200
    # Confirm deletion
    get_resp = client.get("/habits/max")
    assert len(get_resp.get_json()) == 0
