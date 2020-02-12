from django.db import models
from django.db.models import signals


class Pasazerowie(models.Model):
    pesel = models.CharField(max_length=11, unique=True)
    imie = models.CharField(max_length=20)
    nazwisko = models.CharField(max_length=20)

    def __str__(self):
        return str(self.imie) + " " + str(self.nazwisko)
    class Meta:
        verbose_name_plural="Pasazerowie"

class Lotniska(models.Model):
    nazwa = models.CharField(max_length=20)

    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name_plural="Lotniska"

class Trasy(models.Model):
    miejsce_odlotu = models.ForeignKey(Lotniska, related_name="miejsce_odlotu", on_delete=models.CASCADE)
    miejsce_przylotu = models.ForeignKey(Lotniska, related_name="miejsce_przylotu", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.miejsce_odlotu) + " --> " + str(self.miejsce_przylotu)
    class Meta:
        verbose_name_plural="Trasy"

class Samoloty(models.Model):
    ilosc_miejsc = models.IntegerField()

    def __str__(self):
        return "Samolot nr " + str(self.id) + " ilosc miejsc - " + str(self.ilosc_miejsc)

    class Meta:
        verbose_name_plural="Samoloty"


class Loty(models.Model):
    data_odlotu = models.DateTimeField()
    data_przylotu = models.DateTimeField()
    trasa = models.ForeignKey(Trasy, on_delete=models.CASCADE)
    samolot = models.ForeignKey(Samoloty, on_delete=models.CASCADE)
    numer_lotu = models.CharField(max_length=10)

    def __str__(self):
        return str(self.trasa) + " " + str(self.data_odlotu)[:19] + " " + self.numer_lotu

    class Meta:
        verbose_name_plural="Loty"


class Rezerwacje(models.Model):
    pasazer = models.ForeignKey(Pasazerowie, on_delete=models.CASCADE)
    lot = models.ForeignKey(Loty, on_delete=models.CASCADE,default=0)
    data = models.DateTimeField()

    def __str__(self):
        return str(self.id) + "- " + str(self.pasazer) + " data rezerwacji: " + str(self.data)[:19]

    class Meta:
        verbose_name_plural="Rezerwacje"


class Siedzenia(models.Model):
    samolot = models.ForeignKey(Samoloty, on_delete=models.CASCADE)
    lot = models.ForeignKey(Loty, on_delete=models.CASCADE)
    pasazer = models.ForeignKey(Pasazerowie, on_delete=models.CASCADE, default='', null=True, blank=True)
    miejsce = models.IntegerField()

    def __str__(self):
        return str(self.lot) + " " + str(self.miejsce)
    class Meta:
        verbose_name_plural="Siedzenia"
'''funkcje'''

