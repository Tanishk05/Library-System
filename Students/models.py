from django.db import models

# Create your models here.
class Students(models.Model):
    student_name = models.CharField(max_length=200)
    student_phone = models.CharField(max_length=20)
    student_email = models.EmailField()
    student_address = models.CharField(max_length=500)
    no_of_books_issued = models.IntegerField(default=0)

    def __str__(self):
        return self.student_name
    