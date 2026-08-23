from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import SignupForm
from .nickname import generate_nickname


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.nickname = generate_nickname()
            user.save()

            login(request, user)
            return redirect("post_list")

    else:
        form = SignupForm()

    return render(
        request,
        "signup.html",
        {
            "form": form
        }
    )


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("post_list")

        return render(
            request,
            "login.html",
            {
                "error": "아이디 또는 비밀번호가 올바르지 않습니다."
            }
        )

    return render(request, "login.html")


def user_logout(request):
    logout(request)
    return redirect("post_list")

@login_required
def mypage(request):
    # 로그인된 유저가 작성한 글과 댓글 가져오기
    user_posts = request.user.post_set.all().order_by("-created_at")
    user_comments = request.user.comment_set.all().order_by("-created_at")

    return render(
        request,
        "mypage.html",
        {
            "user": request.user,
            "posts": user_posts,
            "comments": user_comments,
        },
    )