from django.views.generic import TemplateView
from apps.blog.models import Post
from django.db.models import Count
from django.contrib.auth import get_user_model

CustomUser = get_user_model()
class HomePageView(TemplateView):
    """This template shows Home Page"""
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = Post.objects.all()
        context['posts'] = posts

        top_authors = (
            CustomUser.objects.annotate(post_count=Count('post'))
            .filter(post_count__gt=0)
            .order_by('-post_count')[:3]
        )

        context['top_authors'] = top_authors
        return context


