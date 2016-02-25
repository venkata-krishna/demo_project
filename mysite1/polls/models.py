from django.contrib import admin
from django.db import models
from django.contrib.admin.filters import ChoicesFieldListFilter
# Create your models here.
class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
class UserForm(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=100)
    ph_no=models.IntegerField(max_length=10)

COLORS= (
    ('R', 'Red'),
    ('B', 'Yellow'),
    ('G', 'White'),
)
class Car(models.Model):
    name = models.CharField(max_length=20)
    color= models.CharField(max_length=1, choices=COLORS)
age_list=(
          ('1','22'),
          ('2','23'),
          )
class Age(models.Model):
    name=models.CharField(max_length=20)
    age=models.CharField(max_length=1,choices=age_list)
    
name_list=(('k','krishna'),
           ('V','venkat'),
           )
class Name(models.Model):
    select_name=models.CharField(max_length=1,choices=name_list)
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')