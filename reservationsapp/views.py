from django.shortcuts import render, redirect
from .models import *
from django.views.decorators.csrf import csrf_exempt
from .forms import RezerwacjaForm
from django.http import HttpResponseRedirect
from time import *
from django.utils import timezone
# Create your views here.

def wybor_lotu(request):
    loty = Loty.objects.all()
    template ="wybor_lotu.html"
    loty = loty.filter(data_odlotu__gt=timezone.now())
    context = {'loty': loty}
    if request.method == 'GET':
        return render(request, template, context)
    elif request.method == 'POST':
        loty = Loty.objects.all()
        wybrany_lot = request.POST.get('lot')
        for x in loty:
            if str(wybrany_lot) == str(x):
                wybrany_lot = Loty(pk=x.id)
                url = str(x.id) + "/pasazer"
                return HttpResponseRedirect(url)

        return render(request,template,context)


def pasazer(request,id):
    template = "pasazer.html"
    lot = Loty.objects.get(pk=id)
    pasazerowie=Pasazerowie.objects.all()
    siedzenia=Siedzenia.objects.all()
    miejsca=lot.samolot.ilosc_miejsc-siedzenia.filter(lot_id=id).count()
    if request.method == 'GET':
        form = RezerwacjaForm()
        context = {'lot': lot, 'form': form, 'miejsca': miejsca}
        return render(request, template, context)
    elif request.method == "POST":
        form = RezerwacjaForm(request.POST)
        if form.is_valid():
            if miejsca == 0:
                form = RezerwacjaForm()
                context = {'lot': lot, 'form': form, 'miejsca': miejsca, 'brak_miejsc':'brak miejsc!'}
                return render(request, template, context)

            pasazer=Pasazerowie(imie=form.cleaned_data.get('imie'), nazwisko=form.cleaned_data.get('nazwisko'),pesel=form.cleaned_data.get('pesel'))
            pasazer.save()

            siedzenie=Siedzenia(samolot_id=lot.samolot.id, lot_id=id, miejsce=(int(lot.samolot.ilosc_miejsc)) - miejsca, pasazer_id=pasazer.id)
            siedzenie.save()

            rezerwacja=Rezerwacje(pasazer_id=pasazer.id, lot_id=id, data=timezone.now())
            rezerwacja.save()

            url="../../" + str(id) + "/rezerwacje/"
            return HttpResponseRedirect(url)
        else:
            form = RezerwacjaForm()
            context = {'lot': lot, 'form': form}
        return render(request, template, context)


def rezerwacje(request, id):
    if request.method == 'GET':
        template="rezerwacje.html"
        rezerwacje = Rezerwacje.objects.all()
        return render(request, template, {'rezerwacje': rezerwacje})
    elif request.method == 'POST':
        if request.POST.get('nowa_rezerwacja'):
            url="../.."
            return HttpResponseRedirect(url)


def redirect(request):
    return HttpResponseRedirect('/wybor_lotu')