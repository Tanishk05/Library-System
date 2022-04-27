from django.db import models
# Create your models here.
class Inventory(models.Model):
    student_name = models.CharField(max_length=200)
    book_name_to_be_issued = models.CharField(max_length=200)
    book_rental = models.IntegerField()
    date_issued = models.DateField()

    def __str__(self):
        return self.student_name
    