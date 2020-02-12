from django import forms
from .models import Pasazerowie
from django.core.exceptions import ValidationError


class RezerwacjaForm(forms.Form):
    imie = forms.CharField(max_length=20, widget=forms.TextInput(attrs=
                                                                 {"placeholder": "Imie",
                                                                 "required": "required",
                                                                 "pattern":"[A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ' ]{1,20}",
                                                                 "maxlength":"20",
                                                                 "title": "Dozwolone znaki : A-Z a-z żźćńółęąśŻŹĆĄŚĘŁÓŃ' oraz spacja"
                                                                  }
                                                                 )
                           )
    nazwisko = forms.CharField(max_length=20, widget=forms.TextInput(attrs={"placeholder": "Nazwisko",
                                                                            "required": "required",
                                                                            "pattern":"[A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ' ]{1,20}",
                                                                            "maxlength":"20",
                                                                            "title":"Dozwolone znaki : A-Z a-z żźćńółęąśŻŹĆĄŚĘŁÓŃ' oraz spacja"
                                                                            }
                                                                 )
                               )
    pesel = forms.CharField(max_length=11, widget=forms.TextInput(attrs={"placeholder": "Pesel",
                                                                         "required": "required",
                                                                         "pattern": "^\d{11}$",
                                                                         "title": "Pesel to ciąg 11 cyfr!"}))
    #miejsca = forms.IntegerField(widget=forms.NumberInput(attrs={"min": "1",
                                                                # "max": "5",
                                                                 #"required": "required",
                                                                 #"default": "1",
                                                                # }))


    def clean_pesel(self):
        data = self.cleaned_data.get('pesel')
        pasazerowie = Pasazerowie.objects.all()
        for x in pasazerowie:
            if data == x.pesel:
                raise ValidationError('Podany pesel istnieje juz w bazie danych!')
        return data

    #def clean_miejsca(self):
    #    data = self.cleaned_data.get('miejsca')
    #    return data