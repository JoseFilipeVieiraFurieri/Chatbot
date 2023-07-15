from django.db import models

# chatblog/models.py

from django.db import models

class Statement(models.Model):
    text = models.TextField()
    in_response_to = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

