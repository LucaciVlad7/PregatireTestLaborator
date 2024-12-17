from domeniu.dovezi import Dovada

class RepoDovezi:
    def __init__(self,cale_fisier):
        self.__cale_fisier = cale_fisier
        self.lista_dovezi = []
        self.__citeste_tot_din_fisier()

    def lista_dovezi_function(self):
        return self.lista_dovezi

    def __citeste_tot_din_fisier(self):
        with open(self.__cale_fisier, 'r') as f:
            self.lista_dovezi.clear()
            linii=f.readlines()
            for linie in linii:
                linie=linie.strip()
                if linie!="":
                    parts=linie.split(",")
                    id_dovada=int(parts[0])
                    descriere=parts[1]
                    data=parts[2]
                    tip=parts[3]
                    suspect=parts[4]
                    dovada=Dovada(id_dovada,descriere,data,tip,suspect)
                    self.lista_dovezi.append(dovada)