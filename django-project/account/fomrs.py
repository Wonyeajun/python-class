from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class SignupForm(UserCreationForm):
    nickname = forms.CharField(
            max_length=50, 
            widget=forms.TextInput(attrs={'placeholder': '사용할 익명 닉네임 (예: 익명_신난고양이)'}),
            label="닉네임"
        )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('nickname',)