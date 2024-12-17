from domeniu.comanda import Comenzi

class ServiceHaine:
    def __init__(self, repo_haine,validator_haine):
        self.__repo_haine = repo_haine
        self.__validator_haine = validator_haine
        self.lista_comenzi=[]

    def lista_comenzi_function(self):
        return self.lista_comenzi

    def lista_haine_function(self):
        return self.__repo_haine.lista_haine

    def adauga_service(self,id_haine,denumire,tip,pret):
        self.__repo_haine.adauga_haine(id_haine,denumire,tip,pret)

    def filtrare_tip(self,tip):
        lista_haine=self.__repo_haine.lista_haine_function()
        lista_filtrata=[]
        for haina in lista_haine:
            if haina.tip==tip:
                lista_filtrata.append(haina)
        return lista_filtrata

    def comanda(self,id_haina,nr_bucati,nume,adresa):
        lista_haine=self.__repo_haine.lista_haine_function()
        pret=lista_haine[id_haina-1].pret*nr_bucati
        comanda=Comenzi(id_haina,nr_bucati,nume,adresa,lista_haine[id_haina-1].pret,pret)
        self.lista_comenzi.append(comanda)