from django.contrib import admin
from .models import Profile,Product
from django.contrib.auth.models import Group


# Register your models here.
admin.site.register(Profile)


admin.site.unregister(Group)

admin.site.site_header = 'DressUp Admin Dashboard'
admin.site.site_title = 'Welcome to DressUp Admin Dashboard'
admin.site.index_title = 'DressUp Portal'

class ProductAdmin(admin.ModelAdmin):
  list_display = ('name', 'profile', 'category', 'created_on', 'active') 
  list_filter = ('name', 'created_on', 'category')

  def active(self, obj): 
    return obj.is_active == 1

  active.boolean = True

  def make_active(modeladmin, request, queryset):
    queryset.update(is_active = 1) 
    messages.success(request, "Selected Record(s) Marked as Active Successfully !!") 

  def make_inactive(modeladmin, request, queryset):
    queryset.update(is_active = 0)
    messages.success(request, "Selected Record(s) Marked as Inactive Successfully !!") 

  admin.site.add_action(make_active, "Make Active") 
  admin.site.add_action(make_inactive, "Make Inactive")

  # def has_delete_permission(self, request, obj = None): 
  #   return False

  # def has_add_permission(self, request): 
  #   return False

admin.site.register(Product, ProductAdmin)
