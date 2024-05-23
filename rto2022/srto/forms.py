from django import forms
from srto.models import Rtoffice, Taxrate, Licenserate, Employee, Dealers, Leaners, Lapptable, Vehicleregister,Question,Drivinglicense

class RtofficeForm(forms.ModelForm):
    class Meta:
        model = Rtoffice
        fields = ['rcode','rname', 'address','phone','email']

class TaxForm(forms.ModelForm):
    class Meta:
        model = Taxrate
        fields = "__all__"

class LicenseForm(forms.ModelForm):
    class Meta:
        model = Licenserate
        fields = "__all__"

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['adharno', 'ename','gender', 'hname', 'place', 'quali', 'phone', 'email', 'rcode']

class DealerForm(forms.ModelForm):
    class Meta:
        model= Dealers
        fields =['dcode', 'dname', 'place', 'phone', 'email', 'rcode']

class LeanersForm(forms.ModelForm):
    class Meta:
        model = Leaners
        fields =['adate', 'rcode', 'aname', 'dob', 'gender', 'fname', 'address', 'adharno', 'quali', 'cardno']


class LapptableForm(forms.ModelForm):
    class Meta:
        model = Lapptable
        fields =['adate', 'rcode', 'aname', 'dob', 'gender', 'fname', 'address', 'adharno', 'quali','phone','email', 'cardno']


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicleregister
        fields = ['appdate','rcode','dcode','vname','eno','chno','ymanu','mnamu','taxcode','vprice','tax','cardno','oname','address','adharno','mobile','email']

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields =['qno','qname','op1','op2','op3','op4','ans']

class DrivingForm(forms.ModelForm):
    class Meta:
        model = Drivinglicense
        fields = "__all__"

