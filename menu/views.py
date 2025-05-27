from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return  render(request, 'menu/base.html')
def about(request):
    return  render(request, 'menu/about.html')
def blog(request):
    return  render(request, 'menu/blog.html')
def contact(request):
    return  render(request, 'menu/contact.html')

def home(request):
    context = {
        'jina': 'Bongoclass',
        'muda': 4,
        'domain': 'bongoclass.com',
        'course': 'Python - Django',
        'gharama': 'SHILINGI 30,000',
        'room': 'online',
    }
    return render(request, 'menu/home.html', context)
def fomu_view(request):
    if request.method == 'POST':
        jina = request.POST.get('jina')
        ujumbe = request.POST.get('ujumbe')

        if jina and ujumbe:
            context = {
                'jina': jina,
                'ujumbe': ujumbe,
            }
            return render(request, 'menu/taarifa.html', context)
        else:
            return render(request, 'menu/fomu.html', {'error': 'Tafadhali jaza mashamba yote.'})

    return render(request, 'menu/fomu.html')