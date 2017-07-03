# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
import os
from os import listdir
from os.path import isfile, join
this_dir = os.path.dirname(os.path.abspath(__file__))
onlyfiles = [f for f in listdir(this_dir) if isfile(join(this_dir, f))]

TEMPLATES = {
    'page.html': _('page.html'),
}#Makes page.html come first, and this it's the default.

keys = TEMPLATES.keys()
TEMPLATES.update({f: _(f) for f in onlyfiles if f.endswith('.html') and f not in keys})

