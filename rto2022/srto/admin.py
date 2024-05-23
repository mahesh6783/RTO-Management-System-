from django.contrib import admin
from srto.models import Rtoffice, Taxrate, Licenserate, Employee, Useraccount, Dealers, Lapptable, Vehicleregister, Question,Drivinglicense

class RtofficeAdmin(admin.ModelAdmin):
    list_display = ('rcode', 'rname','address','phone', 'email')
    search_fields = ('rcode', 'rname')
    list_editable = ['rname','address','phone', 'email']

class TaxrateAdmin(admin.ModelAdmin):
    list_display = ('taxcode', 'vhtype', 'mop', 'taxp','duration')
    search_fields = ('taxcode','vhtype')

class LicenserateAdmin(admin.ModelAdmin):
    list_display = ('lcode', 'lname', 'lfee', 'validity')
    search_fields = ('lcode','lname')

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('adharno', 'ename', 'hname', 'place','quali','phone','email','job','rcode','status')
    search_fields = ('adharno','ename')

class UseraccountAdmin(admin.ModelAdmin):
    list_display = ('uname', 'pword', 'rights', 'ids','rcode')
    search_fields = ('uname','ids')
    list_editable = ['rights']

class DealersAdmin(admin.ModelAdmin):
    list_display = ('dcode', 'dname', 'place', 'phone','email','rcode','status')
    search_fields = ('dcode','dname')

class LeanerAdmin(admin.ModelAdmin):
    list_display = ('id','adate','rcode','aname','dob','gender','fname','lcode','lname','testdate','lno','status')
    list_editable = ['status']

class VehicleregisterAdmin (admin.ModelAdmin):
    list_display = ('id','appdate','rcode','dcode','vname','cardno','oname','status')

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('qno', 'qname', 'op1', 'op2', 'op3', 'op4', 'ans')

class DrivingAdmin(admin.ModelAdmin):
    list_display = ('lno', 'apdate', 'lcode', 'lname', 'amt','rcode','aname', 'cardno', 'dlno', 'status')
    list_editable = ['status']

admin.site.register(Rtoffice, RtofficeAdmin)
admin.site.register(Taxrate,TaxrateAdmin)
admin.site.register(Licenserate,LicenserateAdmin)
admin.site.register(Useraccount, UseraccountAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Dealers, DealersAdmin)
admin.site.register(Lapptable, LeanerAdmin)
admin.site.register(Vehicleregister, VehicleregisterAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Drivinglicense,DrivingAdmin)