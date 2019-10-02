from django.db import models

# Create your models here.
class Todo(models.Model): # models 안의 Model을 상속받는다.
    title = models.CharField(max_length=50)
    due_date = models.DateField()