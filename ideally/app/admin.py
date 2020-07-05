from django.contrib import admin

from .models import Idea, Tag


admin.site.register(Idea)
admin.site.register(Tag)
