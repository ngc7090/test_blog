from django import forms
from .models import Tag, Article, Comment


class RegistrationForm(forms.Form):
    username = forms.CharField(required=True, label='Имя',
                               max_length=40)
    email = forms.CharField(required=True, label='Email', max_length=40)
    password = forms.CharField(required=True, label='Пароль',
                               max_length=40, widget=forms.PasswordInput())


class ArticleCreateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'content', 'tags', 'image')

    title = forms.CharField(label="Заголовок")
    content = forms.CharField(label="Текст статьи", widget=forms.Textarea())
    tags = forms.ModelMultipleChoiceField(label="Теги", required=False,
                                          queryset=Tag.objects.all())


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text', )

    text = forms.CharField(label="Текст вашего комментария",
                           widget=forms.Textarea())
