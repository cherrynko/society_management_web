from django.contrib import admin
from .models import Role,Department,Member,Director,AssistantDirector,EC,Sponsor,Patron

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
    list_display = ('member_name','role_name', 'dept_name')
    list_filter = ('dept_name','role_name')

class DirAdmin(admin.ModelAdmin):
    list_display = ('member_name','role_name', 'dept_name')
    list_filter = ('dept_name','role_name')

class ECAdmin(admin.ModelAdmin):
    list_display = ('member_name','role_name')
    list_filter = ['role_name']

class ADAdmin(admin.ModelAdmin):
    list_display = ('member_name','role_name', 'dept_name')
    list_filter = ('dept_name','role_name')

admin.site.register(Role)
admin.site.register(Department)
admin.site.register(Member, MemberAdmin)
admin.site.register(Director, DirAdmin)
admin.site.register(AssistantDirector, ADAdmin)
admin.site.register(EC, ECAdmin)
admin.site.register(Sponsor)
admin.site.register(Patron)


