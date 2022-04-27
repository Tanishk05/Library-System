from django.db import models

# Create your models here.
class Books(models.Model):
    book_name = models.CharField(max_length=200)
    book_desc = models.TextField()
    book_author = models.CharField(max_length=200)
    book_rental = models.IntegerField()
    book_available = models.IntegerField(default=1)
    no_of_time_issued = models.IntegerField(default=0)

    def __str__(self):
        return self.book_name
    