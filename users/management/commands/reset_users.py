from django.core.management.base import BaseCommand, CommandError

from ...models import User, Admin, Customer


# reset db and insert 3 users
class Command(BaseCommand):
    help = "Adds a few base users"

    def handle(self, *args, **options):
        User.objects.all().delete()
        Admin.objects.create(
            username="muhammed", email="muhammed@shokr.works",
            password='argon2$argon2i$v=19$m=512,t=2,p=2$dFpyaVJON3pWQ09O$9YzyOo16jil0top+vKyIgQ',
            type=User.Types.ADMIN, is_staff=True, is_superuser=True
        )
        Customer.objects.create(
            username="nader", email="nader@gmail.com",
            password='argon2$argon2i$v=19$m=512,t=2,p=2$dFpyaVJON3pWQ09O$9YzyOo16jil0top+vKyIgQ',
            type=User.Types.CUSTOMER
        )
        Customer.objects.create(
            username="nour", email="nour@yahoo.com",
            password='argon2$argon2i$v=19$m=512,t=2,p=2$dFpyaVJON3pWQ09O$9YzyOo16jil0top+vKyIgQ',
            type=User.Types.CUSTOMER
        )
        self.stdout.write(self.style.SUCCESS("Users reset"))
