import django_filters
from .models import *

class BloodgroupFilter(django_filters.FilterSet):
    class Meta:
        model = AcceptDonorList
        fields = ['d_bloodgroup','d_gender']