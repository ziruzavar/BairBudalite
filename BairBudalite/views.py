from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DeleteView

from BairBudalite.forms import CommentForm
from BairBudalite.models import Pohodi, Budali, Images, Comment
from budalite_authentication.models import UserProfile


class IndexView(ListView):
    template_name = 'index.html'
    model = Pohodi

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pohodi'] = Pohodi.objects.all().order_by('-id')[:3]
        context['budali'] = Budali.objects.all().order_by('-pohodi')[0:4]
        return context


class PohodiView(ListView):
    model = Pohodi
    template_name = 'generic.html'
    context_object_name = 'pohodi'


def elements(request):
    return render(request, 'elements.html')


def pohod(request, pk):
    images = Images.objects.filter(pohod=pk).all()
    pohod = Pohodi.objects.get(pk=pk)
    if request.method == "GET":
        context = {
            'pohod': pohod,
            'comment': Comment.objects.filter(pohod=pk).all(),
            'form': CommentForm(),
            'all': len(images),
            'images': {images[num]: num + 1 for num in range(0, len(images))},
        }
        return render(request, 'pohod.html', context)
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            all = form.cleaned_data
            comment = Comment(comment=all['comment'], pohod_id=pk, user_profile=UserProfile.objects.get(user_id=request.user.id))
            comment.save()
            return redirect('pohod', pk)
        else:
            context = {
                'pohod': pohod,
                'comment': Comment.objects.filter(pohod=pk).all(),
                'form': CommentForm(),
                'all': len(images),
                'images': {images[num]: num + 1 for num in range(0, len(images))},
            }
            return render(request, 'pohod.html', context)


class DeleteCommentView(View):
    def get(self, request, **kwargs):
        comment = Comment.objects.get(pk=kwargs['pk'])
        pohod_id = comment.pohod_id
        comment.delete()
        return redirect('pohod', pohod_id)


#def gallery(rq):
#    images = Images.objects.filter(pohod=1).all()
#   context = {
#       'all': len(images),
#       'images': {images[num]: num+1 for num in range(0,len(images))},
#   }
#   return render(rq, 'common/mooving_gallery.html', context)
