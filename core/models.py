from django.db import models

# Create your models here.
category1 = [
    ('Fashion', 'Fashion'),
    ('Lifestyle', 'Lifestyle'),
    ('Travel', 'Travel'),
    ('Food', 'Food'),
    ('Health', 'Health'),
]
class Cloapedia(models.Model):
    title = models.CharField(max_length = 255)
    content = models.TextField()
    image = models.TextField()
    category = models.CharField(max_length = 255, choices = category1)
    name = models.CharField(max_length = 255)
    date = models.DateTimeField(auto_now = False)
    def __str__(self):
        return self.title