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
        db.users.insert_many(users)

        # Test data for teams
        teams = [
            {"name": "Team Alpha", "members": ["User One", "User Two"]},
            {"name": "Team Beta", "members": []},
        ]
        db.teams.insert_many(teams)

        # Test data for activities
        activities = [
            {"activity_id": "A1", "description": "Running"},
            {"activity_id": "A2", "description": "Swimming"},
        ]
        db.activity.insert_many(activities)

        # Test data for leaderboard
        leaderboard = [
            {"leaderboard_id": "L1", "scores": {"User One": 100, "User Two": 80}},
        ]
        db.leaderboard.insert_many(leaderboard)

        # Test data for workouts
        workouts = [
            {"workout_id": "W1", "exercises": ["Push-ups", "Sit-ups"]},
            {"workout_id": "W2", "exercises": ["Squats", "Lunges"]},
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the octofit_db database with test data'))
