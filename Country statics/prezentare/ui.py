from exceptii.erori import *

class Consola:
    def __init__(self,service):
        self.__service_tari=service
        self.comenzi={
            "adauga":self.__adauga,
            "inflatie":self.__rata_inflatie
        }

    def __adauga(self):
        nume=input("Introduceti numele tari: ")
        an=int(input("Introduceti anul: "))
        inflatie=float(input("Introduceti inflatie: "))
        somaj=float(input("Introduceti somaj: "))
        populatie=input("Introduceti populatie: ")
        self.__service_tari.adauga(nume,an,inflatie,somaj,populatie)

    def __rata_inflatie(self):
        rata_inflatie=float(input("Introduceti rata inflatiei dorita: "))
        lista_inflatie=self.__service_tari.rata_medie_de_inflatie(rata_inflatie)
        if lista_inflatie==None:
            print("Nu exista astfel de tara!")
        else:
            for tara in lista_inflatie:
                print(f"{tara.nume},{tara.somaj}")

    def run(self):
        while True:
            nume_comanda=input(">>>")
            nume_comanda.strip()
            if nume_comanda=="exit":
                break
            if nume_comanda =="":
                continue
            try:
                if nume_comanda in self.comenzi:
                    self.comenzi[nume_comanda]()
                else:
                    print("Comanda invalida!")
            except ValueError as ve:
                print(f"Eroare de validare: {ve}")
            except RepoError as re:
                print(f"Eroare de repo: {re}")