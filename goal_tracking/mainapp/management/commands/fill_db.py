from django.core.management.base import BaseCommand, CommandError
from mainapp.models import User, Category, Goal


class Command(BaseCommand):
    help = 'Fill db'

    def handle(self, *args, **options):
        User.objects.all().delete()
        Category.objects.all().delete()
        Goal.objects.all().delete()


        gleb = User.objects.create(name="Глеб", surname="Агапов")
        nikita = User.objects.create(name="Никита", surname="Рижский")
        print(User.objects.all())

        personal = Category.objects.create(name="личное")
        work = Category.objects.create(name="работа")
        family = Category.objects.create(name="семья")
        studies = Category.objects.create(name="учеба")
        print(Category.objects.all())

        finish_hw = Goal.objects.create(
            name="закончить дз",
            deadline="2023-4-12",
            user=gleb,
        )
        finish_hw.categories.clear()
        finish_hw.categories.set([studies, work])
        finish_hw.save()
        do_work = Goal.objects.create(
            name="сделать работу",
            deadline="2023-5-14",
            user = nikita,
        )
        do_work.categories.clear()
        do_work.categories.add(work)
        do_work.save()
        buy_food = Goal.objects.create(
            name='купить еду',
            deadline="2023-4-23",
            user=nikita,
        )
        buy_food.categories.clear()
        buy_food.categories.add(personal)
        buy_food.categories.add(family)
        buy_food.save()
        print(Goal.objects.all())