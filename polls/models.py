from django.contrib.auth.models import User
from django.db import models
from django.db.models import UniqueConstraint
from django.urls import reverse


class Voter(models.Model):
    name = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('voter-detail', args=[str(self.pk)])


class Year(models.Model):
    vote_year = models.IntegerField(primary_key=True)

    def __str__(self):
        return str(self.vote_year)

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('year-detail', args=[str(self.pk)])


class Vote(models.Model):
    value = models.CharField(max_length=100)
    voter = models.ForeignKey(User, on_delete=models.CASCADE)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)

    class Meta:
        constraints = [UniqueConstraint(fields=['voter', 'year'], name='voter_year')]

    def __str__(self):
        return f'{self.value} {self.voter} {self.year}'

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('vote-detail', args=[str(self.id)])
