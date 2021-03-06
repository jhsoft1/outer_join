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

SELECT "polls_voter"."name", "polls_vote"."value" AS "value", "polls_vote"."year" AS "year" FROM "polls_voter"
LEFT OUTER JOIN "polls_vote" ON ("polls_voter"."id" = "polls_vote"."voter_id")
WHERE ("polls_vote"."year" = 2020 OR "polls_vote"."year" IS NULL)

from django.db.models import FilteredRelation
for v in Voter.objects.annotate(votes2020=FilteredRelation('vote', condition=Q(vote__year=2020))).values('name', 'votes2020__value', 'votes2020__year'):
    print(v)

SELECT "polls_voter"."name", votes2020."value", votes2020."year" FROM "polls_voter"
LEFT OUTER JOIN "polls_vote" votes2020 ON ("polls_voter"."id" = votes2020."voter_id" AND (votes2020."year" = 2020))