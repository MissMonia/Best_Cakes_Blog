from django import forms


class GetInTouchForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)




