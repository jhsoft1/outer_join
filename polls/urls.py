from django.urls import path

from polls import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('', Home.as_view(), name='home'),
    path('voters/', views.VoterListView.as_view(), name='voters'),
    path('voter/create/', views.VoterCreate.as_view(), name='voter-create'),
    path('voter/<str:pk>', views.VoterDetailView.as_view(), name='voter-detail'),
    path('voter/<str:pk>/update/', views.VoterUpdate.as_view(), name='voter-update'),
    path('voter/<str:pk>/delete/', views.VoterDelete.as_view(), name='voter-delete'),
    path('votes/', views.VoteListView.as_view(), name='votes'),
    path('vote/create/', views.VoteCreate.as_view(), name='vote-create'),
    path('vote/<int:pk>', views.VoteDetailView.as_view(), name='vote-detail'),
    path('vote/<int:pk>/update/', views.VoteUpdate.as_view(), name='vote-update'),
    path('vote/<int:pk>/delete/', views.VoteDelete.as_view(), name='vote-delete'),
    path('voters-outer/', views.VoterOuterListView.as_view(), name='voters-outer'),
]
