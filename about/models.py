from django.db import models

# Create your models here.


class FAQ(models.Model):
    """
    Defines FAQs
    """

    question = models.CharField(max_length=254)
    answer = models.TextField()

    def __str__(self):
        return str(self.question)

    def get_friendly_name(self):
        return str(self.answer)