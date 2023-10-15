from django.db import models


from django.db import models

class ChatMessage(models.Model):
    sender = models.CharField(max_length=100)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    parent_message = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')

    def __str__(self):
        return f'{self.sender}: {self.message}'
    

from django.db import models

class Resource(models.Model):
    SUBJECT_CHOICES = [
        ('mathematics', 'Mathematics'),
        ('chemistry', 'Chemistry'),
        ('physics', 'Physics'),
        # Add more subjects as needed
    ]

    title = models.CharField(max_length=200)
    subject = models.CharField(max_length=100, choices=SUBJECT_CHOICES)
    file = models.FileField(upload_to='resources/')

    def __str__(self):
        return self.title




# Create your models here.
