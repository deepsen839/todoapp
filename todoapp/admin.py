from django.contrib import admin
from .models import TodoModel
# Register your models here.
@admin.register(TodoModel)
class TodoAdmin(admin.ModelAdmin):
    class Meta:
        model = TodoModel    
    list_display = ('id','name','task_status')
