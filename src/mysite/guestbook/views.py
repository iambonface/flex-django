from django.shortcuts import render, redirect
from . models import Comment
from . forms import CommentForm
# Create your views here.
def index(request):
    comments = Comment.objects.order_by('-created')

    context = {'comments': comments}

    return render(request, 'guestbook/index.html', context )

def sign(request):

    if request.method == 'POST':
        form  = CommentForm(request.POST)

        if form.is_valid():
            valid_comment = Comment(name=request.POST['name'], comment=request.POST['comment'])
            valid_comment.save()
            return redirect('index')

    else:
        form = CommentForm()

    context = {'form': form}

    return render(request, 'guestbook/sign.html', context)