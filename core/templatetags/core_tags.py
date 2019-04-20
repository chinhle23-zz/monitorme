from __future__ import unicode_literals

from django import template
from core.models import User, TrackerGroup, TrackerGroupInstance, Question, Answer, Response
from django.contrib.auth.models import Group


register = template.Library()

 


