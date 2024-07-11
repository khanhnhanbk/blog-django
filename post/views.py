from datetime import datetime

from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from .models import Post


def index(request):
    now = datetime.now()
    html = f"""
    <html>
        <body>
            <h1>Hello from Vercel!</h1>
            <p>The current time is { now }.</p>
        </body>
    </html>
    """
    return HttpResponse(html)


class PostListView(ListView):
    model = Post
    template_name = "post/index.html"
    context_object_name = "posts"
    ordering = ["-created_at"]
    paginate_by = 10


class PostDetailView(DetailView):
    model = Post
    template_name = "post/detail.html"
    context_object_name = "post"
    pk_url_kwarg = "pk"
