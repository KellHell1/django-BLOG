from .models import Article, Comment
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'anons', 'full_text', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи'
            }),
            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс статьи'
            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи'
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации',
                'type': 'datetime-local'
            })
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваше имя'
            }),

            'body': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваш комментарий'
            })
        }
