from django.contrib import admin
from .models import ListeningExam, ListeningQuestion, ListeningOption, ReadingExam, ReadingQuestion, ReadingBlank

class ListeningQuestionInline(admin.StackedInline):
    model = ListeningQuestion
    extra = 3

class ListeningExamAdmin(admin.ModelAdmin):
    inlines = [ListeningQuestionInline]

class ReadingQuestionInline(admin.StackedInline):
    model = ReadingQuestion
    extra = 3

class ReadingBlankInline(admin.StackedInline):
    model = ReadingBlank
    extra = 3

class ReadingQuestionAdmin(admin.ModelAdmin):
    inlines = [ReadingBlankInline]

admin.site.register(ListeningExam, ListeningExamAdmin)
admin.site.register(ReadingExam)
admin.site.register(ReadingQuestion, ReadingQuestionAdmin)
