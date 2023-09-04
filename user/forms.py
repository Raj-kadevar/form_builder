from django import forms

from user.models import User


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["name", "email", "number", "gender"]

    def clean_name(self):
        name = self.cleaned_data['name']
        if User.objects.filter(name=name).exists():
            raise forms.ValidationError("This name is already taken.")
        return name

    def clean_name(self):
        name = self.cleaned_data['name']
        if User.objects.filter(name=name).exists():
            raise forms.ValidationError("This name is already taken.")
        return name

    def clean_name(self):
        name = self.cleaned_data['name']
        if User.objects.filter(name=name).exists():
            raise forms.ValidationError("This name is already taken.")
        return name

    def clean_number(self):
        number = self.cleaned_data["number"]
        if not number.isdigit():
            raise forms.ValidationError("Please enter number only")
        elif len(str(number)) != 10:
            raise forms.ValidationError("Please enter 10 digit")
        else:
            if User.objects.filter(number=number).exists():
                raise forms.ValidationError("This number is already taken.")
        return number