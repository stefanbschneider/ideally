from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

from .views import IndexView, IdeaDetail, IdeaCreate, IdeaUpdate, IdeaDelete, \
    TagIndex, TagDetail, TagCreate, TagUpdate, TagDelete, redirect_landing_page


app_name = 'app'

urlpatterns = [
    path('', include('pwa.urls')),  # You MUST use an empty string as the URL prefix
    path('', redirect_landing_page, name='redirect'),
    path('about/', TemplateView.as_view(template_name='app/about.html'), name='about'),

    # idea views
    path('idea/', IndexView.as_view(), name='index'),
    path('idea/<int:pk>/', IdeaDetail.as_view(), name='detail'),
    path('idea/add/', IdeaCreate.as_view(), name='add'),
    path('idea/<int:pk>/edit/', IdeaUpdate.as_view(), name='edit'),
    path('idea/<int:pk>/delete/', IdeaDelete.as_view(), name='delete'),

    # tag views
    path('tag/', TagIndex.as_view(), name='tag-index'),
    path('tag/<int:pk>/', TagDetail.as_view(), name='tag-detail'),
    path('tag/add/', TagCreate.as_view(), name='tag-add'),
    path('tag/<int:pk>/edit/', TagUpdate.as_view(), name='tag-edit'),
    path('tag/<int:pk>/delete/', TagDelete.as_view(), name='tag-delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
