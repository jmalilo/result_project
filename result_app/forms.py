from django.forms import Form
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from result_app.models import User,Fee
from django import forms
from django.conf import settings
from result_app.models import Result



class SignupForm(UserCreationForm):
    class Meta:
        model=User
        fields=['email','full_name','phone_1','phone_2','password1','password2']

class ResultForm(forms.ModelForm):
    class Meta:
        model=Result
        fields=['email','stud_name','arithmetic','e_language','kiswahili','pre_science','writing']

# class AddParentForm(forms.ModelForm):
#     class Meta:
#         model=User
#         fields=['email']


class EditResultForm(forms.ModelForm):
    class Meta:
        model=Result
        fields=['email','stud_name','arithmetic','e_language','kiswahili','pre_science','writing']

class EditParentForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['email','full_name','phone_1','phone_2']
class AddFeeForm(forms.ModelForm):
    class Meta:
        model=Fee
        exclude=['debt']  

class EditFeeForm(forms.ModelForm):
    class Meta:
        model=Fee
        exclude=['debt'] 
