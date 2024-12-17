from domeniu.criminal import Criminal

class ServiceDovezi:
    def __init__(self,repo_dovezi):
        self.__repo_dovezi=repo_dovezi

    def lista(self):
        return self.__repo_dovezi.lista_dovezi_function()

    def contine_string(self, string):
        lista_dovezi = self.__repo_dovezi.lista_dovezi_function()
        lista_care_contine = []
        for dovada in lista_dovezi:
            if string in dovada.suspect:
                lista_care_contine.append(dovada)
        if lista_care_contine:
            for i in range(len(lista_care_contine)):
                poz = i
                try:
                    parts = lista_care_contine[i].data.split("/")
                    data1 = 365 * int(parts[0]) + 30 * int(parts[1]) + int(parts[2])
                    for j in range(i + 1, len(lista_care_contine)):
                        parts = lista_care_contine[j].data.split("/")
                        data2 = 365 * int(parts[0]) + 30 * int(parts[1]) + int(parts[2])
                        if data1 < data2:
                            poz = j
                except (ValueError, IndexError) as e:
                    pass
                if poz != i:
                    lista_care_contine[i], lista_care_contine[poz] = lista_care_contine[poz], lista_care_contine[i]
        return lista_care_contine

    def dovezi_distincte(self):#2
        lista_dovezi=self.__repo_dovezi.lista_dovezi_function()
        lista_dovezi.sort(key=lambda item: item.suspect)
        lista_criminali=[]
        #for lista in lista_dovezi:
        #    print(f"{lista.suspect}")
        curent=1
        for i in range(1,len(lista_dovezi)):
            if lista_dovezi[i].suspect==lista_dovezi[i-1].suspect:
                curent+=1
            else:
                lista_dovezi[i-curent:i-1]=sorted(lista_dovezi[i-curent:i],key=lambda item: self.date_to_days(item.data))
                durata1=self.date_to_days(lista_dovezi[i-curent].data)
                durata2=self.date_to_days(lista_dovezi[i-1].data)
                durata=durata2-durata1
                crim=Criminal(lista_dovezi[i-1].suspect,curent,durata)
                lista_criminali.append(crim)
            lista_dovezi[i - curent:i - 1] = sorted(lista_dovezi[i - curent:i],key=lambda item: self.date_to_days(item.data))
            durata1 = self.date_to_days(lista_dovezi[i - curent].data)
            durata2 = self.date_to_days(lista_dovezi[i - 1].data)
            durata = durata2 - durata1
            crim = Criminal(lista_dovezi[i - 1].suspect, curent, durata)
            lista_criminali.append(crim)
        return lista_criminali


    def date_to_days(self,data):
        parts=data.split("/")
        return self.zile_ani(int(parts[0]))+self.zile_luni(int(parts[1]),int(parts[0]))+int(parts[2])

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
        else:
            return "Luna invalidă"





