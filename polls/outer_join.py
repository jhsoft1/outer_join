from polls.models import *
from django.db.models import F

juan = Voter.objects.create(name='Juan')
gustavo = Voter.objects.create(name='Gustavo')
kelian = Voter.objects.create(name='Kelian')
micaela = Voter.objects.create(name='Micaela')

Vote.objects.create(voter=Voter.objects.get(name='Juan'), value='C++', year=2019)
Vote.objects.create(voter=Voter.objects.get(name='Juan'), value='Javascript', year=2020)
Vote.objects.create(voter=Voter.objects.get(name='Gustavo'), value='Javascript', year=2020)
Vote.objects.create(voter=Voter.objects.get(name='Kelian'), value='C#', year=2019)

for v in Voter.objects.annotate(value=F('vote__value'), year=F('vote__year')).values('name', 'value', 'year'):
    print(v)

for v in Voter.objects.annotate(value=F('vote__value'), year=F('vote__year')).values('name', 'value', 'year').filter(year=2020):
    print(v)

from django.db.models import Q
for v in Voter.objects.annotate(value=F('vote__value'), year=F('vote__year')).values('name', 'value', 'year').filter(Q(year=2020) | Q(year__isnull=True)):
    print(v)

from django.db.models import FilteredRelation
for v in Voter.objects.annotate(votes2020=FilteredRelation('vote', condition=Q(vote__year=2020))).values('name', 'votes2020__value', 'votes2020__year'):
    print(v)