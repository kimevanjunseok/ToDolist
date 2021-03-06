from django.contrib import admin
from myapp.home.models import Boards

# Register your models here.
class BoardAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'priority', 'created_at', 'finished_at',)

admin.site.register(Boards, BoardAdmin)
