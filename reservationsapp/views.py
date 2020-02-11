from django.shortcuts import render, redirect
from .models import *
from django.views.decorators.csrf import csrf_exempt


# Create your views here.


@csrf_exempt
def pasazer(request):
    if request.method == 'GET':
        template = "pasazer.html"
        loty = Loty.objects.all()
        context = {'loty': loty}
        return render(request, template, context)
    elif request.method == "POST":
        template = 'siedzenia.html'
        imie = request.POST.get('imie')
        nazwisko = request.POST.get('nazwisko')
        pesel = request.POST.get('pesel')
        lot = request.POST.get('lot')
        pasazerowie = Pasazerowie.objects.all()

        for x in pasazerowie:
            if pesel == x.pesel:
                if nazwisko == x.nazwisko:
                    if imie == x.imie:
                        existing_id = x.id
                        url = '/siedzenia/' + str(x.id) + "/" + str(lot)
                        return redirect(url)
                    else:
                        loty = Loty.objects.all()
                        error = 'Podany pesel istnieje juz w bazie!'
                        context = {'loty': loty, 'error': error}
                        template = "pasazer.html"

                        return render(request, template, context)
                else:
                    loty = Loty.objects.all()
                    error = 'Podany pesel istnieje juz w bazie!'
                    context = {'loty': loty, 'error': error}
                    template = "pasazer.html"

                    return render(request, template, context)
        pasazerek = Pasazerowie(imie=imie, nazwisko=nazwisko, pesel=pesel)
        pasazerek.save()
        siedzonka = Siedzenia.objects.filter(lot_id=lot.id)
        for x in siedzonka:
            if x.pasazer is None:
                x.pasazer == pasazerek
                x.save(update_fields=['pasazer'])
                continue
        pasazer_id = pasazerek.id
        url = '/siedzenia/' + str(pasazer_id) + "/" + str(lot)

        return redirect(url)


def siedzenia(request, pasazer_id,lot):
    if request.method == 'GET':
        loty=Loty.objects.all()
        for y in loty:
            if str(lot) == str(y):
                id_lotu = y.id
        lot = Loty.objects.get(pk=id_lotu)
        template = "siedzenia.html"
        siedzenia = Siedzenia.objects.filter(lot_id=id_lotu)
        wymagania = Wymagania.objects.all()

        aktualny_pasazer = Pasazerowie.objects.get(pk=pasazer_id)
        context = {'aktualny_pasazer': aktualny_pasazer, 'siedzenia': siedzenia, 'wymagania': wymagania}
        return render(request, template, context)
    if request.method == 'POST':
        url = '/siedzenia/' + str(pasazer_id)
        return redirect(url)


def rezerwacje(request):
    return render(request, template, context)
