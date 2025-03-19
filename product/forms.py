from django import forms
from .models import FoodItem, Category, Species

class FoodItemForm(forms.ModelForm):
    class Meta:
        model = FoodItem
        fields = ['name', 'image', 'price', 'calories_per_10g', 'category', 'species']

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    species = forms.ModelMultipleChoiceField(
        queryset=Species.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple()  # ✅ Allow multiple choices
    )

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    image = forms.FileInput(attrs={'class': 'form-control'})
    price = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    calories_per_10g = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
