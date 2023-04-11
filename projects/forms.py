from .models import Project
from django import forms 
from django.forms import ModelForm

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title' ,'featured_images' , 'description','demo_link', 'source_link','tags']

        widgets = {
            'tags' : forms.CheckboxSelectMultiple() ,  
        }
    
    def __init__(self, *args , **kwargs):
        super(ProjectForm , self).__init__(*args, **kwargs)

        for name , field in self.fields.items():
            field.widget.attrs.update({'class' : 'input'})
        # self.fields['title'].widget.attrs.update({'class': 'input' , 'placeholder':'Add title'})

        # self.fields['description'].widget.attrs.update({'class': 'input' , 'placeholder':'Add description'})
