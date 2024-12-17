from domeniu.Materiale import Materiale
from erori.errors import RepoError

class Repo_materiale:
    def __init__(self,cale_fisier):
        self.lista_materiale = []
        self.__cale_fisier = cale_fisier
        self.__citeste_tot_din_fisier()

    def lista_materiale_function(self):
        return self.lista_materiale

    def adauga_material(self,id_material,denumire,unitate_masura,cantitate,pret):
        self.__adauga_material_lista(id_material,denumire,unitate_masura,cantitate,pret)
        self.__scrie_la_final(id_material,denumire,unitate_masura,cantitate,pret)

    def vanzare(self,id_material,cantitate):
        if cantitate>self.lista_materiale[id_material].cantitate:
            return None,None,None
        else:
            self.lista_materiale[id_material].cantitate-=cantitate
            return self.lista_materiale[id_material].denumire,cantitate,cantitate*self.lista_materiale[id_material].pret

    def __adauga_material_lista(self,id_material,denumire,unitate_masura,cantitate,pret):
        material=Materiale(id_material,denumire,unitate_masura,cantitate,pret)
        for materiale in self.lista_materiale:
            if id_material==materiale.id_material:
                raise RepoError("Id-ul exista deja\n")
        self.lista_materiale.append(material)

    def __citeste_tot_din_fisier(self):
        with open(self.__cale_fisier, 'r') as f:
            self.lista_materiale.clear()
            linii=f.readlines()
            for linie in linii:
                linie=linie.strip()
                if linie!="":
                    parts=linie.split(",")
                    cod=int(parts[0])
                    denumire=parts[1]
                    unitate_masura=parts[2]
                    cantitate=float(parts[3])
                    pret=float(parts[4])
                    material=Materiale(cod,denumire,unitate_masura,cantitate,pret)
                    self.lista_materiale.append(material)

    def __scrie_la_final(self,cod,denumire,unitate_masura,cantitate,pret):
        with open(self.__cale_fisier, 'a') as f:
            f.write(f"\n{cod},{denumire},{unitate_masura},{cantitate},{pret}")

    def scrie_tot_in_fisier(self):
        with open(self.__cale_fisier, 'w') as f:
            for material in self.lista_materiale:
                f.write(f"{material.id_material},{material.denumire},{material.unitate_masura},{material.cantitate},{material.pret} \n")