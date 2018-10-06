from django.db import models
import jwt
from datetime import datetime, timedelta
from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
import uuid

from apps.books.models import Bookinfo


class UserManager(BaseUserManager):
    """
    Django requires that custom users define their own Manager class. By
    inheriting from `BaseUserManager`, we get a lot of the same code used by
    Django to create a `User`. 

    All we have to do is override the `create_user` function which we will use
    to create `User` objects.
    """

    def create_user(self, username, email, password=None):
        """Create and return a `User` with an email, username and password."""
        if username is None:
            raise TypeError('Users must have a username.')

        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password):
        """
        Create and return a `User` with superuser (admin) permissions.
        """
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user

class User(AbstractBaseUser, PermissionsMixin):

    class Meta:
        db_table = 'users'

    # Each `User` needs a human-readable unique identifier that we can use to
    # represent the `User` in the UI. We want to index this column in the
    # database to improve lookup performance.
    username = models.CharField(
        db_index=True, max_length=255, unique=True, verbose_name='用戶名稱')

    # We also need a way to contact the user and a way for the user to identify
    # themselves when logging in. Since we need an email address for contacting
    # the user anyways, we will also use the email for logging in because it is
    # the most common form of login credential at the time of writing.
    email = models.EmailField(db_index=True, unique=True, verbose_name='電子郵件')
    user_image = models.ImageField(upload_to='img', verbose_name='用戶圖片', blank=True)
    birthday = models.DateField(blank=True, null=True, verbose_name='生日')
    GENDER_CHOICES = (
                ('Male', '男'),
                ('Female', '女')
        )
    gender = models.CharField(
        max_length=5, choices=GENDER_CHOICES, null=True, blank=True, verbose_name='性別')
    location = models.CharField(
        max_length=255, null=True, blank=True, verbose_name='地區')
    about = models.TextField(blank=True, null=True, verbose_name='關於我')

    # When a user no longer wishes to use our platform, they may try to delete
    # their account. That's a problem for us because the data we collect is
    # valuable to us and we don't want to delete it. We
    # will simply offer users a way to deactivate their account instead of
    # letting them delete it. That way they won't show up on the site anymore,
    # but we can still analyze the data.
    is_active = models.BooleanField(default=True)

    # The `is_staff` flag is expected by Django to determine who can and cannot
    # log into the Django admin site. For most users this flag will always be
    # false.
    is_staff = models.BooleanField(default=False)

    # A timestamp representing when this object was created.
    created_at = models.DateTimeField(auto_now_add=True)

    # A timestamp reprensenting when this object was last updated.
    updated_at = models.DateTimeField(auto_now=True)

    # More fields required by Django when specifying a custom user model.
    # The `USERNAME_FIELD` property tells us which field we will use to log in.
    # In this case we want it to be the email field.
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    # Tells Django that the UserManager class defined above should manage
    # objects of this type.
    objects = UserManager()

    def __str__(self):
        """
        Returns a string representation of this `User`.

        This string is used when a `User` is printed in the console.
        """
        return self.email

    @property
    def token(self):
        """
        Allows us to get a user's token by calling `user.token` instead of
        `user.generate_jwt_token().

        The `@property` decorator above makes this possible. `token` is called
        a "dynamic property".
        """
        return self._generate_jwt_token()

    def get_full_name(self):
        """
        This method is required by Django for things like handling emails.
        Typically this would be the user's first and last name. Since we do
        not store the user's real name, we return their username instead.
        """
        return self.username

    def get_short_name(self):
        """
        This method is required by Django for things like handling emails.
        Typically, this would be the user's first name. Since we do not store
        the user's real name, we return their username instead.
        """
        return self.username

    def _generate_jwt_token(self):
        """
        Generates a JSON Web Token that stores this user's ID and has an expiry
        date set to 60 days into the future.
        """
        dt = datetime.now() + timedelta(days=60)

        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')

class UniUser(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True, verbose_name='電子郵件')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    jwt_secret = models.UUIDField(default=uuid.uuid4)

# Allowing the REST Framework JWT library to access this new field.
def jwt_get_secret_key(user_model):
    return user_model.jwt_secret


class Comments(models.Model):
    class Meta(object):
        db_table = 'comments'
        ordering = ['_id']

    _id = models.AutoField(unique=True, primary_key=True, verbose_name='評論ID')
    comment_text = models.TextField(blank=True, verbose_name='評論文字')
    RATING_CHOICES = (
        ('One', '1'),
        ('Two', '2'),
        ('Three', '3'),
        ('Four', '4'),
        ('Five', '5'),
    )
    rating = models.IntegerField(blank=True, verbose_name='評分')
    READ_STATUS_CHOICES = (
        ('Intend', '想讀'),
        ('Reading', '閱讀中'),
        ('Done', '已讀完')
    )
    read_status = models.CharField(
        blank=True, max_length=10, choices=READ_STATUS_CHOICES, verbose_name='閱讀狀態')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='建立時間')
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE, verbose_name='用戶ID')
    bookinfo = models.OneToOneField(
        Bookinfo, null=True, blank=True, on_delete=models.CASCADE, verbose_name='書籍ID')

class Bookshelf(models.Model):
    class Meta(object):
        db_table = 'bookshelf'
        ordering = ['_id']

    _id = models.AutoField(unique=True, primary_key=True, verbose_name='書櫃ID')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='建立時間')
    bookinfo = models.ForeignKey(
        Bookinfo, null=True, blank=True, on_delete=models.CASCADE, verbose_name='書籍')
    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE, verbose_name='用戶ID')
