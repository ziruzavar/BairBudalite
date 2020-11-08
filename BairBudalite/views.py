from django.shortcuts import render, redirect

from BairBudalite.forms import CommentForm
from BairBudalite.models import Pohodi, Budali, Images, Comment


def index(request):
    context = {
        'pohodi': Pohodi.objects.all().order_by('-id')[:3],
        'budali': Budali.objects.all().order_by('pohodi')[:4:-1],
    }
    return render(request, 'index.html', context)


def pohodi(request):
    context = {
        'pohodi': Pohodi.objects.all()
    }
    return render(request, 'generic.html', context)


def elements(request):
    return render(request, 'elements.html')


def pohod(request, pk):
    pohod = Pohodi.objects.get(pk=pk)
    if request.method == "GET":
        context = {
            'pohod': pohod,
            'images': Images.objects.filter(pohod=pk).all(),
            'comment': Comment.objects.filter(pohod=pk).all(),
            'form': CommentForm()
        }
        return render(request, 'pohod.html', context)
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            all = form.cleaned_data
            comment = Comment(comment=all['comment'], pohod_id=pk)
            comment.save()
            return redirect('pohod', pk)
        else:
            context = {
                'pohod': pohod,
                'images': Images.objects.filter(pohod=pk).all(),
                'comment': Comment.objects.filter(pohod=pk).all(),
                'form': CommentForm()
            }
            return render(request, 'pohod.html', context)
