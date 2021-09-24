import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Company
from recipeapp.models import UserModel
from .forms import CompanyForm


@login_required(login_url='/login')
def create_company(request):
    user = UserModel.objects.get(username=request.user)
    company_details = Company.objects.filter(user=request.user)
    if company_details.count() > 1:
        many_companies = True
    else:
        many_companies = False
    company_name = request.session.get('company_name')
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            company_detail = form.save(commit=False)
            company_detail.user = request.user
            company_detail.save()
            print(company_detail.name)
            request.session['company_name'] = company_detail.name
            return redirect('/company/edit')
        else:
            return render(
                request,
                'company_new.html',
                {
                    'form': form,
                    'username': user.username,
                    'email': user.email,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'many_companies': many_companies,
                    'company_details': company_details,
                    'company_name': company_name,
                    'fail': 'Invalid Data'
                }
            )
    else:
        form = CompanyForm()
        return render(
            request,
            'company_new.html',
            {
                'form': form,
                'username': user.username,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'many_companies': many_companies,
                'company_details': company_details,
                'company_name': company_name,
            }
        )


@login_required(login_url='/login')
def save_company_name(request):
    if request.method == 'POST':
        name = request.POST.get('valueSelected')
        print(name)
        request.session['company_name'] = name
        return HttpResponse(json.dumps({'status': 'ok'}), content_type='application/json')


@login_required(login_url='/login')
def edit_company(request):
    user = UserModel.objects.get(username=request.user)
    company_details = Company.objects.filter(user=request.user)
    if company_details.count() > 1:
        many_companies = True
    else:
        many_companies = False
    company_name = request.session.get('company_name')
    company_detail = Company.objects.get(user=request.user, name=company_name)
    if request.method == 'POST':
        form = CompanyForm(instance=company_detail, data=request.POST)
        if form.is_valid():
            form.save()
            request.session['company_name'] = company_detail.name
            return render(
                request,
                'company_info.html',
                {
                    'form': form,
                    'username': user.username,
                    'email': user.email,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'many_companies': many_companies,
                    'company_details': company_details,
                    'company_name': company_name,
                }
            )
    else:
        form = CompanyForm(instance=company_detail)
        return render(
            request,
            'company_info.html',
            {
                'form': form,
                'username': user.username,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'many_companies': many_companies,
                'company_details': company_details,
                'company_name': company_name,
            }
        )


@login_required(login_url='/login')
def company_settings(request):
    user = UserModel.objects.get(username=request.user)
    company_details = Company.objects.filter(user=request.user)
    if company_details.count() > 1:
        many_companies = True
    else:
        many_companies = False
    company_name = request.session.get('company_name')
    return render(
        request,
        'company_settings.html',
        {
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'many_companies': many_companies,
            'company_details': company_details,
            'company_name': company_name,
        }
    )
