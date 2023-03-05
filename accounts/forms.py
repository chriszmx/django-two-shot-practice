from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=150,
                               widget=forms.PasswordInput
                               )


class SignupFrom(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=150,
                               widget=forms.PasswordInput)
    password_confirmation = forms.CharField(max_length=150,
                                            widget=forms.PasswordInput)

    # class Meta:
    #     fields = (
    #         'username',
    #         'password',
    #         'password_confirmation',
    #     )
