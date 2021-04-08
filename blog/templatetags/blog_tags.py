from django import template
from ..models import Post

register = template.Library()

@register.inclusion_tag('blog/recent_posts.html')
def recent_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}

@register.inclusion_tag('blog/index_recent_posts.html')
def index_recent_posts(count=3):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}