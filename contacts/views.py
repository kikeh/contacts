from django.shortcuts import *
from django.http import HttpResponse

from contacts.models import *

from django.utils.text import slugify

def index(request):
    companies = Company.objects.all()
    categories = Category.objects.all()
    return render(request, 'contacts/index.html', { 'companies' : companies, 'categories' : categories })

def create_company(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        data = request.POST
        form = CreateCompany(data)
        if form.is_valid():
            company = form.save(commit=False)
            # Set slug and category
            # TODO: Check if slug is not already taken
            slug = slugify(data['name'])
            company.slug = slug
            category = get_category(data)
            company.category = category
            company.save()
            return redirect("index")
        else:
            return render(request, 'contacts/createCompany.html', { 'form' : form, 'categories' : categories })
    else:
        return render(request, 'contacts/createCompany.html', { 'categories' : categories })

def show_company(request, slug):
    company = Company.objects.get(slug=slug)
    return render(request, 'contacts/showCompany.html', { 'company' : company })

def edit_company(request, slug):
    categories = Category.objects.all()
    company = get_object_or_404(Company, slug=slug)
    if request.method == 'POST':
        data = request.POST
        form = CreateCompany(data or None, instance=company)
        if form.is_valid():
            # Set slug and category
            # TODO: Check if slug is not already taken
            slug = slugify(data['name'])
            company.slug = slug
            category = get_category(data)
            company.category = category
            company.save()
            return redirect("index")
        else:
            return render(request, 'contacts/createCompany.html', { 'form' : form, 'categories' : categories })
    return render(request, 'contacts/editCompany.html', { 'company' : company, 'categories' : categories })

def create_category(request):
    if request.method == 'POST':
        data = request.POST
        form = CreateCategory(data)
        if form.is_valid():
            category = form.save()
            return redirect("index")
        else:
            return render(request, 'contacts/createCategory.html', { 'error' : 'Could not save category %s' % form })
    else:
        return render(request, 'contacts/createCategory.html')
    
##
# Helper methods
##

def get_category(data):
    try:
        category_id = data['category'] if 'category' in data else None
        category = Category.objects.get(pk=category_id)
    except Category.DoesNotExist:
        return None
    return category
