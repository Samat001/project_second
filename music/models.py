from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self) -> str:
        return self.name

    

class Music(models.Model):
    title = models.CharField(max_length=50)
    durations = models.PositiveIntegerField()
    create_at = models.DateField(auto_now_add=True)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='Musics')

    def __str__(self) -> str:
        return self.title

