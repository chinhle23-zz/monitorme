from __future__ import unicode_literals

from django import template
from core.models import User, TrackerGroup, TrackerGroupInstance, Question, Answer, Response
from django.contrib.auth.models import Group
from django.db.models import Avg, Count
from datetime import datetime, date
from dateutil.relativedelta import relativedelta


register = template.Library()

 
@register.simple_tag
def currentMonthCount(pk, user):
    today = date.today()
    current_instances = TrackerGroupInstance.objects.filter(started_at__month=today.month, tracker_id=pk, created_by=user).count()
    return current_instances

@register.simple_tag
def thirtyDayCount(pk, user):
    last_month = datetime.today() + relativedelta(days=-30)
    thirtyday_instances = TrackerGroupInstance.objects.filter(started_at__date__gte=last_month, tracker_id=pk, created_by=user).count()
    return thirtyday_instances

@register.simple_tag
def averageOfDays(pk, user):
    last_month = datetime.today() + relativedelta(days=-30)

    count_of_instances = TrackerGroupInstance.objects.filter(started_at__date__gte=last_month, tracker_id=pk, created_by=user).count()

    all_per_month = TrackerGroupInstance.objects.filter(started_at__date__gte=last_month, created_by=user).count()

    try:
        average_of_instances = round(float(float(count_of_instances)/float(all_per_month)* 100.00), 1)
        return average_of_instances
    except:
        return int(0)


@register.filter(answer='been_clicked')
def been_clicked(answer, trackergroupinstance):

    try:
        responses = Response.objects.filter(tracker_instance=trackergroupinstance).filter(answers__id=answer.pk).exists()
       
        if responses:
            status = True
            return status
    except:
        return False

