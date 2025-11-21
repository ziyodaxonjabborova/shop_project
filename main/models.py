from django.db import models

class Product(models.Model):
    image=models.FileField(upload_to="images")
    title=models.CharField(max_length=200)
    price=models.IntegerField()
    desc=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    is_active=models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
