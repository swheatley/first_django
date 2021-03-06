from django.contrib import admin
from main.models import State, StateCapital, City, UserProfile
# Register your models here.


class StateCapitalAdmin(admin.ModelAdmin):
    list_display = ('name', 'pop')
    search_fields = ('name',)



class StateAdmin(admin.ModelAdmin):
        list_display = ('name', 'abbrev')
        search_fields = ['name']
        #inlines = [StateCapitalInline]


class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'state')


admin.site.register(UserProfile)
admin.site.register(StateCapital, StateCapitalAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(City, CityAdmin)