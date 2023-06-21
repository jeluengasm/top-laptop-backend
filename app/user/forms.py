from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.translation import gettext_lazy as _

from user.models import User


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(
        label=_('Password'), widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label=_('Password confirmation'), widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ['email']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords don\'t match')
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    help_text = _(
        '''
        Raw passwords are not stored, so there is no way to see this
        user's password, but you can change the password using
        <a href='../password/'>this form</a>.
    '''
    )
    password = ReadOnlyPasswordHashField(label='Password', help_text=help_text)

    class Meta:
        model = User
        fields = ['email', 'password', 'is_active']

    def clean_password(self):
        return self.initial['password']
