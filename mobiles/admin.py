# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin


from .models import Devices,DeviceDetails

admin.site.register(DeviceDetails)

admin.site.register(Devices)
