from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from .models import Post, Comment


def post_list(request):
    sort = request.GET.get('sort', 'recent')  # 기본값: 최신순
    q = request.GET.get('q', '').strip()

    posts = Post.objects.all()

    # 카테고리 라벨 <-> 코드 매핑 dictionary
    category_map = {name: code for code, name in Post.CATEGORY_CHOICES}

    # 검색어가 있을 경우 카테고리(키워드) 우선 검색
    if q:
        # 사용자가 입력한 검색어가 카테고리 이름(예: '연애', '친구')과 일치하는지 확인
        target_category = category_map.get(q)
        
        if target_category:
            # 선택한 키워드(카테고리) 기준으로만 필터링
            posts = posts.filter(category=target_category)
        else:
            # 카테고리 코드 직접 검색 또는 제목/내용 검색
            posts = posts.filter(
                Q(category__icontains=q) | 
                Q(title__icontains=q) | 
                Q(content__icontains=q)
            )

    # 정렬 조건
    if sort == 'comments':
        posts = posts.annotate(comment_cnt=Count('comments')).order_by('-comment_cnt', '-created_at')
    elif sort == 'reactions':
        posts = posts.annotate(
            total_rx=Count('likes', distinct=True) + Count('thumbs', distinct=True) + Count('sads', distinct=True)
        ).order_by('-total_rx', '-created_at')
    else:
        posts = posts.order_by('-created_at')

    return render(request, 'post_list.html', {
        'posts': posts,
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
            comment = Comment(
                post=post,
                author=request.user,
                content=content
            )
            comment.save()

    return redirect("post_detail", pk=pk)


@login_required
def post_like(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return redirect("post_detail", pk=pk)


@login_required
def post_thumb(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user in post.thumbs.all():
        post.thumbs.remove(request.user)
    else:
        post.thumbs.add(request.user)
    return redirect('post_detail', pk=pk)


@login_required
def post_sad(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user in post.sads.all():
        post.sads.remove(request.user)
    else:
        post.sads.add(request.user)
    return redirect('post_detail', pk=pk)