# -*- coding: utf-8 -*-
# Reference: http://www.zhidaow.com/post/django-custom-template-tag-markdown

import markdown2
import markdown

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(is_safe=True)
@stringfilter
def cslzy_markdown(value):
    extensions = ["codehilite","nl2br", "tables", "fenced_code", "codehilite(css_class=highlight)", "toc", "sane_lists"]
    return mark_safe(
             markdown.markdown(
             force_unicode(value),
             extensions,
             safe_mode=True,
             enable_attributes=False)
                     )
