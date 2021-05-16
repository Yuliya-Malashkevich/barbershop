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
        'values': ['Короткие волосы: 13,00 руб.', 'Средние волосы: 18,00 руб.', 'Длинные волосы: 23,00 руб.'],
        'values_1': ['Cтрижка простая, наголо (с использованием 1 насадки): 7,00 руб.', 'Mодельная стрижка: 10,00 руб.', 'Kреативная стрижка (каре,шапочка,ирокез,шейвер и др.): 13,00 руб'],
        'values_2': ['Mодельная стрижка 5,50 руб.'],
        'values_3': ['МАНИКЮР КЛАССИЧЕСКИЙ (снятие лака, придание формы ногтям, обработка кутикулы, легкий массаж, салфетка) 10,00 руб.', 'КОМПЛЕКСНЫЙ МАНИКЮР (снятие лака, придание формы ногтям, обработка кутикулы, легкий массаж, полное покрытие, масло, салфетка) 16,00 руб.'],
        'values_4': ['ЖЕНСКИЙ ПЕДИКЮР от 14,50 руб.', 'МУЖСКОЙ ПЕДИКЮР от 17,50 руб.'],
    }
    return render(request, 'main/services.html', data)

def contacts(request):
    form = userForm()
    data = {
        'title': 'ПАРИКМАХЕРСКАЯ <7 ЖЕЛАНИЙ>',
        'values': ['8 017 263-84-39', '8 029 342-94-61', 'Минск, ул. Янки Лучины, 8'],
        "form": form,
    }
    if request.method == 'POST':
        user = User()
        user.name = request.POST.get('name')
        user.email = request.POST.get('email')
        user.phone = request.POST.get('phone')
        user.save()
        return HttpResponse(f'<h1>Hello {user.name} ur email is {user.email}, phone is {user.phone}</h1>')
    else:
        form = userForm()
        return render(request, "main/contacts.html", data)


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
    servicesForMen = ServicesForMen.objects.all()
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





