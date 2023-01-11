from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import BasePasswordHasher, check_password

from django.shortcuts import HttpResponse

class UserPasswordHash(BasePasswordHasher):
    algorithm = 'a'
    iterations = None
    library = None
    salt_entropy = None

    def salt(self):
        return ''

    def encode(self, password, salt='_'):
        stroke = self.algorithm+'$'+password
        return stroke

    def decode(self, password):
        return password[2:]

    def verify(self, password, encoded):
        decoded = self.decode(encoded)
        return password == decoded

    def harden_runtime(self, password, encoded):
        pass

    def safe_summary(self, encoded):
        return {
            ("algorithm"): '',
            ("iterations"): '',
            ("salt"): '',
            ("hash"): self.decode(encoded),
        }



class UserManager(BaseUserManager):

    def create_user(self, login, password=None, position='Безработный'):
        if not login:
            raise ValueError('Users must have a login')

        user = self.model(
            login=login,
            position=position,
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, login, password=None, position='Разработчик БД'):

        user = self.create_user(
            login=login,
            password=password,
            position=position,
        )
        user.save(using=self._db)

        return user

class User(PermissionsMixin, AbstractBaseUser):
    USERNAME_FIELD = "login"
    last_login = None
    is_superuser = None
    login = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=1024)
    position = models.CharField(max_length=20)

    objects = UserManager()


    def set_password(self, password):
        hasher = UserPasswordHash()
        self.password = hasher.encode(password)

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.position == 'Разработчик БД'

    @property
    def is_superuser(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.position == 'Разработчик БД'
