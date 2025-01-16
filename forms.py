class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image']
