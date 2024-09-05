from django.contrib import admin
from .models import Post
from .models import body_cons, Question, Choice

class PostAdmin(admin.ModelAdmin):
    list_display = ["email_id", "password", "created_at","updated_at"]

admin.site.register(Post, PostAdmin)

admin.site.register(body_cons)
admin.site.register(Question)
admin.site.register(Choice)
