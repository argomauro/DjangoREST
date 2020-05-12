from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from products.models import Product, Manufacturer
from django.http import JsonResponse

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    
class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'

def product_list(request):
    products = Product.objects.all()[:30]
    data = {'products':list(products.values())}
    response = JsonResponse(data)
    return response

def manufacturer_list(request):
    manufacturers = Manufacturer.objects.all()[:30]
    data = {'manufacturers':list(manufacturers.values())}
    response = JsonResponse(data)
    return response

def manufacturer_detail(request, pk):
    try:
        manufacturer = Manufacturer.objects.get(pk=pk)
        #con la chiamata di sotto prendo i riferimenti tramite
        #related_name
        manufacturer_products = manufacturer.products.all()
        #con la chiamata di sotto prendo i riferimenti tramite
        #un filtro con chiave primaria ed id
        products = Product.objects.filter(manufacturer_id=manufacturer.pk)
        data = {'manufacturer': {
            'name': manufacturer.name,
            'location': manufacturer.location,
            #'products': list(manufacturer_products.values()),
            'products': list(products.values()),
            }
        }
        response = JsonResponse(data)
    except Manufacturer.DoesNotExist:
        response = JsonResponse({
            'error':{
                'code': 404,
                'message': 'Manufacturer non trovato'
            }
        }, status = 404)
            
    return response

def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        data = {'product': {
            'name': product.name,
            'manufacturer': product.manufacturer.name,
            'description':product.description,
            }
        }
        response = JsonResponse(data)
    except Product.DoesNotExist:
        response = JsonResponse({
            'error':{
                'code': 404,
                'message': 'prodotto non trovato'
            }
        }, status = 404)
            
    return response