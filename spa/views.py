from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from spa.forms import LoginForm, MyUserCreationForm, CommentsForm
from spa.models import PostModel, CommentsModel


@login_required
def create_comment(request):
    if request.user.is_authenticated:
        posts = PostModel.objects.all()
        comments = CommentsModel.objects.all()

        if request.method == 'POST':
            form = CommentsForm(request.POST)
            if form.is_valid():
                # Отримуємо post_id та user_id з POST-запиту, не через cleaned_data
                post_id = request.POST['post_id']
                user_id = request.POST['user_id']

                # Збереження коментара у базу даних, передавши post_id та user_id
                comment = form.save(commit=False)
                comment.post_id = post_id
                comment.user_id = user_id
                comment.save()

                return redirect('/')
        else:
            form = CommentsForm()

        return render(request, 'spa/post.html', {'form': form, 'posts': posts, 'comments': comments})
    else:
        return redirect('/login')


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'spa/login.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = MyUserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/login')
    else:
        form = MyUserCreationForm()

    return render(request, 'spa/signup.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/login')
