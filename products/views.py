from django.shortcuts import render
import sqlalchemy, sqlalchemy.orm
from .models import Base, Products, session
from django.http import HttpResponseRedirect
import factory
from sqlalchemy import orm

from algoliasearch.search_client import SearchClient
from algolia import settings

# For algolia data upload
client = SearchClient.create('<APPLICATION_ID>', '<API_KEY>')
index = client.init_index('products')

# Home page
def productList(request):
    rows = session.query(Products).count()
    products = session.query(Products).all()
    context = {
        'products':products,
        'rows':rows
    }
    return render(request, 'product-list.html', context)

# add the product and redirect to product list page
def productAdd(request):
    if request.method == 'POST':
        if request.POST:
            name = request.POST.get('name')
            model_number = request.POST.get('model-number')
            character = request.POST.get('character')
            brand = request.POST.get('brand')
            description = request.POST.get('description')
            product = Products(request.POST.get('name'), request.POST.get('model_number'), request.POST.get('character'), request.POST.get('brand'), request.POST.get('description'))
            session.add(product)
            session.commit()

            # save to algolia
            product = {'name': name, 'model_number': model_number, 'character': character, 'brand': brand, 'description': description}
            index.save_object(product, {'autoGenerateObjectIDIfNotExist': bool})
            return HttpResponseRedirect('/')
    else:
        print('well shit')

    context = {

    }
    return render(request, 'product-add.html', context)


def productSearch(request):
    context = {
        'appID': settings.ALGOLIA['APPLICATION_ID'],
        'searchKey': settings.ALGOLIA['API_KEY'],
        'indexName': 'products',
    }
    return render(request, 'search.html', context)


