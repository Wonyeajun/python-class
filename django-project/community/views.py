from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from django.http import JsonResponse
from .models import Post, Comment


def post_list(request):
    sort = request.GET.get('sort', 'recent')
    q = request.GET.get('q', '').strip()

    posts = Post.objects.all()

    # hot_score 계산 (distinct=True 제거 -> 각 반응 종류별 개수가 개별로 합산됨)
    hot_post = Post.objects.annotate(
        hot_score=Count('likes') + Count('thumbs') + Count('sads')
    ).order_by('-hot_score', '-created_at').first()

    # 카테고리 매핑
    category_map = {name: code for code, name in Post.CATEGORY_CHOICES}

    # 드롭다운 선택 필터링
    if q:
        target_category = category_map.get(q, q)
        posts = posts.filter(
            Q(category=target_category) | 
            Q(category__icontains=q)
        )

    # 정렬
    if sort == 'comments':
        posts = posts.annotate(comment_cnt=Count('comments')).order_by('-comment_cnt', '-created_at')
    elif sort == 'reactions':
        # 반응순 정렬 시에도 distinct=True 제거
        posts = posts.annotate(
            total_rx=Count('likes') + Count('thumbs') + Count('sads')
        ).order_by('-total_rx', '-created_at')
    else:
        posts = posts.order_by('-created_at')

    return render(request, 'post_list.html', {
        'posts': posts,
        'hot_post': hot_post,
        'sort': sort,
        'q': q,
        'categories': Post.CATEGORY_CHOICES,
    })


@login_required
def post_create(request):
    if request.method == "POST":
        category = request.POST.get("category", "etc")
        title = request.POST.get("title")
        content = request.POST.get("content")

        Post.objects.create(
            author=request.user,
            category=category,
            title=title,
            content=content
        )
        return redirect("post_list")

    return render(request, "post_create.html", {
        "categories": Post.CATEGORY_CHOICES
    })


# 비로그인 유저 접근 제한
@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "post_detail.html", {
        "post": post
    })


@login_required
def comment_create(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        content = request.POST.get("content", "").strip()

        if content:
            comment = Comment.objects.create(
                post=post,
                author=request.user,
                content=content
            )
            nickname = request.user.nickname if hasattr(request.user, 'nickname') and request.user.nickname else request.user.username
            
            return JsonResponse({
                "status": "success",
                "author": nickname,
                "created_at": comment.created_at.strftime("%Y-%m-%d %H:%M"),
                "content": comment.content,
                "total_comments": post.comments.count()
            })

    return JsonResponse({"status": "error"}, status=400)


@login_required
def post_like(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        active = False
    else:
        post.likes.add(request.user)
        active = True

    return JsonResponse({
        "count": post.likes.count(),
        "active": active
    })


@login_required
def post_thumb(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.user in post.thumbs.all():
        post.thumbs.remove(request.user)
        active = False
    else:
        post.thumbs.add(request.user)
        active = True

    return JsonResponse({
        "count": post.thumbs.count(),
        "active": active
    })


@login_required
def post_sad(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.user in post.sads.all():
        post.sads.remove(request.user)
        active = False
    else:
        post.sads.add(request.user)
        active = True

    return JsonResponse({
        "count": post.sads.count(),
        "active": active
    })