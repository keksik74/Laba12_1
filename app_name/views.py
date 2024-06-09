from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import Post


def post_list(request):
    posts = Post.objects.all()
    return render(request, "post_list.html", {"posts": posts})


def post_create(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        Post.objects.create(title=title, content=content)
        return redirect("post_list")
    return render(request, "post_create.html")


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.title = request.POST["title"]
        post.content = request.POST["content"]
        post.save()
        return redirect("post_list")
    return render(request, "post_edit.html", {"post": post})


def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect("post_list")
    return render(request, "post_delete.html", {"post": post})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("post_list")
        messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})


def register_view(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Registration successful. You can now log in."
            )
            return redirect("login")
    else:
        form = UserRegistrationForm()
    return render(request, "register.html", {"form": form})