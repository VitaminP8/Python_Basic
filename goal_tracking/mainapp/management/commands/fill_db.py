from django.core.management.base import BaseCommand, CommandError

from mainapp.models import User, Category, Goal
from userapp.models import MyUser


class Command(BaseCommand):
    help = 'Fill db'

    def handle(self, *args, **options):
        MyUser.objects.all().delete()
        Category.objects.all().delete()
        Goal.objects.all().delete()

        # create superuser
        try:
            MyUser.objects.create_superuser('admin', 'admin@admin.com', 'admin123')
        except:
            print('Админ уже был создан раньше')

        gleb = MyUser.objects.create_user(
            username="gleb",
            email="gleb@gleb.com",
            password="admin123456"
        )
        nikita = MyUser.objects.create_user(
            username="nikita",
            email="nikita@nikita.com",
            password="admin123456"
        )
        print(MyUser.objects.all())

        personal = Category.objects.create(name="личное")
        work = Category.objects.create(name="работа")
        family = Category.objects.create(name="семья")
        studies = Category.objects.create(name="учеба")
        print(Category.objects.all())
        #
        # finish_hw = Goal.objects.create(
        #     name="закончить дз",
        #     deadline="2023-4-12",
        #     user=gleb,
        # )
        # finish_hw.categories.clear()
        # finish_hw.categories.set([studies, work])
        # finish_hw.save()
        # do_work = Goal.objects.create(
        #     name="сделать работу",
        #     deadline="2023-5-14",
        #     user = nikita,
        # )
        # do_work.categories.clear()
        # do_work.categories.add(work)
        # do_work.save()
        # buy_food = Goal.objects.create(
        #     name='купить еду',
        #     deadline="2023-4-23",
        #     user=nikita,
        # )
        # buy_food.categories.clear()
        # buy_food.categories.add(personal)
        # buy_food.categories.add(family)
        # buy_food.save()
        # print(Goal.objects.all())