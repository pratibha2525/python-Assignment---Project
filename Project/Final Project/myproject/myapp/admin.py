from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Chairman)
admin.site.register(Member)
admin.site.register(watchman)
admin.site.register(visitor)
admin.site.register(Notice)
admin.site.register(Notice_view)
admin.site.register(Event)
