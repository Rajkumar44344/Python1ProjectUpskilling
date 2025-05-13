from django.contrib import admin
from .models import Emp, Testimonial

class EmpAdmin(admin.ModelAdmin):
    # Display the data in the admin table
    list_display = ('name', 'working', 'address', 'phone')
    # Set the first field's display link explicitly to avoid issues
    list_display_links = ('working',)  # Or any other field except 'name'
    # Allow editable fields at the admin level
    list_editable = ('phone', 'name')
    # Enable search functionality in the admin panel
    search_fields = ('name',)  # Ensure this is a tuple

admin.site.register(Emp, EmpAdmin)
admin.site.register(Testimonial)
