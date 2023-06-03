from django.contrib import admin
from result_app.models import Result,Student,LevelClass,User,Fee
# Register your models here.
admin.site.site_header='Result Management system'
admin.site.index_title='Manage School'


class ResultAdmin(admin.ModelAdmin):
    list_display=['stud_name','total','average','grade']
    # search_fields=['stud_name']
    list_display_links=['total','average']
    # list_editable=['grade','average','total']



admin.site.register(Result,ResultAdmin)
admin.site.register(Student)
admin.site.register(LevelClass)
admin.site.register(User)
admin.site.register(Fee)