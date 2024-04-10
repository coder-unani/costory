from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "placeholder": "제목을 입력하세요.",
                }
            ),
            "content": forms.Textarea(
                attrs={
                    "placeholder": "내용을 입력하세요.",
                }
            ),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if '*' in title:
            raise forms.ValidationError("'*'는 포함할 수 없습니다.")
        return title
        # fields = "__all__"
    
