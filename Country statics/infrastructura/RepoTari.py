from domeniu.tari import Tara
from exceptii.erori import RepoError

class RepoTari:
    def __init__(self,cale_fisier):
        self.__cale_fisier=cale_fisier
        self.lista_tari=[]
        self.citeste_tot_din_fisier()

    def lista_tari_function(self):
        return self.lista_tari

    def adauga_tara(self,nume,an,inflatie,somaj,populatie):
        self.__adauga_lista(nume,an,inflatie,somaj,populatie)
        self.__append_fisier(nume,an,inflatie,somaj,populatie)

    def __adauga_lista(self,nume,an,inflatie,somaj,populatie):
        tara=Tara(nume,an,inflatie,somaj,populatie)
        for tari in self.lista_tari:
            if tari.nume==nume and tari.an==an:
                raise RepoError("Date invalide")
        self.lista_tari.append(tara)

    def __append_fisier(self,nume,an,inflatie,somaj,populatie):
        with open(self.__cale_fisier,'a') as f:
            f.write(f"\n{nume},{an},{inflatie},{somaj},{populatie}\n")

    def citeste_tot_din_fisier(self):
        self.lista_tari.clear()
        with open(self.__cale_fisier,'r') as f:
            linii=f.readlines()
            for linie in linii:
                linie.strip()
                if linie=="":
                    continue
                parts=linie.split(",")
                nume=parts[0]
                an=int(parts[1])
                inflatie=float(parts[2])
                somaj=float(parts[3])
                populatie=parts[4]
                tara=Tara(nume,an,inflatie,somaj,populatie)
                self.lista_tari.append(tara)

