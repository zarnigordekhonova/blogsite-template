from django.contrib.auth import get_user_model
from django.shortcuts import redirect, reverse
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView
from django.urls import reverse_lazy
from django.db.models import Count
from apps.blog.models import Category, Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

CustomUser = get_user_model()


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "blog/post_create.html"
    fields = ["title", 'content', 'category', 'image']
    success_url = reverse_lazy("home")
    login_url = reverse_lazy("users:login")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = "blog/post_update.html"
    fields = ["title", 'content', 'category', 'image']
    login_url = reverse_lazy("users:login")

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

    def get_success_url(self):
        post_slug = self.object.slug
        return reverse("blog:detail_post", kwargs={"slug": post_slug})


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context["debug_context"] = context.copy()
        return context


class PostDeleteView(DeleteView):
    model = Post
    template_name = "blog/post_delete.html"

    def get_success_url(self):
        return reverse_lazy("home")






