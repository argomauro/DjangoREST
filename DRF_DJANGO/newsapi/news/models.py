from django.db import models



class Journalist(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    biography = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name[:1]}. {self.last_name[:1]}."

# Create your models here.
class Article(models.Model):
    author = models.ForeignKey(Journalist, on_delete=models.CASCADE,related_name='articles')
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=200)
    body = models.TextField()
    location = models.CharField(max_length=120)
    publication_date = models.DateField()
    active = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{ self.author } - { self.title }"

