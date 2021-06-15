from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View

from charity.models import Donation, Institution


class IndexView(View):
    def get(self, request):
        fundations = Institution.objects.filter(type=1).order_by('name')
        fund_paginator = Paginator(fundations, 5)
        fund_page_num = request.GET.get('page')
        fund_page = fund_paginator.get_page(fund_page_num)

        ngos = Institution.objects.filter(type=2).order_by('name')
        ngos_paginator = Paginator(ngos, 5)
        ngos_page_num = request.GET.get('page')
        ngos_page = ngos_paginator.get_page(ngos_page_num)

        charity_events = Institution.objects.filter(type=3).order_by('name')
        charity_paginator = Paginator(charity_events, 5)
        charity_page_num = request.GET.get('page')
        charity_page = charity_paginator.get_page(charity_page_num)

        donations = Donation.objects.all()
        bags = 0
        for element in donations:
            bags += element.quantity
        return render(request, 'index.html', {'bags': bags, 'donations': donations, 'charity_pages': charity_page,
                                              'fund_pages': fund_page,
                                              'ngos_pages': ngos_page})


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')


class AddDonationView(View):
    def get(self, request):
        return render(request, 'form.html')
