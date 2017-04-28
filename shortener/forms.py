from django import forms

from django.core.validators import URLValidator

from .validators import validate_url, validate_dot_com

class SubmitUrlForm(forms.Form):
    url = forms.CharField(label = "Submit URL Here.", validators=[validate_url, validate_dot_com])

    # def clean(self):
    #     cleaned_data = super(SubmitUrlForm, self).clean()
    #     print (cleaned_data)
    #     url = cleaned_data.get('url')
    #     print (url)
    #     url_validator = URLValidator()
    #     try:
    #         url_validator(url)
    #     except:
    #         raise forms.ValidationError("Invalid URL or this field.")
    #     return url


    # def clean_url(self):
    #     url = self.cleaned_data['url']
    #
    #     # print (url)
    #     # url_validator = URLValidator()
    #     # try:
    #     #     url_validator(url)
    #     # except:
    #     #     raise forms.ValidationError("Invalid URL or this field.")
    #     return url
