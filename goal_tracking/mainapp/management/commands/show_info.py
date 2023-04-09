from django.core.management.base import BaseCommand, CommandError
from mainapp.models import User, Category, Goal


class Command(BaseCommand):
    help = 'show db'

    def handle(self, *args, **options):
        print(User.objects.all())
        print(Category.objects.all())
        print(Goal.objects.all())
        print(Goal.objects.filter(categories__name="работа"))