from rest_framework import serializers

# Define serializers for users, teams, activity, leaderboard, and workouts
class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    name = serializers.CharField(max_length=100)

class TeamSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    members = serializers.ListField(child=serializers.CharField(max_length=100))

class ActivitySerializer(serializers.Serializer):
    activity_id = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=255)

class LeaderboardSerializer(serializers.Serializer):
    leaderboard_id = serializers.CharField(max_length=100)
    scores = serializers.DictField()

class WorkoutSerializer(serializers.Serializer):
    workout_id = serializers.CharField(max_length=100)
    exercises = serializers.ListField(child=serializers.CharField(max_length=100))
