from django.contrib import admin

from .models import Account, Customer, Grid, Node, Project, Service, Stack


class AccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'email', 'type')
    list_filter = ('type',)
    search_fields = ('name', 'email')
    readonly_fields = ('slug',)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('customer', 'name', 'slug')
    list_filter = ('customer',)
    search_fields = ('name', 'slug')
    readonly_fields = ('slug',)


class InlineProjectAdmin(admin.TabularInline):
    model = Project
    extra = 0
    readonly_fields = ('slug',)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'is_internal')
    search_fields = ('name', 'slug')
    readonly_fields = ('slug',)
    inlines = [InlineProjectAdmin]


class NodeAdmin(admin.ModelAdmin):
    list_display = ('grid', 'hostname')
    list_filter = ('grid',)
    search_fields = ('hostname',)


class InlineNodeAdmin(admin.TabularInline):
    model = Node
    extra = 0


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('admin_get_customer', 'admin_get_project', 'stack', 'canonical_name', 'hostname', 'role')

    # TODO WTF The value of 'list_filter[0]' refers to 'stack__project__customer', which does not refer to a Field.
    # list_filter = ('stack__project__customer', 'stack__project', 'stack', 'role')
    list_filter = ('stack__project', 'stack', 'role')

    search_fields = ('hostname', 'name', 'canonical_name')
    raw_id_fields = ('depends_on',)


class InlineServiceAdmin(admin.TabularInline):
    model = Service
    extra = 0
    raw_id_fields = ('depends_on',)


class InlineStackAdmin(admin.TabularInline):
    model = Stack
    extra = 0
    readonly_fields = ('slug',)


class GridAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'type')
    list_filter = ('type',)
    search_fields = ('name', 'slug')
    readonly_fields = ('slug',)
    inlines = [InlineNodeAdmin, InlineStackAdmin]


class StackAdmin(admin.ModelAdmin):
    list_display = ('admin_get_customer', 'project', 'name', 'slug', 'environment')

    # TODO WTF The value of 'list_filter[0]' refers to 'project__customer', which does not refer to a Field.
    # list_filter = ('project__customer', 'project', 'environment')
    list_filter = ('project', 'environment')

    search_fields = ('name', 'slug')
    readonly_fields = ('slug',)
    inlines = [InlineServiceAdmin]


admin.site.register(Account, AccountAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Grid, GridAdmin)
admin.site.register(Node, NodeAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Stack, StackAdmin)
