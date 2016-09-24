from django.shortcuts import render
from django.http import HttpResponse

from contacts.models import *

def index(request):
    companies = Company.objects.all()
    return render(request, 'contacts/index.html', { 'companies' : companies })

def create_company(request):
    if request.method == 'POST':
        form = CreateCompany(request.POST)
        if form.is_valid():
            company = form.save()
            return render_to_response("contacts/index.html", RequestContext(request))
    else:
        return render(request, 'contacts/createCompany.html')
