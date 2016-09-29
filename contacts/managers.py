from django.db import models


class CompanyManager(models.Manager):
    def getCompanies(self, order_by='name'):
        return super(CompanyManager, self).get_queryset().extra(order_by=[order_by])

class CategoryManager(models.Manager):
    def getCategories(self, order_by='name'):
        return super(CategoryManager, self).get_queryset().extra(order_by=[order_by])
