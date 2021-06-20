from django.contrib import admin
from .models import Projects
from .models import Tasks

admin.site.register(Tasks)
admin.site.register(Projects)
# Register your models here.
