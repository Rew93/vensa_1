from django.shortcuts import render

from app1.forms import TextForm


# Create your views here.

def index(request):
    if request.method == 'GET':
        form = TextForm(request.GET)
    else:
        form = TextForm()
    context = {'form': form}
    return render(request, 'app1/index.html', context)


def rev(request):
    user_text = request.GET['text']
    context = {'usertext': user_text,
               'rev_user_text': user_text[::-1]}
    return render(request, 'app1/rev.html', context)
