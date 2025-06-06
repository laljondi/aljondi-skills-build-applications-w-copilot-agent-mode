# Test data for the octofit_db database

users = [
    {"email": "user1@example.com", "name": "User One"},
    {"email": "user2@example.com", "name": "User Two"},
]

teams = [
    {"name": "Team Alpha", "members": ["User One", "User Two"]},
    {"name": "Team Beta", "members": []},
]

activities = [
    {"activity_id": "A1", "description": "Running"},
    {"activity_id": "A2", "description": "Swimming"},
]

leaderboard = [
    {"leaderboard_id": "L1", "scores": {"User One": 100, "User Two": 80}},
]

workouts = [
    {"workout_id": "W1", "exercises": ["Push-ups", "Sit-ups"]},
    {"workout_id": "W2", "exercises": ["Squats", "Lunges"]},
]
