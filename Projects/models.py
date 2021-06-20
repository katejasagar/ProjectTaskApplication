from datetime import time
from django.db import models
from django.utils import timezone
from PIL import Image
from django.contrib.auth.models import User
# Create your models here.

class Projects(models.Model):

    
    project_id = models.AutoField(primary_key=True, unique=True)
    #u_id = models.ForeignKey(User,on_delete=models.CASCADE)
    project_name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.DurationField()
    status = models.CharField(('status'), max_length=20, default='to-do')
    image = models.ImageField(default ='default.jpg', upload_to = 'pictures')

    def __str__(self):
        return self.project_name

    def save(self, *args, **kawrgs):
        super().save(*args, **kawrgs) 
        img = Image.open(self.image.path) #Open the path of user profile
        if img.height > 300 or img.width > 300:
            output_size = (300,300)   
            img.thumbnail(output_size) #resize image to 300*300
            img.save(self.image.path)   #saving the image to the sam

class Tasks(models.Model):
    task_id =  models.AutoField(primary_key=True, unique=True)
    project_id = models.ForeignKey(Projects,on_delete=models.CASCADE)
    task_name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    