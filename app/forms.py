from django import forms

class FormData(forms.Form):
	url = forms.CharField(
		max_length=2000,
		widget=forms.TextInput(
			attrs={
				'class':'form-control',
				'placeholder':'Enter URL',
				'id':'inputUrl'
			}
		)
	)
	slug = forms.CharField(
		max_length=100,
		widget=forms.TextInput(
			attrs={
				'class':'form-control',
				'placeholder':'Enter Slug',
				'id':'inputSlug'
			}
		)
	)
