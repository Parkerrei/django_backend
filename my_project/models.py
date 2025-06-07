from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return (f'{self.name}')

  
class Book(models.Model):
    title = models.CharField(max_length=400)
    content = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
  
    def __str__(self):
        return (f'Post:{self.title},{self.content},{self.author.name}')
