from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser,
)

from fusionbox import behaviors


class UserManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        user = self.model(
            email=UserManager.normalize_email(email),
            name=name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(
            email=email,
            name=name,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(behaviors.Timestampable, AbstractBaseUser):
    email = models.EmailField(_('email'), max_length=255, unique=True,
                              db_index=True, help_text=_('A valid email address'))
    name = models.CharField(_('name'), max_length=255)

    is_active = models.BooleanField(_('active'), default=True, blank=True)
    is_superuser = models.BooleanField(_('superuser'), default=False, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def __unicode__(self):
        return u'{name} ({email})'.format(**vars(self))

    @property
    def is_staff(self):
        return self.is_superuser

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
