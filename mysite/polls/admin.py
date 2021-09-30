from django.contrib import admin

from .models import Choice, Question


# admin username: admin
# admin email: admin@gmail.com
# admin password: Adm!n123

admin.site.register(Choice)
admin.site.register(Question)