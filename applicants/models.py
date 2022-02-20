from operator import mod
from django.db import models
from base.models import Jobs
from users.models import Newuser

class Applications(models.Model):
    applied_date = models.DateField(auto_now_add = True)
    selected = models.BooleanField(default=False)
    user = models.ForeignKey(Newuser,on_delete=models.CASCADE )
    job = models.ForeignKey(Jobs, on_delete=models.CASCADE)

    