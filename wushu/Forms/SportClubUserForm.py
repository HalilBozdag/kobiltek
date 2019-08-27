from django import forms
from django.forms import ModelForm

from wushu.models import SportClubUser


class SportClubUserForm(ModelForm):
    class Meta:
        model = SportClubUser

        fields = (
            'role', 'sportClub')
        labels = {'role': 'Rol'}

        widgets = {

            'role': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                        'style': 'width: 100%; '}),

            'sportClub': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                             'style': 'width: 100%; '}),

        }