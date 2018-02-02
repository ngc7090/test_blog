from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django import forms
from .forms import RegistrationForm, ArticleCreateForm, CommentCreateForm
from .models import Article


@login_required
def index_view(request):
    context = {'articles': Article.objects.all()}
    return render(request, 'user/index.html', context)


@login_required
def article_view(request, id):
    article = get_object_or_404(Article, id=id)
    if request.method == 'POST':
        form = CommentCreateForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.article = article
            comment = form.save()
    context = {'article': article, 'form': CommentCreateForm()}
    return render(request, 'user/article.html', context)


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form_user = form.cleaned_data
            username = form_user['username']
            email = form_user['email']
            password = form_user['password']
            if not (User.objects.filter(
                username=username).exists() or User.objects.filter(
                    email=email).exists()):
                User.objects.create_user(username, email, password)
                user = authenticate(username=username, password=password)
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                raise forms.ValidationError('Email или имя уже заняты.')
    else:
        form = RegistrationForm()
    return render(request, 'user/register.html', {'form': form})


@login_required
def create_view(request):
    if request.method == 'POST':
        form = ArticleCreateForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article = form.save()
            return HttpResponseRedirect(
                reverse_lazy('user:article', kwargs={'id': article.id}))
    else:
        form = ArticleCreateForm()
    return render(request, 'user/create.html', {'form': form})
