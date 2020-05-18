from rest_framework.pagination import PageNumberPagination

class EbooksPaginations(PageNumberPagination):
    page_size = 3
    page_query_param = 'pagina'
    