from .models import Project
from django.forms import ModelForm

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title' , 'description', 'featured_images' , 'demo_link', 'source_link','tags']

