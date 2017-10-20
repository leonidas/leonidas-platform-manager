from django.contrib import admin

from .models import Customer, Grid, Node, Project, Service, Stack


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


class StackAdmin(admin.ModelAdmin):
    list_display = ('admin_get_customer', 'project', 'name', 'slug', 'environment')

    # TODO WTF The value of 'list_filter[0]' refers to 'project__customer', which does not refer to a Field.
    # list_filter = ('project__customer', 'project', 'environment')
    list_filter = ('project', 'environment')

    search_fields = ('name', 'slug')
    readonly_fields = ('slug',)


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('admin_get_customer', 'admin_get_project', 'stack', 'canonical_name', 'hostname', 'role')

    # TODO WTF The value of 'list_filter[0]' refers to 'stack__project__customer', which does not refer to a Field.
    # list_filter = ('stack__project__customer', 'stack__project', 'stack', 'role')
    list_filter = ('stack__project', 'stack', 'role')

    search_fields = ('hostname', 'name', 'canonical_name')
    raw_id_fields = ('depends_on',)


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Grid, GridAdmin)
admin.site.register(Node, NodeAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Stack, StackAdmin)
admin.site.register(Service, ServiceAdmin)
