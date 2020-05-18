from django.db import models

class Quote(models.Model):
    author = models.CharField(max_length=60)
    quote = models.CharField(max_length=250)
    context = models.CharField(max_length=150)
    source = models.CharField(max_length=90)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.author} - {self.quote[:20]} ....'
