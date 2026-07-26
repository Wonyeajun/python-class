import random

from .models import CustomUser

ADJECTIVES = [
    "피곤한", "행복한", "배고픈", "졸린",
    "용감한", "귀여운", "신난", "조용한",
    "느긋한", "수줍은", "엉뚱한", "든든한"
]

ANIMALS = [
    "하이에나", "고양이", "강아지", "사자",
    "여우", "수달", "판다", "늑대",
    "참새", "호랑이", "부엉이", "돌고래"
]


def generate_nickname():
    while True:
        nickname = f"{random.choice(ADJECTIVES)} {random.choice(ANIMALS)}"

        if not CustomUser.objects.filter(nickname=nickname).exists():
            return nickname