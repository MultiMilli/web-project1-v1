from django.shortcuts import render
from django.urls import reverse
from .models import Users
from .forms import UsersForm
from django.core.exceptions import ObjectDoesNotExist


def index(request):
    result = ''
    if request.method == 'POST':
        form = UsersForm(data=request.POST)
        if form.is_valid():
            name = request.POST['name']
            try:
                if Users.objects.get(name=name):
                    result = 'Вже бачилися, ' + name
            except ObjectDoesNotExist:
                form.save()
                result = 'Привіт, ' + name
            except Exception:
                result = 'Сталася помилка'

    form = UsersForm()

    context = {
        'form': form,
        'result': result,
    }
    return render(request, 'home/index.html', context)

def list(request):

    context = {
        'user': Users.objects.order_by('id'),
    }
    return render(request, 'home/list.html', context)