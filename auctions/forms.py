from re import A
from django import forms
from decimal import *
from .models import Comment, Category
from django.forms import Select

class Select(Select):
    def create_option(self, *args, **kwargs):
        option = super().create_option(*args, **kwargs)
        if not option.get('value'):
            option['attrs']['disabled'] = 'True'
        
        return option

class CreateListing(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""  # Removes : as label suffix

    
    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)
         
        tmp = list(Category.objects.values('name'))
        tmp = [i['name'] for i in tmp]
        CHOICES = [('', 'Select a category')]   
        for i in range(len(tmp)):
            CHOICES.append((tmp[i], tmp[i].capitalize()))
        self.fields["category"].choices=CHOICES


    product = forms.CharField(label="Product Name", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Product name'}))
    price = forms.CharField(label="Initial Bid", widget=forms.TextInput(attrs={'class': 'bid-input bid-f', 'id':'bidding_val', 'value':'0.00'}))
    image = forms.URLField(label="Product Image", max_length=5000, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Image link'}))
    category = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-select'}), initial='Select a category')
    description = forms.CharField(label="Description", max_length=500, widget=forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Additional information'}))

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control comment-body'
            visible.field.widget.attrs['placeholder'] = 'Leave a comment'
            visible.label = ''

