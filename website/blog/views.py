from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .forms import EmailPostForm
from django.core.mail import send_mail
from django import forms

def index(request):
    return render(request, "blog/base.html")


def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        slug=post,
        status="published",
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )
    return render(request, "blog/post/detail.html", {"post": post})


def post_list(request):
    object_list = Post.published.all()
    paginator = Paginator(object_list, 3)
    page = request.GET.get("page")
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, "blog/post/list.html", {"page": page, "posts": posts})


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = "posts"
    paginate_by = 3
    template_name = "blog/post/list.html"

def post_share(request, post_id):
    # Retrieve post by id
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False

    if request.method == 'POST':
        # Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = '{} ({}) recommends you reading "{}"'.format(cd['name'], cd['email'], post.title)
            message = 'Read "{}" at {}\n\n{}\'s comments: {}'.format(post.title, post_url, cd['name'], cd['comments'])
            send_mail(subject, message, 'admin@myblog.com', [cd['to']])
            sent = True
    else:
        form = EmailPostForm()

    return render(request, 'blog/post/share.html', {'post': post, 'form': form, 'sent': sent})
    
# def post_share(request, post_id):
#     post = get_object_or_404(Post, id=post_id)
#     sent = False
#     form = EmailPostForm()  # Initialize the form here

#     if request.method == "POST":
#         form = EmailPostForm(request.POST)  # Reinitialize with POST data
#         if form.is_valid():
#             # Send the email (implement your email sending logic)
#             cd = form.cleaned_data
#             subject = f"{cd['name']} recommends you read '{post.title}'"
#             message = f"Read '{post.title}' at http://127.0.0.1:8000{post.get_absolute_url()}\n\nComments: {cd['comments']}"
#             send_mail(subject, message, 'your_email@example.com', [cd['to']])  # Replace with your sender email
#             sent = True
#             return redirect(post.get_absolute_url())  # Redirect to post detail page
#     # If GET request or form is invalid, render the form
#     return render(request, "blog/post/share.html", {"form": form, "post": post, "sent": sent})