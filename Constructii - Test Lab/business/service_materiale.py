from domeniu.Materiale import Materiale


class ServiceMateriale:
    def __init__(self,repo,validare):
        self.__repo_material=repo
        self.__validare=validare

    def adauga_material(self,id_material,denumire,unitate_masura,cantitate,pret):
        material=Materiale(id_material,denumire,unitate_masura,cantitate,pret)
        self.__validare.valideaza_material(material)
        self.__repo_material.adauga_material(id_material,denumire,unitate_masura,cantitate,pret)

    def lista_materiale_service(self):
        return self.__repo_material.lista_materiale_function()

    def service_vanzare(self,id_material,cantitate):
        denumire,cantitate,valoare_incasata=self.__repo_material.vanzare(id_material,cantitate)
        with open("vanzari","a") as f:
            f.write(f"{denumire},{cantitate},{valoare_incasata}\n")
        self.__repo_material.scrie_tot_in_fisier()
        return denumire,cantitate,valoare_incasata

    def salvare_fisier_a_materialelor_cu_valoare(self,valoare):
        lista_materiale=self.__repo_material.lista_materiale_function()
        lista_cu_valoare=[]
        for material in lista_materiale:
            if material.pret*material.cantitate>valoare:
                lista_cu_valoare.append(material)
        with open("fisier_cu_valoare","w") as f:
            for material in lista_cu_valoare:
                f.write(f"{material.id_material},{material.denumire},{material.cantitate},{material.pret}\n")