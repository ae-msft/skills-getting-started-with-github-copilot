from fastapi.testclient import TestClient

from src.app import activities, app


def test_signup_adds_participant_to_activity_state():
    client = TestClient(app)
    activity_name = "Chess Club"
    email = "newstudent@mergington.edu"
    original_participants = list(activities[activity_name]["participants"])

    try:
        response = client.post(f"/activities/{activity_name}/signup?email={email}")

        assert response.status_code == 200
        assert email in activities[activity_name]["participants"]
        assert response.json()["message"] == f"Signed up {email} for {activity_name}"
    finally:
        activities[activity_name]["participants"] = original_participants
