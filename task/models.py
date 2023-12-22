from audioop import reverse
from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE )
    created_at = models.DateTimeField(auto_now=True)
    due_date = models.DateField(auto_now=False)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("task_detail", kwargs={"pk": self.pk})
    

class Country(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Capital(models.Model):

    name = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, unique=True)
    
    def __str__(self):
        return self.name
    
    
class Book(models.Model):

    name = models.CharField(max_length=50)    

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class AuthorBook(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

