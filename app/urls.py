from django.urls import path

from .views import IndexView, IdeaDetail, IdeaCreate, IdeaUpdate, IdeaDelete, \
    TagIndex, TagDetail, TagCreate, TagUpdate, TagDelete


app_name = 'app'

urlpatterns = [
    # idea views
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/', IdeaDetail.as_view(), name='detail'),
    path('add/', IdeaCreate.as_view(), name='add'),
    path('<int:pk>/edit/', IdeaUpdate.as_view(), name='edit'),
    path('<int:pk>/delete/', IdeaDelete.as_view(), name='delete'),

    # tag views
    path('tag/', TagIndex.as_view(), name='tag-index'),
    path('tag/<int:pk>/', TagDetail.as_view(), name='tag-detail'),
    path('tag/add/', TagCreate.as_view(), name='tag-add'),
    path('tag/<int:pk>/edit/', TagUpdate.as_view(), name='tag-edit'),
    path('tag/<int:pk>/delete/', TagDelete.as_view(), name='tag-delete'),
]
