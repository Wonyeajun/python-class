from django.shortcuts import render


# ==========================================
# 2. 메인 페이지 뷰 (기존 index 함수를 확장)
# ==========================================
def index(request):
    # 좌측 사이드바에 들어갈 '인기글' 더미 데이터
    popular_stories = [
        {"id": 1, "category": "인간관계", "title": "자꾸 눈치 보게 되는 친구가 있어요.."},
        {"id": 2, "category": "학업/진로", "title": "이번 시험 망쳤는데 위로해주세요 ㅠㅠ"},
        {"id": 3, "category": "연애", "title": "좋아하는 애한테 익명으로 쪽지 보내는 법"},
        {"id": 4, "category": "가족", "title": "부모님이랑 말다툼했는데 먼저 사과하는 팁"},
    ]

    # 중앙 피드에 들어갈 '메인 사연' 더미 데이터
    main_stories = [
        {
            "id": 10,
            "category": "친구관계",
            "title": "친구랑 사소한 걸로 오해가 생겼는데 어떻게 풀죠?",
            "preview": "말 한마디 잘못했다가 분위기가 서먹해졌어요. 장난이었는데 친구는 진지하게 받아들인 것 같아요. 내일 학교에서 직접 말하는 게 나을까요?",
            "author": "익명_숲속의토끼",
            "comments": 18,
            "likes": 32,
        },
        {
            "id": 11,
            "category": "공부·학업",
            "title": "슬럼프가 온 것 같아요. 아무것도 손에 안 잡히네요.",
            "preview": "독서실에 앉아는 있는데 집중이 하나도 안 되고 계속 멍 때리게 돼요. 다른 친구들은 다 열심히 달리고 있는 것 같아서 불안감만 커지는데 어쩌죠.",
            "author": "익명_지친댕댕이",
            "comments": 14,
            "likes": 28,
        },
        {
            "id": 12,
            "category": "연애",
            "title": "짝사랑하는 애가 있는데 포기해야 할까요?",
            "preview": "같은 동아리 지인인데 친해지기는 했거든요? 근데 상대방은 저를 그냥 편한 동료로만 생각하는 것 같아서 마음이 아파요.",
            "author": "익명_수줍은사자",
            "comments": 22,
            "likes": 25,
        }
    ]

    # 사용자의 임시 로그인 상태 확인 (세션 데이터 읽기)
    # 로그인을 안 했다면 기본값으로 '익명_방문자'와 False를 가져옵니다.
    current_user_nickname = request.session.get('user_nickname', '익명_방문자')
    is_authenticated = request.session.get('is_authenticated', False)

    # HTML 템플릿으로 보낼 데이터 묶기
    context = {
        'popular_stories': popular_stories,
        'main_stories': main_stories,
        'user_nickname': current_user_nickname,
        'is_authenticated': is_authenticated,
    }
    
    # render할 때 두 번째 인자가 index.html이므로, 
    # 지난번에 만든 메인 페이지 html 파일명이 index.html이어야 연동됩니다!
    return render(request, 'index.html', context)


