from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(null=True, blank=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)

    class Meta:
        ordering = ['first_name']
        verbose_name = u'pessoa'
        verbose_name_plural = u'pessoas'

    def __str__(self):
        return self.first_name + " " + self.last_name

    full_name = property(__str__)
