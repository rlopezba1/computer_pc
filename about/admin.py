from django.contrib import admin
from .models import FAQ

# Register your models here.


class FAQAdmin(admin.ModelAdmin):
    """ Create Admin views for FAQs """
    list_display = (
        'question',
        'answer',
    )


admin.site.register(FAQ, FAQAdmin)