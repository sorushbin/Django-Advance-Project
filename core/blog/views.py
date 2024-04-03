# from typing import Any
# from django.db.models.query import QuerySet
# from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    RedirectView,
    ListView,
    DetailView,
    # FormView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Post

# Create your views here.
"""
this is a function view
def blog_view(request):
    return render(request, 'index.html')
"""


class BlogView(TemplateView):
    """
    this is a class based view
    """

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "ali"
        context["posts"] = Post.objects.all()
        return context


class RedirectToVarzeshView(RedirectView):
    """
    this is a redirect to varzesh3
    """

    # url = 'https://varzesh3.com/'
    pattern_name = "blog:cbv-index"


class PostListView(ListView):
    model = Post
    # queryset = Post.objects.filter(status = True)
    context_object_name = "posts"
    # paginate_by = 2
    ordering = "-id"

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(status=True)


class PostDetailView(DetailView):
    model = Post


"""
class PostFormView(FormView):
    template_name = 'post-form.html'
    form_class = PostForm
    success_url = '/blog/home-blog/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super().form_valid(form)
"""


class PostCreateView(CreateView):

    model = Post
    # fields =['title', 'content', 'status', 'published_date']
    form_class = PostForm
    success_url = "/blog/home-blog/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostEditView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ["title", "content"]
    success_url = "/blog/home-blog/"


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = "/blog/home-blog/"
