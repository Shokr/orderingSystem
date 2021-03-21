from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db.models import CharField, TextChoices, Manager, EmailField
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(
            self, username, email, password=None, is_staff=False, is_active=True, type="CUSTOMER", **extra_fields
    ):
        """Create a user instance with the given email and password."""
        email = UserManager.normalize_email(email)

        user = self.model(
            username=username, email=email, is_active=is_active, is_staff=is_staff, type=type, **extra_fields
        )
        if password:
            user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password=None, type="ADMIN", **extra_fields):
        return self.create_user(
            username, email, password, is_staff=True, is_superuser=True, type=type, **extra_fields
        )


class User(AbstractUser):
    """Default user for Promo."""

    class Types(TextChoices):
        ADMIN = "ADMIN", "Admin"
        CUSTOMER = "CUSTOMER", "Customer"

    base_type = Types.CUSTOMER

    # What type of user are we?
    type = CharField(_("Type"), max_length=50, choices=Types.choices, default=base_type)

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)

    address = CharField(max_length=255, blank=True, null=True)
    mobile_number = CharField(max_length=11, unique=True, blank=True, null=True,
                              validators=[RegexValidator(regex=r'^\+?1?\d{11,11}$',
                                                         message="Mobile Number must be entered [01xxxxxxxxx] Num.")])

    email = EmailField(unique=True)

    CURRENCY_CHOICES = [('USD', 'USD $'), ('EUR', 'EUR €')]
    currency = CharField(max_length=300, choices=CURRENCY_CHOICES, default='EUR')

    objects = UserManager()

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)

    def __str__(self):
        return '{} [{}]'.format(self.username, self.type)


class AdminManager(Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.ADMIN)


class CustomerManager(Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.CUSTOMER)


class Admin(User):
    base_type = User.Types.ADMIN
    objects = AdminManager()

    class Meta:
        proxy = True


class Customer(User):
    base_type = User.Types.CUSTOMER
    objects = CustomerManager()

    class Meta:
        proxy = True
