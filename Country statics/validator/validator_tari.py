from exceptii.erori import ValidationError

class ValidatorTari:
    def validator_tari(self,tara):
        #presupun ca infatie si rata somaj e >1.0
        erori=""
        if tara.nume=="":
            erori+="Nume invalid"
        if tara.inflatie<1.0:
            erori+="Infatie invalid"
        if tara.somaj<1.0:
            erori+="Rata invalid"
        parts=tara.populatie.split("_")
        pop=0
        for i in range(len(parts)):
            pop=pop+int(parts[i])*1000
        pop=pop/1000
        if pop<=0:
            erori+="Populatie invalid"
        if erori!="":
            raise ValidationError(erori)