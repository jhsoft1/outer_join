from django.db import models


class Voter(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Vote(models.Model):
    value = models.CharField(max_length=100)
    voter = models.ForeignKey(Voter, on_delete=models.CASCADE)
    year = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.value} {str(self.voter)} {str(self.year)}'
