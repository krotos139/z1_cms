from django.contrib import admin
from datetime import datetime
from cms.models import Category,Entity,MainMenu
from filebrowser.sites import FileBrowserSite

# Register your models here.
class EntityAdmin(admin.ModelAdmin):
    fieldsets = [
        ( None,         {'fields': ['name', 'category', 'content']}),
        ( 'Additional', {'fields': ['tags', 'author', 'pub_date'], 'classes': ['collapse']})
    ]
    list_display = ('category', 'name', 'pub_date')
    search_fields = ['name']
    list_filter = ['pub_date'] 
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'author':
            kwargs['initial'] = request.user.id
        return super(EntityAdmin, self).formfield_for_foreignkey( db_field, request, **kwargs )

#    class Media:
#        js = ('/static/tinymce/tinymce.min.js',)


admin.site.register(MainMenu)
admin.site.register(Category)
admin.site.register(Entity, EntityAdmin)
