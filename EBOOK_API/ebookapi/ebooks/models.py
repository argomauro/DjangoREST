from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
# Create your models here.
class Ebook(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    publication_date = models.DateField()
    
    def __str__(self):
        return f"{self.title}"

class Review(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1),
                                         MaxValueValidator(5)])
    review = models.TextField(blank=True, null=True)
    author_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    ebook = models.ForeignKey(Ebook, on_delete=models.CASCADE, related_name='reviews')
    
    
    
    def __str__(self):
        return f"{self.rating}"