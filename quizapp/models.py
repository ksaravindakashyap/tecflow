from django.db import models

# Create your models here.
class QUIZFORM(models.Model):
    questions = models.TextField(max_length=1000)
    choice1 =   models.CharField(max_length=100)
    choice2 =   models.CharField(max_length=100)
    choice3 =   models.CharField(max_length=100)
    choice4 =   models.CharField(max_length=100)
    correctanswer = models.CharField(max_length=100)

    

    class Meta:
        db_table = "quizapp"


