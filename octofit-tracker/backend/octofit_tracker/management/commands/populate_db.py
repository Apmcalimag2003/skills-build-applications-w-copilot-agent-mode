from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Team.objects.all().delete()
        User.objects.all().delete()

        # Create users (super heroes)
        marvel_heroes = [
            {'username': 'ironman', 'email': 'ironman@marvel.com', 'first_name': 'Tony', 'last_name': 'Stark'},
            {'username': 'spiderman', 'email': 'spiderman@marvel.com', 'first_name': 'Peter', 'last_name': 'Parker'},
            {'username': 'captainamerica', 'email': 'cap@marvel.com', 'first_name': 'Steve', 'last_name': 'Rogers'},
        ]
        dc_heroes = [
            {'username': 'batman', 'email': 'batman@dc.com', 'first_name': 'Bruce', 'last_name': 'Wayne'},
            {'username': 'superman', 'email': 'superman@dc.com', 'first_name': 'Clark', 'last_name': 'Kent'},
            {'username': 'wonderwoman', 'email': 'wonderwoman@dc.com', 'first_name': 'Diana', 'last_name': 'Prince'},
        ]
        marvel_users = [User.objects.create(**hero) for hero in marvel_heroes]
        dc_users = [User.objects.create(**hero) for hero in dc_heroes]

        # Create teams
        marvel_team = Team.objects.create(name='Marvel')
        dc_team = Team.objects.create(name='DC')
        marvel_team.members.set(marvel_users)
        dc_team.members.set(dc_users)

        # Create workouts
        workout1 = Workout.objects.create(name='Push Ups', description='Do 20 push ups', difficulty='Easy')
        workout2 = Workout.objects.create(name='Running', description='Run 5km', difficulty='Medium')
        workout3 = Workout.objects.create(name='Squats', description='Do 30 squats', difficulty='Easy')

        # Create activities
        Activity.objects.create(user=marvel_users[0], type='Running', duration=30, calories=300, date='2025-11-27')
        Activity.objects.create(user=dc_users[0], type='Push Ups', duration=15, calories=100, date='2025-11-27')

        # Create leaderboard
        Leaderboard.objects.create(user=marvel_users[0], score=100, rank=1)
        Leaderboard.objects.create(user=dc_users[0], score=90, rank=2)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
