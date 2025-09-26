from django.db import models

sub = [('Algo', 'Algo'), ('Django', 'Django'), ('Django_Rest', 'Django_Rest'), ('SQL', 'SQL')]


class Cont(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    created_time = models.DateField(auto_now_add=True)
    tag = models.CharField(choices=sub)
    
    class Meta:
        pass
    
    def __str__(self):
        return f"{self.title}  {self.content} ({self.tag})"