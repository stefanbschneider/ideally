from django.urls import path

from .views import IndexView, DetailView, IdeaCreate, IdeaUpdate, IdeaDelete


app_name = 'app'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/', DetailView.as_view(), name='detail'),
    path('add/', IdeaCreate.as_view(), name='add'),
    path('<int:pk>/edit/', IdeaUpdate.as_view(), name='edit'),
    path('<int:pk>/delete/', IdeaDelete.as_view(), name='delete'),
]
