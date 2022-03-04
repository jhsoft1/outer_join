from django.urls import path

from polls import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('', Home.as_view(), name='home'),
    path('years/', views.YearListView.as_view(), name='years'),
    path('year/create/', views.YearCreate.as_view(), name='year-create'),
    path('year/<str:pk>', views.YearDetailView.as_view(), name='year-detail'),
    path('year/<str:pk>/update/', views.YearUpdate.as_view(), name='year-update'),
    path('year/<str:pk>/delete/', views.YearDelete.as_view(), name='year-delete'),
    path('votes/', views.VoteListView.as_view(), name='votes'),
    path('vote/create/', views.VoteCreate.as_view(), name='vote-create'),
    path('vote/create/<int:year>', views.VoteYearCreate.as_view(), name='vote-year-create'),
    path('vote/<int:pk>', views.VoteDetailView.as_view(), name='vote-detail'),
    path('vote/<int:pk>/update/', views.VoteUpdate.as_view(), name='vote-update'),
    path('vote/<int:pk>/update-value/', views.VoteValueUpdate.as_view(), name='vote-value-update'),
    path('vote/<int:pk>/delete/', views.VoteDelete.as_view(), name='vote-delete'),
    path('years-outer/', views.YearOuterListView.as_view(), name='years-outer'),
]
