from rest_framework import pagination


class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    page_size_query_param = 'per_page'
    max_page_size = 1000
