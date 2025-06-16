from django.contrib import admin
from project.models import menubaritems,childcell
class menubar(admin.ModelAdmin):
    listdisplay=(menubaritems.name)

class childitems(admin.ModelAdmin):
    listdisplay=(childcell.name, childcell.parentcell)

admin.site.register(menubaritems , menubar)
admin.site.register(childcell ,childitems)
# Register your models here.
