# -*- coding: utf-8 -*-
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tw.spec.prod.settings")

from tw.wsgi import application