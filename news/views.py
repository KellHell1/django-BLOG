from django.shortcuts import render, redirect
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from django.views.generic import UpdateView, DeleteView, TemplateView


def news_home(request):
    news = Article.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news': news})


class NewsTemplateView(TemplateView):
    template_name = 'news/details_view.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['form'] = CommentForm()
        context['comments'] = Comment.objects.filter(post_id=self.kwargs.get('pk', None))
        news = Article.objects.filter(id = self.kwargs.get('pk', None))
        news_values = news.values()
        context['news_title'] = news_values[0]['title']
        context['anons'] = news_values[0]['anons']
        context['full_text'] = news_values[0]['full_text']
        context['date'] = news_values[0]['date']

        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        news_pk = self.kwargs.get('pk', None)
        form = CommentForm(self.request.POST)

        post = Article.objects.get(id=self.kwargs.get('pk', None))
        form.instance.post = post

        if form.is_valid():
            form_update = form.save(commit=False)
            form_update.save()
            return redirect('/')


class NewsUpdateView(UpdateView):
    model = Article
    template_name = 'news/create.html'
    form_class = ArticleForm


class NewsDeleteView(DeleteView):
    model = Article
    template_name = 'news/news-delete.html'
    form_class = ArticleForm
    success_url = '/news/'


def create(request):
    error = ''
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "Форма была неверной"

    form = ArticleForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'news/create.html', data)

