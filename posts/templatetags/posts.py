from django import template

register = template.Library()


@register.filter
def short_content(post, max_len: int = 500):
    return post.content[:max_len] + '...'


@register.filter
def datetime_term(post):
    return post.created_at.strftime("%Y-%m-%d")
