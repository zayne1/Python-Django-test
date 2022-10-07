from email.policy import default
from lib2to3.pgen2.token import MINUS
from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateField('date published')

    # show a more meaningful label on admin panel
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    # tie choice to question via new FK, which is the model id of param 1, 
    # and do a cascade del
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    # show a more meaningful label on admin panel
    def __str__(self):
        return self.choice_text
