from django.db import models

# Create your models here.
class Todo(models.Model):
    titre = models.CharField(verbose_name="Le titre du todo", max_length=120)
    descr = models.TextField("La description")
    fait_le = models.DateTimeField(auto_now_add=True)
