from datetime import datetime

import django_filters
from django import forms

from room.models import Room, Book, TYPE


class RoomFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='exact')
    type = django_filters.ChoiceFilter(choices=TYPE)

    class Meta:
        model = Room
        fields = []


class RoomBookingFilter(django_filters.FilterSet):
    resident = django_filters.CharFilter(field_name='resident__name', lookup_expr='exact')
    room = django_filters.CharFilter(field_name='room__name', lookup_expr='exact')
    start = django_filters.CharFilter(field_name='start', lookup_expr='exact')
    end = django_filters.CharFilter(field_name='end', lookup_expr='exact')

    class Meta:
        model = Book
        fields = []
