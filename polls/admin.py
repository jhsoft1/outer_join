from django.contrib import admin

from polls.models import Voter, Vote

admin.site.register(Voter)
admin.site.register(Vote)
