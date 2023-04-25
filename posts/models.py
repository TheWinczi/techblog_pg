import os
import random

from django.db import models
from django.utils.translation import gettext_lazy as _


def post_image_upload(instance, filename):
    id = ''.join(str(random.randint(0, 9)) for _ in range(10))
    return os.path.join('posts', id, 'images', 'postImage')


class Post(models.Model):
    CONTENT_MAX_LENGTH = 5000
    TITLE_MAX_LENGTH = 500

    content = models.TextField(verbose_name=_('Content'), max_length=CONTENT_MAX_LENGTH)
    title = models.CharField(verbose_name=_('Title'), blank=False, max_length=TITLE_MAX_LENGTH)
    author = models.ForeignKey('accounts.CustomUser', rel='posts', verbose_name=_('Author'), on_delete=models.CASCADE)
    image = models.ImageField(verbose_name=_('Image'), upload_to=post_image_upload, blank=False)

    created_at = models.DateTimeField(verbose_name=_('Created At'), auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_('Updated At'), auto_now=True)

    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')

    def __str__(self):
        return f'{self.author} | {self.title}'

    def __repr__(self):
        return f'Post(content={self.content}, author={self.author})'


class Comment(models.Model):
    CONTENT_MAX_LENGTH = 500

    content = models.TextField(verbose_name=_('Content'), max_length=CONTENT_MAX_LENGTH)
    post = models.ForeignKey(Post, verbose_name=_('Post'), rel='comments', null=False, blank=False, on_delete=models.CASCADE)
    author = models.ForeignKey('accounts.CustomUser', rel='comments', verbose_name=_('Author'), on_delete=models.CASCADE)

    created_at = models.DateTimeField(verbose_name=_('Created At'), auto_now_add=True)

    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')

    def __str__(self):
        return f'{self.author} | POST[{self.post}]'

    def __repr__(self):
        return f'Comment(content={self.content}, post={self.post}, author={self.author})'
