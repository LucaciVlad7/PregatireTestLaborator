import unittest
from repo.repo_materiale import Repo_materiale
from business.service_materiale import ServiceMateriale
from domeniu.Materiale import Materiale
from validare.validare_materiale import ValidareMateriale

class Test(unittest.TestCase):
    def setUp(self):
        self.repo_materiale=Repo_materiale("materiale.txt")
        self.validator=ValidareMateriale()
        self.service_materiale=ServiceMateriale(self.repo_materiale,self.validator)

    def ruleaza_toate_testele(self):
        #Test adauga
        self.repo_materiale.adauga_material(0, "Denumire", "Unit", 1000, 1000)
        lista=self.repo_materiale.lista_materiale_function()
        self.assertEqual(lista[0].denumire,"Denumire")
        self.assertEqual(lista[0].unitate_mechanica,"Unit")
        self.assertEqual(lista[0].cantitate,"1000")
        self.assertEqual(lista[0].pret,"1000")

        #Test vanzare
        denumire,cantitate,valoare=self.repo_materiale.__vanzare(0, 500)
        self.assertEqual(denumire,"Denumire")
        self.assertEqual(cantitate,"500")
        self.assertEqual(valoare,"50000")

        #Test salvare in fisier
        self.service_materiale.salvare_fisier_a_materialelor_cu_valoare(0)
        with open("fisier_cu_valoare","r") as f:
            lista=[]
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
        self.assertEqual(material.denumire, "Denumire")
        self.assertEqual(material.unitate_masura, "Unit")
        self.assertEqual(material.cantitate, "1000")
        self.assertEqual(lista[0].pret, "1000")

        self.repo_materiale.lista_materiale.clear()