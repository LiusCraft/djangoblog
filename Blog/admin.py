from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Catagory)
admin.site.register(Article)
admin.site.register(Link)