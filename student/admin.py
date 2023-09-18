from django.contrib import admin
from . models import *
from .resource import ReportResource  
from import_export.admin import ImportExportModelAdmin
from django.utils.translation import gettext_lazy as _
from datetime import datetime
from rangefilter.filters import (
    DateRangeFilterBuilder,
    DateTimeRangeFilterBuilder,
    NumericRangeFilterBuilder,
    DateRangeQuickSelectListFilterBuilder,
)

# @admin.register(Post)
class StudentAdmin(admin.ModelAdmin):
    list_filter = (
        ("created", DateRangeFilterBuilder()),
        (
            "updated",
            DateTimeRangeFilterBuilder(
                title="Custom title",
                default_start=datetime(2020, 1, 1),
                default_end=datetime(2030, 1, 1),
            ),
        ),
        ("Name", NumericRangeFilterBuilder()),
        ("created", DateRangeQuickSelectListFilterBuilder()),  # Range + QuickSelect Filter
    )

# Register your models here.

class ReportAdmin(ImportExportModelAdmin):
     resource_class = ReportResource 

class MyStudent(Student):
    class Meta:
        proxy = True


admin.site.register(MyStudent,ReportAdmin)
admin.site.register(Student,StudentAdmin)
# admin.site.register(CourseCategory)
admin.site.register(Courses)
admin.site.register(Fees_Payment)
admin.site.register(Fees_Show)
admin.site.register(Enquries)
admin.site.register(Transaction)
admin.site.register(Account)