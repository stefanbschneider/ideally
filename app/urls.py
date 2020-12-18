from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

from . import views


app_name = 'app'

urlpatterns = [
    path('', include('pwa.urls')),  # You MUST use an empty string as the URL prefix
    path('', views.redirect_landing_page, name='redirect'),
    path('about/', TemplateView.as_view(template_name='app/about.html'), name='about'),

    # idea views
    path('idea/', views.IndexView.as_view(), name='index'),
    path('idea/<int:pk>/', views.IdeaDetail.as_view(), name='detail'),
    path('idea/add/', views.add_idea, name='add'),
    path('idea/<int:pk>/edit/', views.IdeaUpdate.as_view(), name='edit'),
    path('idea/<int:pk>/delete/', views.IdeaDelete.as_view(), name='delete'),
    # note views
    path('idea/<int:pk_idea>/note/add/', views.add_note, name='add-note'),
    path('idea/<int:pk_idea>/note/<int:pk_note>', views.edit_note, name='edit-note'),

    # tag views
    path('tag/', views.TagIndex.as_view(), name='tag-index'),
    path('tag/<int:pk>/', views.TagDetail.as_view(), name='tag-detail'),
    path('tag/add/', views.TagCreate.as_view(), name='tag-add'),
    path('tag/<int:pk>/edit/', views.TagUpdate.as_view(), name='tag-edit'),
    path('tag/<int:pk>/delete/', views.TagDelete.as_view(), name='tag-delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
