from rest_framework import filters
from .models import *

class ObjektFilterBackend(filters.BaseFilterBackend):
    allowed_fields = ['job_title', 'company_name', 'web_company_jobs_id',]

    def filter_queryset(self, request, queryset, view):
        flt = {}
        for param in request.query_params:
            for fld in self.allowed_fields:
                if param.startswith(fld):
                    flt[param] = request.query_params[param]

        return queryset.filter(**flt)