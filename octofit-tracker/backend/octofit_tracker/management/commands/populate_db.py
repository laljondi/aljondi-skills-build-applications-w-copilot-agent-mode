import sys
sys.path.append('/workspaces/aljondi-skills-build-applications-w-copilot-agent-mode/octofit-tracker/backend')

from django.core.management.base import BaseCommand
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Test data for users
        users = [
            {"email": "user1@example.com", "name": "User One"},
            {"email": "user2@example.com", "name": "User Two"},
        ]
        for user in users:
            db.users.update_one({"email": user["email"]}, {"$set": user}, upsert=True)

        # Test data for teams
        teams = [
            {"name": "Team Alpha", "members": ["User One", "User Two"]},
            {"name": "Team Beta", "members": []},
        ]
        for team in teams:
            db.teams.update_one({"name": team["name"]}, {"$set": team}, upsert=True)

        # Test data for activities
        activities = [
            {"activity_id": "A1", "description": "Running"},
            {"activity_id": "A2", "description": "Swimming"},
        ]
        for activity in activities:
            db.activity.update_one({"activity_id": activity["activity_id"]}, {"$set": activity}, upsert=True)

        # Test data for leaderboard
        leaderboard = [
            {"leaderboard_id": "L1", "scores": {"User One": 100, "User Two": 80}},
        ]
        for entry in leaderboard:
            db.leaderboard.update_one({"leaderboard_id": entry["leaderboard_id"]}, {"$set": entry}, upsert=True)

        # Test data for workouts
        workouts = [
            {"workout_id": "W1", "exercises": ["Push-ups", "Sit-ups"]},
            {"workout_id": "W2", "exercises": ["Squats", "Lunges"]},
        ]
        for workout in workouts:
            db.workouts.update_one({"workout_id": workout["workout_id"]}, {"$set": workout}, upsert=True)

        self.stdout.write(self.style.SUCCESS('Successfully populated the octofit_db database with test data'))
