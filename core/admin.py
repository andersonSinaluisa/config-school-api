from django.contrib import admin
from .models import SectionModel, ClassScheduleModel, SectionBreakModel
# Register your models here.
admin.site.register(SectionModel)
admin.site.register(ClassScheduleModel)
admin.site.register(SectionBreakModel)
