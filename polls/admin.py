from django.contrib import admin
from .models import Question
from .models import Choice

# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
