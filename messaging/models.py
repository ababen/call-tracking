from django.db import models

class Message(models.Model):
    from_number = models.CharField(max_length=9)
    to_number = models.CharField(max_length=9)
    message = models.CharField(max_length=255)

    def __str__(self):
        return str(self.message)
