from __future__ import unicode_literals

from django import template
from core.models import User, TrackerGroup, TrackerGroupInstance, Question, Answer, Response
from django.contrib.auth.models import Group


register = template.Library()

 
# @register.simple_tag
# def currentMonthCount(pk)
#     today = date.today()
#     current_instances = TrackerGroupInstance.objects.filter(started_at__month=today.month, tracker_id=tracker.pk).count()
#     return month_count

# @register.simple_tag
# def thirtyDayCount(pk)
#     last_month = datetime.today() + relativedelta(days=-30)
#     thirtyday_instances = TrackerGroupInstance.objects.filter(started_at__date__gte=last_month, tracker_id=tracker.pk)
