#models.py 안의 blog 클래스를 기반으로 입력공간을 만들 것이기 때문에 같은 폴더인 blogapp 에 만들엇음

from django import forms
from .models import Blog

class BlogPost(forms.ModelForm): #임의의 form을 만들고 싶으면 forms.Form
    class Meta:
        model = Blog #blog 기반으로 만들건데
        fields = ['title', 'body'] #이 두가지를 입력 받게 할것이다!
        #처리함수는 views.py