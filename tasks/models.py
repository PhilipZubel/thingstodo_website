from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class Task(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	date = models.DateField()
	description = models.CharField(max_length = 100)
	isCompleted = models.BooleanField(default=False)

	class Meta:
		ordering =['-date']

	@property
	def is_past_due(self):
		return datetime.date.today() > self.date
