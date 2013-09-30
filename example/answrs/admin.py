from django.contrib import admin

from answrs.models import UserProfile, Category, Question, Answer

admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(Question)
admin.site.register(Answer)
