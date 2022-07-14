from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
from .models import Profile, Staff, Student
from django import forms

class ProfileCreationForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = ('email',)


class ProfileChangeForm(UserChangeForm):
    class Meta:
        model = Profile
        fields = ('email',)


class StaffAdminForm(forms.ModelForm):
    """
    Staff model admin form with custom form field validation
    """
    class Meta:
        model = Staff
        fields = "__all__"

    def clean_staff_id(self):
        staff_id = self.cleaned_data["staff_id"].upper()
        
        if (len(staff_id) == 7) and (staff_id[:3] == 'STF') and (staff_id[3:].isnumeric()):
            return self.cleaned_data["staff_id"].upper()
        else:
            raise ValidationError(_("Incorrect staff id!"))


class StudentAdminForm(forms.ModelForm):
    """
    Staff model admin form with custom form field validation
    """
    class Meta:
        model = Student
        fields = "__all__"

    def clean_reg_no(self):
        reg_no = self.cleaned_data["reg_no"]
        
        if (len(reg_no) == 4) and (reg_no.isnumeric()):
            return self.cleaned_data["reg_no"]
        else:
            raise ValidationError(_("Incorrect registration number!"))
