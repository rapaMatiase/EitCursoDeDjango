from posixpath import join
from django.contrib import admin
from .models import Theme, Journalist, News, Images
# Register your models here.

admin.site.register(Theme)
admin.site.register(Journalist)
admin.site.register(News)
admin.site.register(Images)
