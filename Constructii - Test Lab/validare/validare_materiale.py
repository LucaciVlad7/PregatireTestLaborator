from erori.errors import ValidationError

class ValidareMateriale:
    def valideaza_material(self,material):
        erori=""
        if material.id_material<0:
            erori+="Id-ul materialului nu poate fi negativ."
        if material.denumire=="" or material.denumire.islower()==True:
            erori+="Denumire invalida"
        if material.unitate_masura=="" or material.unitate_masura.islower()==True:
            erori+="Uninunitatea de masura invalida"
        if material.cantitate<=0:
            erori+="Cantitatea invalida"
        if material.pret<=0:
            erori+="Pretul invalid"
        if erori!="":
            raise ValidationError(erori)