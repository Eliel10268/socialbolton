from django.shortcuts import render, redirect
from .models import Post
from authentification.models import Account
from .forms import AddNewPost

# Create your views here.
def posts_view(request):
    try:
        account_id = request.session["logged_in_account_id"]
        account = Account.objects.get(id=account_id)
        print(account, account_id)

        posts = Post.objects.order_by("-id").all()

        return render(request, "posts.html", {"posts": posts, "username": account.fullname})
    except KeyError:
        return redirect('/auth/login')


def add_new_post_view(request):
    try:
        account_id = request.session["logged_in_account_id"]
        account = Account.objects.get(id=account_id)
        print(account, account_id)
        form = AddNewPost()

        if request.method == 'POST':
            form = AddNewPost(request.POST)
            if form.is_valid():
                post_text = form.cleaned_data['text']
                Post.objects.create(
                    author=account,
                    content=post_text
                )

                return redirect('/posts')
            


        
        return render(request, "add_post.html", {"form": form})
    except KeyError:
        return redirect('/auth/login')