from django import forms
from django.utils.html import escape
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CommentsModel


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class MyUserCreationForm(UserCreationForm):
    username = forms.CharField()
    email = forms.CharField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def save(self, commit=True):
        user = super(MyUserCreationForm, self).save(commit=False)
        if commit:
            user.save()
        return user


class CommentsForm(forms.ModelForm):
    class Meta:
        model = CommentsModel
        fields = ['data_comments', 'text_comments']
        widgets = {'post_id': forms.HiddenInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Налаштовуємо вигляд полів форми (необов'язково)
        # self.fields['user'].widget = forms.HiddenInput()  # автоматично встановити користувача з об'єкта запиту
        self.fields['data_comments'].widget = forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT'
                                                                                                           '%H:%M')

    def clean_text_comments(self):
        # Очищаємо text_comments від HTML-тегів
        text_comments = self.cleaned_data.get('text_comments')
        return escape(text_comments)
