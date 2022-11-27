from django.db import models
from student.models import Student


# Create your models here.


class Exam(models.Model):
    exam_id= models.AutoField(primary_key=True, unique=True)
    name=models.CharField(blank=False,max_length=250,unique=True, default="Haha")
    
    def __str__(self):
        return self.name

class Question(models.Model):
    question_id=models.AutoField(primary_key=True)
    question=models.TextField(max_length=500,blank=False,unique=True)
    option1=models.CharField(max_length=250,blank=False)
    option2=models.CharField(max_length=250,blank=False)
    option3=models.CharField(max_length=250,blank=False)
    option4=models.CharField(max_length=250,blank=False)
    correct_ans=models.CharField(max_length=250,blank=False)
    exam=models.ForeignKey(Exam,on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return self.name   

class Score(models.Model):
    score_id=models.AutoField(primary_key=True, unique=True)
    score=models.IntegerField(blank=False)
    student=models.ForeignKey(Student,on_delete=models.CASCADE,blank=False)
    exam=models.ForeignKey(Exam,on_delete=models.CASCADE,blank=False)

    def __int__(self):
        return self.score
    
    class Meta:
        unique_together = ('student', 'exam')



# Course means test
# A score array will be there in student with objects inside of it and the object will have test_id as key and test_score as value. when the student will click on submit in test, an item in the array will be added and student will not be able to open that test again. and when he submits a new test in the array the score (key-value pair) of that will also be appended.