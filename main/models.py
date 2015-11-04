from django.db import models


class State(models.Model):
    name = models.CharField(max_length=255, null=True)
    abbrev = models.CharField(max_length=2, null=True, blank=True)
    pop = models.IntegerField(null=True, blank=True)
    state_map = models.ImageField(upload_to='state_map', null=True, blank=True)

    def __unicode__(self):
        return self.name


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
    name = models.CharField(max_length=100, null=True, blank=True)
    county = models.CharField(max_length=100, null=True, blank=True)
    state = models.ForeignKey("main.State", null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    class Meta:
        verbose_name_plural="cities"

    def __unicode__(self):
        return "%s" % self.name

