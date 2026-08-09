from django.contrib.auth.decorators import login_required
# get_object_or_404 추가
from django.shortcuts import render, redirect, get_object_or_404

from .models import Post, Comment


def post_list(request):
    posts = Post.objects.all().order_by("-created_at")
    return render(request, "post_list.html", {
        "posts": posts
    })


@login_required
def post_create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")

        Post.objects.create(
            author=request.user,
            title=title,
            content=content
        )

        return redirect("post_list")

    return render(request, "post_create.html")

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "post_detail.html", {
        "post": post
    })

@login_required
def comment_create(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        content = request.POST.get("content")

        if content:
            Comment.objects.create(
                post=post,
                author=request.user,
                content=content
            )

    return redirect("post_detail", pk=pk)

@login_required
def post_like(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # 이미 공감을 눌렀다면 취소, 안 눌렀다면 추가
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return redirect("post_detail", pk=pk)