from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import EmailValidator
from django.utils.translation import gettext_lazy as _
from django.utils.translation import gettext
from django.contrib.auth.models import Group

from accounts.managers import CustomUserManager


# Groups settings needed for proper translate
_('admin')
_('journalist')
_('user')
Group.__str__ = lambda self: gettext(self.name)



class CustomUser(AbstractBaseUser, PermissionsMixin):
    """ Custom-defined user of the application contains all needed fields
    to his proper authentication such as email and password.

    Notes
    -----
    Because of inheritance from PermissionsMixin model, user model contains the `groups` filed.
    """
    EMAIL_VALIDATOR = EmailValidator(message='Unhallowed format of user email')
    EMAIL_MAX_LENGTH = 100

    id = models.BigAutoField(primary_key=True)
    email = models.EmailField(verbose_name=_('Email address'), validators=[EMAIL_VALIDATOR], unique=True, max_length=EMAIL_MAX_LENGTH)
    is_staff = models.BooleanField(verbose_name=_('Is Staff'), default=False)
    is_active = models.BooleanField(verbose_name=_('Is Active'), default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = _('Account')
        verbose_name_plural = _('Accounts')

    def __str__(self):
        return f'{self.email}'

    def __repr__(self):
        return f'CustomUser(email={self.email})'
