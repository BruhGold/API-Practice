from django.contrib import admin
from .models import Choice, Question

class QuestionAdmin(admin.ModelAdmin):
    autocomplete_fields = ['authors']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)