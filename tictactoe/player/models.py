from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Invitation(models.Model):
  from_user = models.ForeignKey(User, related_name="invitation_sent")
  to_user = models.ForeignKey(User, related_name="invitation_recieved", verbose_name="User to invite", help_text="Please selet the user you want to play a game with")
  message = models.CharField(max_length=300,blank=True, verbose_name="Optional Message", help_text="its always nice to add a friendly message")
  timestamp = models.DateTimeField(auto_now_add=True)
