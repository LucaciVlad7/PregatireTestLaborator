from time import sleep

from domeniu.domeniu_specii import Specii

class RepoSpecii:
    def __init__(self,cale_fisier):
        self.lista_specii = []
        self.__cale_fisier = cale_fisier
        self.citeste_tot_din_fisier()

    def lista_specii_function(self):
        return self.lista_specii

    def citeste_tot_din_fisier(self):
        with open(self.__cale_fisier, 'r') as f:
            self.lista_specii.clear()
            linii=f.readlines()
            for linie in linii:
                linie=linie.strip()
                parts=linie.split(',')
                id_specie=parts[0]
                nume=parts[1]
                data=parts[2]
                locatie=parts[3]
                tip=parts[4]
                durata_de_viata=parts[5]
                specie=Specii(id_specie,nume,data,locatie,tip,durata_de_viata)
                self.lista_specii.append(specie)


