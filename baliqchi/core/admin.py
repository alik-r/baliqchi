from django.contrib import admin
from import_export import fields, resources
from import_export.admin import ImportExportModelAdmin
from core.models import Target, Incident, Alert

class TargetResource(resources.ModelResource):
    id = fields.Field(column_name='id', attribute='id')
    phone_number = fields.Field(column_name='phone_number', attribute='phone_number')
    device_info = fields.Field(column_name='device_info', attribute='device_info')
    created_at = fields.Field(column_name='created_at', attribute='created_at')
    updated_at = fields.Field(column_name='updated_at', attribute='updated_at')
    is_deleted = fields.Field(column_name='is_deleted', attribute='is_deleted')

    class Meta:
        model = Target
        fields = ('id', 'phone_number', 'device_info', 'created_at', 'updated_at', 'is_deleted')
        export_order = ('id', 'phone_number', 'device_info', 'created_at', 'updated_at', 'is_deleted')


class TargetAdmin(ImportExportModelAdmin):
    resource_class = TargetResource
    list_display = ('phone_number', 'device_info', 'created_at', 'updated_at', 'is_deleted',)

admin.site.site_header = "Baliqchi Admin"
admin.site.register(Target, TargetAdmin)
admin.site.register(Incident)
admin.site.register(Alert)