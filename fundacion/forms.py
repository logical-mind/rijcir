from django import forms
from .models import datos



class datosForm(forms.ModelForm):
    
    class Meta:
        model = datos
        fields = '__all__'
      
          
        


