from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.db.models import DateTimeField, Sum, Min, Max
from django.db.models.functions import Trunc

from .models import UserSummary


@admin.register(UserSummary)
class UserSummaryAdmin(ModelAdmin):
    change_list_template = 'admin/user_summary_change_list.html'
    date_hierarchy = 'date_joined'

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(
            request,
            extra_context=extra_context,
        )
        print()
        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response

        if 'date_joined__day' in request.GET:
            period_scale = 'hour'
            summary_over_time = qs.annotate(
                period=Trunc(
                    'date_joined',
                    'hour',
                    output_field=DateTimeField(),
                ),
            ).values('period').annotate(total=Sum('id')).order_by('period')
        else:
            period_scale = 'day'
            summary_over_time = qs.annotate(
                period=Trunc(
                    'date_joined',
                    'day',
                    output_field=DateTimeField(),
                ),
            ).values('period').annotate(total=Sum('id')).order_by('period')

        summary_range = summary_over_time.aggregate(
            low=Min('total'),
            high=Max('total'),
        )
        high = summary_range.get('high', 0)
        low = summary_range.get('low', 0)
        response.context_data['period_scale'] = period_scale
        response.context_data['summary_over_time'] = [{
            'period': x['period'],
            'total': x['total'] or 0,
            'pct': (((x['total'] or 0) - low) / (high - low) * 100
                    if high > low else 0),
        } for x in summary_over_time]

        return response
