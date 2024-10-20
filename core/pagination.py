from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django.utils.translation import gettext_lazy as _
from rest_framework.settings import api_settings
from django.core.paginator import Paginator as DjangoPaginator

class CustomPageNumberPagination(PageNumberPagination):
    """
    A custom page number-based pagination style that includes the page number in the response.
    """
    # The default page size.
    page_size = api_settings.PAGE_SIZE

    django_paginator_class = DjangoPaginator

    # Client can control the page using this query parameter.
    page_query_param = 'page'
    page_query_description = _('A page number within the paginated result set.')

    # Client can control the page size using this query parameter.
    page_size_query_param = 'page_size'
    page_size_query_description = _('Number of results to return per page.')

    # Set to an integer to limit the maximum page size the client may request.
    max_page_size = 100

    last_page_strings = ('last',)

    template = 'rest_framework/pagination/numbers.html'

    invalid_page_message = _('Invalid page.')

    def get_paginated_response(self, data):
        return Response({
            'page': self.page.number,  # Add current page number here
            'total_pages': self.page.paginator.num_pages,
            'total_results': self.page.paginator.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data
        })
