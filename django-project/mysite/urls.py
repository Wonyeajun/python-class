from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('community.urls')),        # 메인(/) 접속 시 community 앱으로 바로 연결
    path('account/', include('account.urls')),
    path('tree/', include('tree.urls')),
]