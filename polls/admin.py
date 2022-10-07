from django.contrib import admin

from .models import Question, Choice

admin.site.site_header = "Zayne's Pollster Admin"
admin.site.site_title = "Zayne's Pollster Admin Area"
admin.site.index_title = "Welcome to Zayne's Pollster Admin Area"

# Register your models here.

# We want choices within questions admin screen
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

# we will use this instead of choice, to allow us to show choices on ques 
# screen (otherwise it would show on it's own screen and not be 'attached' 
# to ques admin screen)
class QuestionAdmin(admin.ModelAdmin):
    # explicitly show ques options
    fieldsets = [(None, {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date'], 'classes':
        ['collapse']}),]
    # pull choice scr into admin scr
    inlines = [ChoiceInline]

# admin.site.register(Question)
# admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)