from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        user = User.objects.create(
            email='admin@admin.com',
            first_name='Superuser',
            last_name='West',
            is_active=True,
            is_staff=True,
            is_superuser=True,
        )

        user.set_password('12345')
        user.save()
