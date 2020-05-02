from django.db import models


class ContactRequest(models.Model):
    CHOICES = (
            ('yes', 'Yes'),
               ('no', 'No')
               )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    answer = models.CharField(max_length=3,
                              choices=CHOICES,
                              default=CHOICES[0])
    message = models.CharField(max_length=255, null=True)
    email = models.EmailField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'Message from {self.first_name}'
