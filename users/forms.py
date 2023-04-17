from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1' , 'password2']
        labels = {
            'first_name': 'Name',
        }

    def __init__(self, *args , **kwargs):
        super(CustomUserCreationForm , self).__init__(*args, **kwargs)

        for name , field in self.fields.items():
            field.widget.attrs.update({'class' : 'input'})

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = [ 'username' , 'name', 
                'email', 'location' ,
                'short_intro', 'bio' , 'profile_image' , 
                'social_github' , 'social_telegram' , 
                'social_instagram' , 'social_linkedin' , 'social_twitter' ,]
        
    def __init__(self, *args , **kwargs):
        super(ProfileForm , self).__init__(*args, **kwargs)

        for name , field in self.fields.items():
            field.widget.attrs.update({'class' : 'input'})