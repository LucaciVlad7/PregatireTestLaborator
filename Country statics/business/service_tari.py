from domeniu.tari import Tara
from domeniu.maxim import Maxim

class ServiceTari:
    def __init__(self,repo,validator):
        self.__repo_tari=repo
        self.__validator_tari=validator

    def adauga_service(self,nume,an,inflatie,somaj,populatie):
        tara=Tara(nume,an,inflatie,somaj,populatie)
        self.__validator_tari.validator_tari(tara)
        self.__repo_tari.adauga_tara(nume,an,inflatie,somaj,populatie)

    def rata_medie_de_inflatie(self,rata_inflatie):
        lista=self.__repo_tari.lista_tari_function()
        lista.sort(key=lambda x: x.nume)
        last_name=""
        contor=0
        inflatie=0
        lista_nume=[]
        maxim=0
        ob=None
        for tara in lista:
            if tara.nume==last_name or last_name=="":
                contor+=1
                inflatie+=tara.inflatie
                somaj_curent=self.calculeaza_somaj(tara)
                if somaj_curent>maxim:
                    maxim=somaj_curent
                last_name = tara.nume
            else:
                if inflatie/contor>rata_inflatie:
                    somaj=self.prelucrare(maxim)
                    inflatie_somaj=Maxim(last_name,somaj)
                    lista_nume.append(inflatie_somaj)
                inflatie=0
                contor=1
                maxim=self.calculeaza_somaj(tara)
                last_name=tara.nume
                ob=tara
        if ob!=None:
            inflatie += ob.inflatie
            if inflatie / contor > rata_inflatie:
                somaj = self.prelucrare(maxim)
                inflatie_somaj = Maxim(last_name, somaj)
                lista_nume.append(inflatie_somaj)
            return lista_nume
        else:
            return None

    def prelucrare(self,number):
        """
        Formats a number so that each 10^3n section is separated by an underscore.

        Args:
            number (int): The input number.

        Returns:
            str: The formatted string with underscores separating 10^3n sections.
        """
        reversed_number = str(number)[::-1]
        grouped = ''.join([reversed_number[i:i + 3] for i in range(0, len(reversed_number), 3)])
        return grouped[::-1]

    def calculeaza_somaj(self,tara):
        parts=tara.populatie.split("_")
        pop=0
        for i in range(len(parts)):
            pop+=int(parts[i])
            pop=pop*1000
        pop=pop/1000
        return pop*tara.somaj