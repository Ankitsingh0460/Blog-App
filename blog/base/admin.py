from django.contrib import admin

# Register your models here.
from . models import Blog


admin.site.register(Blog)


admin.site.site_header="Ankit kumar singh"
admin.site.site_title="My Blog"
admin.site.index_title="Welcome to my blog"
