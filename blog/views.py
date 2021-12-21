from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic import View, DetailView, ListView
from django.views.generic.edit import CreateView, FormMixin

from .forms import CommentCreateForm
from .models import *


class ArticlesList(ListView):
    model = Article
    template_name = 'blog/blogs.html'
    queryset = model.objects.filter(is_active=True)
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super(ArticlesList, self).get_context_data(**kwargs)
        context["title"] = "Все новости и стати"
        return context

class ArticleDetail(DetailView, FormMixin):
    model = Article
    form_class = CommentCreateForm
    template_name = 'blog/blog.html'
    slug_field = 'slug'
    
    def get_context_data(self, **kwargs):
        context = super(ArticleDetail, self).get_context_data(**kwargs)
        context["title"] = self.model.title
        context["tags"] = Tag.objects.all()
        context["popular_news"] = Article.objects.filter(is_active=True)[:3]
        context["recent_news"] = Article.objects.order_by("published_date").filter(is_active=True)[:3]
        return context
    # Переопределяем метод post чтобы форма записалась в бд
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.article = self.get_object() 
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self, **kwargs) -> str:
        return reverse_lazy("blog", kwargs={"slug": self.get_object().slug})







