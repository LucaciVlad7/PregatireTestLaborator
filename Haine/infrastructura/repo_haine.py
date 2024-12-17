from domeniu.imbracaminte import Haine
from exceptii.erori import RepoError

class RepoHaine:
    def __init__(self,cale_fisier):
        self.__cale_fisier=cale_fisier
        self.lista_haine=[]
        self.citeste_tot_din_fisier()

    def adauga_haine(self,id_haine,denumire,tip,pret):
        self.adauga_in_lista(id_haine,denumire,tip,pret)
        self.scrie_la_final(id_haine,denumire,tip,pret)

    def lista_haine_function(self):
        return self.lista_haine

    def adauga_in_lista(self,id_haine,denumire,tip,pret):
        for haina in self.lista_haine:
            if haina.id_haine==id_haine:
                raise RepoError("Id-ul exista deja")
        haina=Haine(id_haine,denumire,tip,pret)
        self.lista_haine.append(haina)

    def scrie_tot_in_fisier(self):
        with open(self.__cale_fisier,'w') as f:
            for haina in self.lista_haine:
                print(f"{haina.id_haine},{haina.denumire},{haina.tip},{haina.pret}\n")

    def scrie_la_final(self,id_haine,denumire,tip,pret):
        with open(self.__cale_fisier,'a') as f:
            f.write(f"\n{id_haine},{denumire},{tip},{pret}")

    def citeste_tot_din_fisier(self):
        with open(self.__cale_fisier,'r') as f:
            self.lista_haine.clear()
            linii=f.readlines()
            for linie in linii:
                linie=linie.strip()
                if linie!="":
                    parts=linie.split(",")
                    id_haine=int(parts[0])
                    denumire=parts[1]
                    tip=parts[2]
                    pret=float(parts[3])
                    haina=Haine(id_haine,denumire,tip,pret)
                    self.lista_haine.append(haina)

