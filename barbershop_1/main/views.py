from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .models import *
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView

def index(request):
    data = {
        'title': 'ПАРИКМАХЕРСКАЯ <7 ЖЕЛАНИЙ>',
        'values': ['Парикмахерский зал', 'Маникюр', 'Педикюр'],
    }
    return render(request, 'main/index.html', data)


def services(request):
    data = {
        'title': 'ПАРИКМАХЕРСКАЯ <7 ЖЕЛАНИЙ>',
        'values': ['Короткие волосы: 13,00', 'Средние волосы: 18,00', 'Длинные волосы: 23,00'],
        'values_1': ['стрижка простая, наголо (с использованием 1 насадки): 7,00', 'модельная стрижка: 10,00', 'креативная стрижка (каре,шапочка,ирокез,шейвер и др.): 13,00']
    }
    return render(request, 'main/services.html', data)

def contacts(request):
    form = userForm()
    data = {
        'title': 'ПАРИКМАХЕРСКАЯ <7 ЖЕЛАНИЙ>',
        'values': ['8 017 263-84-39', '8 029 342-94-61', 'Минск, ул. Янки Лучины, 8'],
        'form': form,
    }
    return render(request, 'main/contacts.html', data)

# def indexPage(CreateView):
#     if CreateView.method == 'POST':
#         user = User()
#         user.name = CreateView.POST.get('name')
#         user.email = CreateView.POST.get('email')
#         user.phone = CreateView.POST.get('phone')
#         user.save()
#         return HttpResponse(f'<h1>Hello {user.name} ur email is {user.email}, phone is {user.phone}</h1>')
#     else:
#         form = userForm()
#         return render(CreateView, "contacts.html", {'form': form})

def indexPage(request):
    if request.method == 'POST':
        user = User()
        user.name = request.POST.get('name')
        user.email = request.POST.get('email')
        user.phone = request.POST.get('phone')
        user.save()
        return HttpResponse(f'<h1>Hello {user.name} ur email is {user.email}, phone is {user.phone}</h1>')
    else:
        form = userForm()
        return render(request, "contacts.html", {'form': form})

def services_for_women(request):
    servicesForWomen = ServicesForWomen.objects.all()
    return render(request, 'main/services_for_women.html', {'servicesForWomen': servicesForWomen})

def services_for_men(request):
    servicesForMen = ServicesForWomen.objects.all()
    return render(request, 'main/services_for_men.html', {'servicesForMen': servicesForMen})

def services_for_children(request):
    servicesForChildren = ServicesForChildren.objects.all()
    return render(request, 'main/services_for_children.html', {'servicesForChildren': servicesForChildren})

def manicure_pedicure(request):
    manicurePedicure = ManicurePedicure.objects.all()
    return render(request, 'main/manicure_pedicure.html', {'manicurePedicure': manicurePedicure})

def cosmetology_services(request):
    cosmetologyServices = CosmetologyServices.objects.all()
    return render(request, 'main/cosmetology_services.html', {'cosmetologyServices': cosmetologyServices})

def gift_certificates(request):
    giftCertificates = GiftCertificates.objects.all()
    return render(request, 'main/gift_certificates.html', {'giftCertificates': giftCertificates})





