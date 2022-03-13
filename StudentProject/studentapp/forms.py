from dataclasses import field
import imp
from attr import fields
from django import forms
from studentapp.models import School, Student

class Add_Student_Form(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"


class Add_School_Form(forms.ModelForm):
    class Meta:
        model = School
        fields = "__all__"