from erori.errors import RepoError, ValidationError


class Consola:
    def __init__(self,_serivce_materiale):
        self.__serivce_materiale=_serivce_materiale
        self.__comenzi={
            "adauga":self.__ui_adauga,
            "afisare":self.__ui_afisare,
            "vanzare":self.__vanzare,
            "valoare":self.__ui_valoare,
        }

    def __ui_adauga(self):
        id_material=int(input("Introduceti Id-ul materialulul: "))
        denumire=input("Introduceti denumirea materialului: ")
        unitate_masura=input("Introduceti unitatea de masura: ")
        cantitate=float(input("Introduceti cantitatea: "))
        pret=float(input("Introduceti pretul: "))
        self.__serivce_materiale.adauga_material(id_material,denumire,unitate_masura,cantitate,pret)

    def __ui_afisare(self):
        materiale=self.__serivce_materiale.lista_materiale_service()
        for material in materiale:
            print(f"Id-ul materialului: {material.id_material}")
            print(f"Denumirea materialului: {material.denumire}")
            print(f"Unitatea de masura: {material.unitate_masura}")
            print(f"Cantitatea: {material.cantitate }")
            print(f"Pret: {material.pret}")
            print("--------------------------------")

    def __vanzare(self):
        id_material = int(input("Introduceti Id-ul materialulul: "))
        id_material -= 1
        cantitate = float(input("Introduceti cantitatea: "))
        denumire, cantitate, valoare_incasata=self.__serivce_materiale.service_vanzare(id_material,cantitate)
        if denumire is None:
            print("Cantitatea introdusa este prea mare")
        else:
            print("Vanzarea s-a realizat cu succes")
            print(f"Denumirea materialului: {denumire}")
            print(f"Cantitatea vanduta: {cantitate}")
            print(f"Valoarea incasata: {valoare_incasata}")

    def __ui_valoare(self):
        valoare=float(input("Introduceti valoarea materialului: "))
        self.__serivce_materiale.salvare_fisier_a_materialelor_cu_valoare(valoare)

    def run(self):
        while True:
            nume_comanda=input(">>>>")
            nume_comanda=nume_comanda.lower()
            nume_comanda=nume_comanda.strip()
            if nume_comanda=="":
                continue
            if nume_comanda=="exit":
                print("Aplicatia se va opri")
                break
            if nume_comanda in self.__comenzi:
                try:
                    self.__comenzi[nume_comanda]()
                except RepoError as re:
                    print(f"Eroare de repo:{re}")
                except ValidationError as ve:
                    print(f"Eroare de validare:{ve}")
            else:
                print("Comanda invalida!")