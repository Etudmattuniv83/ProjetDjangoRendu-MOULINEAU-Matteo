from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(label="User name", min_length=5, max_length=100,)
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Password",
                               min_length=5, max_length=100,
                               widget=forms.PasswordInput())

    def clean(self):
        pass

    def clean_first_name(self):
        if self.cleaned_data['first_name'] == '':
            self.add_error('first_name', "First name can't be empty!")
        return self.cleaned_data['first_name']