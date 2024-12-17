from exceptii.erori import RepoError,ValidationError

class Consola:
    def __init__(self,_service_haine):
        self.__service_haine=_service_haine
        self._comenzi={
            "adauga":self.adauga,
            "afiseaza":self.afiseaza,
            "filtrare":self.filtrare,
            "comanda":self.comada,
            "afisare_comenzi":self.afisare_comenzi
        }

    def adauga(self):
        id_haina=int(input("Introduceti id-ul: "))
        denumire=input("Denumire: ")
        tip=input("Tip: ")
        pret=input("Pret: ")
        self.__service_haine.adauga_service(id_haina,denumire,tip,pret)

    def afiseaza(self):
        lista=self.__service_haine.lista_haine_function()
        for haina in lista:
            print("----------------")
            print(haina.id_haine)
            print(haina.denumire)
            print(haina.tip)
            print(haina.pret)

    def filtrare(self):
        tip=input("Tip: ")
        lista_filtrata=self.__service_haine.filtrare_tip(tip)
        for haina in lista_filtrata:
            print("----------------")
            print(haina.id_haine)
            print(haina.denumire)
            print(haina.tip)

    def comada(self):
        id_haina=int(input("Introduceti id-ul: "))
        nr_bucati=int(input("Introduceti nr de bucati:"))
        nume=input("Nume: ")
        adresa=input("Adresa: ")
        self.__service_haine.comanda(id_haina,nr_bucati,nume,adresa)

    def afisare_comenzi(self):
        lista=self.__service_haine.lista_comenzi_function()
        for comanda in lista:
            print("----------------")
            print(comanda.id_haina)
            print(comanda.nr_bucati)
            print(comanda.nume)
            print(comanda.adresa)
            print(comanda.pret_bucata)
            print(comanda.pret_total)

    def run(self):
        while True:
            nume_comanda=input(">>>")
            nume_comanda.lower()
            nume_comanda.strip()
            if nume_comanda=="":
                continue
            if nume_comanda=="exit":
                print("Aplicatia se va opri")
                break
            if nume_comanda in self._comenzi:
                try:
                    self._comenzi[nume_comanda]()
                except RepoError as re:
                    print(f"Eroare in repo:{re}")
                except ValidationError as ve:
                    print(f"Eroare la validare:{ve}")
            else:
                print("Comanda invalida")
