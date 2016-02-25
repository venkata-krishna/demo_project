from django.contrib import admin
from polls.models import UserForm, Car, Age,Name
# Register your models here.
from polls.models import Poll, Choice,Question
admin.site.register(Poll)
admin.site.register(Choice)
admin.site.register(UserForm)
admin.site.register(Car)
admin.site.register(Age)
admin.site.register(Name)
admin.site.register(Question)