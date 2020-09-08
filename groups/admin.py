from django.contrib import admin
from .models import Group
# Register your models here.
@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Basic Info",
            {"fields":("name", "uni_code","image","members",)},
        ),
    )
    list_display = (
        "name",
        "uni_code",
    )
    filter_horizontal = (
        "members", # manytomany Field 지정
    )