from django.db import models

# Create your models here.
class Quizes(models.Model):
    topic = models.CharField(max_length=50)
    creater = models.CharField(null=True, blank=True, max_length=50)
    question_file = models.FileField(upload_to='Store', max_length=100)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.topic

class Result(models.Model):
    quiz = models.ForeignKey(Quizes, on_delete=models.CASCADE,null=True,blank=True)
    attempted = models.CharField(null=True, blank=True, max_length=50)
    marks = models.PositiveIntegerField(null=True,blank=True)
    total_marks = models.PositiveIntegerField(null=True,blank=True)
    created_at = models.DateField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return f"Your score is {self.marks} out of {self.total_marks}"
    