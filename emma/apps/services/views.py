#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from django.views.generic import TemplateView, View, FormView

from emma.apps.services.forms import ServiceData
from emma.apps.services.models import Service, Workshop
from emma.apps.xauth.views import SignupView
from emma.core.mixins import RequestFormMixin


class ContractServiceInfo(View):
    template_name = 'services/contract_service_info.html'
    services = Service.objects.all()
    success_url = reverse_lazy('services:contract_signup')

    def get(self, request):
        '''
        if 'id_service' in request.session:
            del request.session['id_service']
        if 'id_workshop' in request.session:
            del request.session['id_workshop']

        if 'workshop_list' in request.session:
            del request.session['workshop_list']
        '''

        ctx = {
            'services': self.services
        }
        return TemplateResponse(request, self.template_name, ctx)

    def post(self, request):
        service_id = request.POST.get('contract-service')
        workshop_list = request.POST.getlist('contract-service-workshop')
        ctx = {
            'services': self.services
        }
        try:
            service = self.services.get(id=service_id)
            for workshop in workshop_list:
                Workshop.objects.get(id=workshop, service=service)
            request.session['id_service'] = service_id
            request.session['workshop_list'] = workshop_list
            return redirect(self.success_url)

        except Service.DoesNotExist:
            error = 'Ocurrio un error, intente de nuevo'
            ctx.update({
                'error': error,
            })
            return render(request, self.template_name, ctx)
        except Workshop.DoesNotExist:
            error = 'Ocurrio un error, intente de nuevo'
            ctx.update({
                'error': error,
            })
            return render(request, self.template_name, ctx)


class ContractSignup(SignupView):
    template_name = 'services/contract_signup.html'
    success_url = reverse_lazy('services:contract_ubication')

    def get(self, request, **kwargs):
        if not 'id_service' in request.session or \
                not 'workshop_list' in request.session :
            return redirect('services:contract_service_info')
        else:
            return super(ContractSignup, self).get(self, request, **kwargs)


class ContractLocation(RequestFormMixin, FormView):
    template_name = 'services/contract_location.html'
    form_class = ServiceData
    success_url = reverse_lazy('services:contract_adult')

    def form_valid(self, form):
        form.save()
        return super(ContractLocation, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ContractLocation, self).get_context_data(**kwargs)
        service = Service.objects.get(
            id=self.request.session['id_service']
        )

        workshop_list = self.request.session['workshop_list']
        workshops = ''
        for workshop in workshop_list:
            work = Workshop.objects.get(id=workshop, service=service)
            workshops += '%s, ' % str(work.name)
        workshops = workshops[:-2]
        context['service'] = service
        context['workshop'] = workshops
        return context


class ContractAdult(TemplateView):
    template_name = 'services/contract_adult.html'

class ContractPay(TemplateView):
    template_name = 'services/contract_payment.html'
