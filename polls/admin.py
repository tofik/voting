from polls.models import Poll, Choice
from django.contrib import admin

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3

class ChoiceAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,    {'fields': ['choice']}),
        ('Voted', {'fields': ['votes']}),
        ]
    list_display = ('choice', 'votes')
    list_filter = ['choice']
    search_fields = ['choice']

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
        ]
    inlines = [ChoiceInLine]
    list_display = ('question', 'pub_date', 'was_published_today')
    list_filter = ['pub_date']
    search_fields = ['question']
    date_hierarchy = 'pub_date'
    
admin.site.register(Poll, PollAdmin)
admin.site.register(Choice, ChoiceAdmin)
