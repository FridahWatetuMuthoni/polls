from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def was_published_recently(self):
        """
        timezone.now() => returns the current date and time
        datetime.timedelta(days=1) => this creates a timedelta object representing a duration of 1 day
        timezone.now() - datetime.timedelta(days=1) => this calculates the point in time exactly 1 day(24 hours) b4 the current time
        self.pub_date >= timezone.now() - datetime.timedelta(days=1) returns true is the poll was published in the last day
        """
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="choices")
    choice_text = models.CharField(max_length=250)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text