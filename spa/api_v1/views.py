from datetime import timedelta

from django.http import HttpResponse
from django.template import loader, RequestContext
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import *
from django.views.generic import TemplateView
import urllib.parse


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    lookup_field = 'url'
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('title',)

    def get_queryset(self):
        dataset = Event.objects

        email = urllib.parse.unquote(self.request.COOKIES.get('email', ''))
        dataset = dataset.filter(email=email)

        date_filter = self.request.GET.get('dateFilter', default=False)
        if date_filter == 'ld':
            dataset = dataset.filter(date__range=[datetime.datetime.now() - timedelta(days=1), datetime.datetime.now()])
        elif date_filter == 'lw':
            dataset = dataset.filter(date__range=[datetime.datetime.now() - timedelta(days=7), datetime.datetime.now()])
        elif date_filter == 'lm':
            dataset = dataset.filter(
                date__range=[datetime.datetime.now() - timedelta(days=30), datetime.datetime.now()])

        return dataset

    def get_serializer_class(self):
        if self.action == 'list':
            return EventPreviewSerializer
        return EventDetailSerializer


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}))
