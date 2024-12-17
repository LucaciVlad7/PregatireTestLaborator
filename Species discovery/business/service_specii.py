class ServiceSpecii:
    def __init__(self,repo):
        self.__repo_specii=repo

    def before_date(self, date):
        lista_specii = self.__repo_specii.lista_specii_function()
        lista_valide=[]
        for specie in lista_specii:
            parts=specie.data.split("/")
            an=int(parts[0])
            luna=int(parts[1])
            zi=int(parts[2])
            data_lista=zi+self.zile_luni(luna,an)+self.zile_ani(an)
            parts=date.split("/")
            an = int(parts[0])
            luna = int(parts[1])
            zi = int(parts[2])
            data=zi+self.zile_luni(luna,an)+self.zile_ani(an)
            if data_lista<data:
                lista_valide.append(specie)
        return lista_valide

    def zile_ani(self,an):
        ani_bisecti=an//4-an//100+an//400
        ani_normali=an-ani_bisecti
        return ani_bisecti*366+ani_normali*365

    def zile_luni(self, luna, an):
        if luna == 1:  # Ianuarie
            return 31
        elif luna == 2:  # Februarie
            if an % 4 == 0 and (an % 100 != 0 or an % 400 == 0):
                return 29
            else:
                return 28
        elif luna == 3:  # Martie
            return 31
        elif luna == 4:  # Aprilie
            return 30
        elif luna == 5:  # Mai
            return 31
        elif luna == 6:  # Iunie
            return 30
        elif luna == 7:  # Iulie
            return 31
        elif luna == 8:  # August
            return 31
        elif luna == 9:  # Septembrie
            return 30
        elif luna == 10:  # Octombrie
            return 31
        elif luna == 11:  # Noiembrie
            return 30
        elif luna == 12:  # Decembrie
            return 31
        return 0


