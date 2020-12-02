from django.shortcuts import render, redirect
from django.views.generic import ListView

from BairBudalite.forms import CommentForm
from BairBudalite.models import Pohodi, Budali, Images, Comment


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
            comment = Comment(comment=all['comment'], pohod_id=pk)
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


#def gallery(rq):
#    images = Images.objects.filter(pohod=1).all()
#   context = {
#       'all': len(images),
#       'images': {images[num]: num+1 for num in range(0,len(images))},
#   }
#   return render(rq, 'common/mooving_gallery.html', context)
