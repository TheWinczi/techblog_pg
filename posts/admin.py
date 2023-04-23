from django.contrib import admin
from django.forms import TextInput
from django.db import models as fields
from django.utils.translation import gettext as _

from posts.models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    formfield_overrides = {
        fields.CharField: {'widget': TextInput(attrs={'size': '100'})},
    }

    fieldsets = [
        (_('General'), {'fields': ['author', 'title', 'content']}),
        (_('Dates'), {'fields': ['created_at', 'updated_at']})
    ]
    list_display = ('title', 'author', 'created_at')
    list_filter = ('author', 'created_at')
    search_fields = ('author', 'title', 'content')
    ordering = ('created_at',)


class CommentAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    formfield_overrides = {
        fields.CharField: {'widget': TextInput(attrs={'size': '50'})},
    }

    fieldsets = [
        (_('General'), {'fields': ['post', 'author', 'content']}),
        (_('Dates'), {'fields': ['created_at']}),
    ]
    list_display = ('content', 'post_title', 'author', 'created_at')
    list_filter = ('author', 'created_at')
    search_fields = ('author', 'content')
    ordering = ('created_at',)

    def post_title(self, comment: Comment):
        return comment.post.title
    post_title.short_description = _('Post Title')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
