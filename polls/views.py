from django.db.models import F, FilteredRelation, Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from polls.models import Voter, Vote


class VoterListView(ListView):
    model = Voter


class VoterCreate(CreateView):
    model = Voter
    fields = '__all__'


class VoterDetailView(DetailView):
    model = Voter


class VoterUpdate(UpdateView):
    model = Voter
    fields = '__all__'


class VoterDelete(DeleteView):
    model = Voter
    success_url = reverse_lazy('voters')


class VoteListView(ListView):
    model = Vote


class VoterOuterListView(ListView):
    model = Voter

    # queryset = Voter.objects.annotate(value=F('vote__value'), year=F('vote__year')).values('name', 'value', 'year')
    # queryset = Voter.objects.annotate(value=F('vote__value'), year=F('vote__year')).values().filter(name=user)
    def get_queryset(self):
        # return Voter.objects.annotate(value=F('vote__value'), year=F('vote__year')).values().filter(name=self.request.user)
        return Voter.objects.annotate(votes2020=FilteredRelation(
            'vote', condition=Q(vote__year=2020))).values('name', 'votes2020__value', 'votes2020__year')


class VoteCreate(CreateView):
    model = Vote
    fields = '__all__'


class VoteDetailView(DetailView):
    model = Vote


class VoteUpdate(UpdateView):
    model = Vote
    fields = '__all__'


class VoteDelete(DeleteView):
    model = Vote
    success_url = reverse_lazy('votes')


def index(request):
    """View function for home page of site."""

    # Generate counts of some main objects
    num_voters = Voter.objects.count()
    num_votes = Vote.objects.all().count()
    if request.user.is_authenticated:
        num_my_votes = Vote.objects.filter(voter__name=request.user).count()
    else:
        num_my_votes = 'We give whisky only to our friends :)'

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    context = {
        'num_voters': num_voters,
        'num_votes': num_votes,
        'num_visits': num_visits,
        'num_my_votes': num_my_votes,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
