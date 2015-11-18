from django.db import models

from django.contrib.auth.models import User

from django.db.models.signals import m2m_changed

import uuid
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model


class CityCas(models.Model):
    state = columns.Text(required=False, primary_key=True)
    name = columns.Text(required=False)  


class UserProfile(models.Model):
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    user = models.OneToOneField(User, null=True, blank=True)
    
    def __unicode__(self):
        return "%s" % self.user


class State(models.Model):
    name = models.CharField(max_length=255, null=True)
    abbrev = models.CharField(max_length=2, null=True, blank=True)
    pop = models.IntegerField(null=True, blank=True)
    state_map = models.ImageField(upload_to='state_map', null=True, blank=True)
    upvotes = models.ManyToManyField('main.UserProfile', related_name="up_votes")
    downvotes = models.ManyToManyField('main.UserProfile', related_name="down_votes")

    upvotes_count = models.IntegerField(default=0, null=True, blank=True)
    downvotes_count = models.IntegerField(default=0, null=True, blank=True)

    votes = models.IntegerField(null=True, blank=True)

    @property
    def total_votes(self):
        total_votes = self.upvotes_count - self.downvotes_count
        return total_votes

    def __unicode__(self):
        return self.name


def recount_up(sender, instance,  **kwargs):
    print "upvotes_count: %s , upvotes.count: %s" % (instance.upvotes_count, instance.upvotes.count())

    instance.upvotes_count = instance.upvotes.count()
    instance.save()

    instance.votes = instance.upvotes_count - instance.downvotes_count
    instance.save()

    
m2m_changed.connect(recount_up, sender=State.upvotes.through)


def recount_down(sender, instance,  **kwargs):
    print "downvotes_count: %s , downvotes.count: %s" % (instance.downvotes_count, instance.downvotes.count())
    instance.downvotes_count = instance.downvotes.count()
    instance.save()

    instance.votes = instance.upvotes_count - instance.downvotes_count
    instance.save()

    print "downvotes_count%s , downvotes.count: %s, votes: %s" % (instance.downvotes_count, instance.downvotes.count(), instance.votes)

m2m_changed.connect(recount_down, sender=State.downvotes.through)


class StateCapital(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True) 
    state = models.OneToOneField('main.State', null=True)
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)
    pop = models.IntegerField(null=True, blank=True)
    #state = models.ForeignKey('main.state', null=True, blank=True)
    #state = models.OneToOneField('main.State', null=True, blank=True)
    class Meta:
        verbose_name_plural='State Capitals'

    def __unicode__(self):
        return"%s" % self.name

    class Meta:
        verbose_name_plural='State Capitals'


class City(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True, db_index=True)
    county = models.CharField(max_length=100, null=True, blank=True)
    state = models.ForeignKey("main.State", null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    class Meta:
        verbose_name_plural="cities"

    def __unicode__(self):
        return "%s" % self.name


# #class CustomUserManager(BaseUserManager):  
#     def _create_user(self, email, username, password, is_staff, is_superuser, **extra_fields):
#         now = timezone.now()

#         if username != None:
#             email = username

#         if not email:
#             raise ValueError("Email must be set")
#         email = self.normalize_email(email)
#         user = self.model(email=email,
#                           is_staff=is_staff,
#                           is_active=True,
#                           is_superuser=is_superuser,
#                           last_login=now,
#                           date_joined=now,
#                           **extra_fields
#                           )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_user(self, email=None, username=None, password=None, **extra_fields):
#         return self._create_user(email, username, password, False, False, **extra_fields)

#     def create_superuser(self, email, username, password, **extra_fields):
#         return self._create_user(email, password, True, True, **extra_fields)


# # #class CustomUser(AbstractBaseUser, PermissionsMixin): 
# #     email = models.EmailField('email address', max_length=255, unique=True)
# #     first_name = models.CharField('first name', max_length=30, blank=True, null=True)
# #     last_name = models.CharField('last name', max_length=30, blank=True, null=True)
# #     is_staff = models.BooleanField('staff status', default=False)
# #     is_active = models.BooleanField('active', default=True)
# #     date_joined = models.DateTimeField('date joined', auto_now_add=True)
# #     objects = CustomUserManager()

# #     USERNAME_FIELD = 'email'
# #     REQUIRED_FIELDS = []

# #     class Meta:
# #         verbose_name = 'user'
# #         verbose_name_plural = 'users'

# #     def get_absolute_url(self):
# #         return "/users/%s/" % urlquote(self.email)

# #     def get_full_name(self):
# #         full_name = '%s %s' % (self.first_name, self.last_name)
# #         return full_name.strip()

# #     def get_short_name(self):
# #         return self.first_name

# #     def email_user(self, subject, message, from_email=None):
# #         send_mail(subject, message, from_email, [self.email])
