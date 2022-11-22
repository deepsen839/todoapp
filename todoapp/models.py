from django.db import models

STATUS_CHOICES = (
    ('select',''),
    ("1","pending"),
    ("2","completed"),
)


# Create your models here.
class TodoModel(models.Model):
    name = models.CharField(max_length=200,null=True)
    task_status = models.CharField(
        max_length = 20,
        choices = STATUS_CHOICES,
        default = ''
        )