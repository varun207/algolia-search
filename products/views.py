from django.shortcuts import render
import sqlalchemy, sqlalchemy.orm
from .models import Base, Products, session
from django.http import HttpResponseRedirect
import factory
from sqlalchemy import orm

from algoliasearch.search_client import SearchClient
from algolia import settings


# sqlalchemy session
# engine = sqlalchemy.create_engine('sqlite:///loose.sqlite')
# Session = sqlalchemy.orm.sessionmaker(bind=engine)
# session = Session()
# Base.metadata.create_all(engine)

# For algolia data upload
client = SearchClient.create('5MOBI7FV78', '7a2c03f64a54f740cea34a137587a887')
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

# # function to upload data to algolia
# def fetch_data_from_database(request):
#     products = session.query(Products).all()
#     index.save_objects(products,  {'autoGenerateObjectIDIfNotExist': True})
#     return render(request, 'demo.html', {'products':products })




# convert sqlalchemy object to list of dicts
# productList = []
    # for product in products:
    #     print(product.name)
    #     _product = {}
    #     _product['name'] = str(product.name)
    #     _product['model_number'] = str(product.model_number)
    #     _product['character'] = str(product.character)
    #     _product['brand'] = str(product.brand)
    #     _product['description'] = str(product.description)
    #     productList.append(_product)

# index.save_objects(productList, {'autoGenerateObjectIDIfNotExist': True})

# Function to fill data
# def is_empty():
#     return len(session.query(Products).all()) <= 0
#
# def populate():
#     new_products = [Products('something', '12345', 'batman', 'apple', 'The best product'),
#                     Products('something else', '45678', 'spider-Waman', 'Next', '9 year old army')]
#     session.add_all(new_products)
#     session.commit()


# Function to add data
# def runseeder(request):
#     for entry in range(1000):
#         fake_name = fakegen.name()
#         fake_model = fakegen.isbn10(separator="-")
#         fake_character = fakegen.first_name()
#         fake_company = fakegen.company()
#         fake_description = fakegen.sentence(nb_words=15, variable_nb_words=True, ext_word_list=None)

#         product = Products(name=fake_name,
#             model_number=fake_model,
#             character=fake_character,
#             brand=fake_company,
#             description=fake_description,
#         )
#         session.add(product)
#         session.commit()

#     return render(request, 'demo.html')
