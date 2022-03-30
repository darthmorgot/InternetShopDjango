from django.shortcuts import render


def index(request):
    context = {
        'title': 'ВелоСам',
    }
    return render(request, 'products/index.html', context=context)
