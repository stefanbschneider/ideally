from django.contrib import admin

from .models import Idea, Tag, Milestone


admin.site.register(Idea)
admin.site.register(Tag)
admin.site.register(Milestone)
