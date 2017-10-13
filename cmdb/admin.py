from django.contrib import admin

from .models import Customer, Grid, Node, Project, Service


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'is_internal')
    search_fields = ('name', 'slug')
    readonly_fields = ('slug',)


class GridAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'type')
    list_filter = ('type',)
    search_fields = ('name', 'slug')
    readonly_fields = ('slug',)


class NodeAdmin(admin.ModelAdmin):
    list_display = ('grid', 'hostname')
    list_filter = ('grid',)
    search_fields = ('hostname',)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('customer', 'name', 'slug')
    list_filter = ('customer',)
    search_fields = ('name', 'slug')
    readonly_fields = ('slug',)


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('project', 'canonical_name', 'hostname', 'role', 'environment', 'grid')
    list_filter = ('project', 'project__customer', 'role', 'environment', 'grid')
    search_fields = ('hostname', 'name', 'canonical_name')
    raw_id_fields = ('depends_on',)


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Grid, GridAdmin)
admin.site.register(Node, NodeAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Service, ServiceAdmin)
