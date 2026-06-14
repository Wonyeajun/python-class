from django.shortcuts import render, redirect

# 기존 더미 유저 목록
DUMMY_USERS = [
    {"username": "student1", "password": "password123", "nickname": "익명_숲속의토끼"},
    {"username": "student2", "password": "password456", "nickname": "익명_지친댕댕이"},
]

def dummy_login(request):
    if request.method == "POST":
        user_id = request.POST.get('username')
        user_pw = request.POST.get('password')

        # 더미 유저 목록 돌면서 일치하는 회원이 있는지 검사
        for user in DUMMY_USERS:
            if user['username'] == user_id and user['password'] == user_pw:
                # 일치하면 브라우저 세션에 로그인 상태를 기록
                request.session['user_nickname'] = user['nickname']
                request.session['is_authenticated'] = True
                return redirect('index') # 로그인 성공 시 메인(index) 페이지로 강제 이동
        
        # 로그인 실패 시 에러 메시지와 함께 다시 로그인 창 띄우기
        return render(request, 'login.html', {'error': '아이디 또는 비밀번호가 틀렸어요!'})
        
    return render(request, 'login.html')


def dummy_logout(request):
    request.session.flush() # 세션에 저장된 로그인 정보 완전히 지우기
    return redirect('index') # 로그아웃 후 메인 페이지로 돌아가기


# ================= 새로 추가된 회원가입 함수 =================
def dummy_signup(request):
    if request.method == "POST":
        user_id = request.POST.get('username')
        user_pw = request.POST.get('password')
        user_nickname = request.POST.get('nickname') # 닉네임 입력값 가져오기

        # [안전장치 1] 아이디 중복 검사
        for user in DUMMY_USERS:
            if user['username'] == user_id:
                return render(request, 'signup.html', {'error': '이미 존재하는 아이디입니다!'})

        # [안전장치 2] 빈칸이 있는지 검사
        if not user_id or not user_pw or not user_nickname:
            return render(request, 'signup.html', {'error': '모든 항목을 입력해 주세요!'})

        # 다 통과했다면 더미 유저 리스트에 딕셔너리 형태로 추가!
        new_user = {
            "username": user_id,
            "password": user_pw,
            "nickname": user_nickname
        }
        DUMMY_USERS.append(new_user)

        # 가입 성공 후 바로 로그인 상태로 만들어주기 (선택 사항)
        request.session['user_nickname'] = new_user['nickname']
        request.session['is_authenticated'] = True
        
        return redirect('index') # 가입 완료 후 메인 페이지로 이동

    return render(request, 'signup.html')