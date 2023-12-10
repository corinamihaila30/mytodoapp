from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#crearea tabelelor si specificarea restrictiilor in baza de date
#de fiecare data cand adaugam models trebuie sa facem migrare
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) #daca contul nu mai exista TASK urile se vor sterge automat
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created =  models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    
    class Meta:
        ordering =['complete']
