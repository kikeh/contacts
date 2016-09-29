from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm
from contacts import managers

class Company(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    category = models.ForeignKey('Category', null = True)

    objects = managers.CompanyManager()

class Contact(models.Model):
    name = models.CharField(
        max_length = 200,
        blank = True
    )
    phone = models.CharField(
        max_length = 50,
        blank = True
    )
    email = models.EmailField(
        blank = True
    )
    comments = models.TextField(
        blank = True
    )

class Communication(models.Model):
    PHONE = 0
    EMAIL = 1
    IN_PERSON = 2
    ONLINE = 3

    COMMUNICATION_TYPES = (
        (PHONE, 'phone'),
        (EMAIL, 'email'),
        (IN_PERSON, 'in_person'),
        (ONLINE, 'online')
    )

    communication_type = models.IntegerField()
    contact = models.ManyToManyField('Contact')
    date = models.DateTimeField()
    comments = models.TextField()
    meeting = models.OneToOneField('Meeting')

class Proposal(models.Model):
    INCOMPLETE = 0
    DELIVERED = 1
    ACCEPTED = 2
    NOT_ACCEPTED = 3

    PROPOSAL_STATUS = (
        (INCOMPLETE, 'incomplete'),
        (DELIVERED, 'delivered'),
        (ACCEPTED, 'accepted'),
        (NOT_ACCEPTED, 'not_accepted')
    )
    
    date = models.DateTimeField()
    contact = models.ManyToManyField('Contact')
    status = models.IntegerField()

class Meeting(models.Model):
    date = models.DateTimeField()
    contact = models.ManyToManyField('Contact')
    location = models.CharField(max_length=300)
    comments = models.TextField()
    proposal = models.ManyToManyField('Proposal')
    
class Category(models.Model):
    name = models.CharField(max_length=50)

    objects = managers.CategoryManager()

    def __str__(self):
        return self.name

#########
# FORMS #
#########

class CreateCompany(ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'category']

    def clean_category(self):
        category = self.cleaned_data['category'] if 'category' in self.cleaned_data else None
        if not category:
            raise ValidationError('No category was selected')
        return category

class CreateCategory(ModelForm):
    class Meta:
        model = Category
        fields = ['name']
