class Teste:
    def __init__(self,repo,service):
        self.__repo_tari=repo
        self.__service_tari=service

    def ruleaza_toate_testele(self):
        #Test adauga service + repo
        assert len(self.__repo_tari.lista_tari_function())==6
        self.__service_tari.adauga_service("Romania",2014,1.5,2.5,"25_000_000")
        lista=self.__repo_tari.lista_tari_function()
        assert len(lista)==7

        #Teste rata Inflatie service
        lista=self.__service_tari.rata_medie_de_inflatie(1.0)
        assert lista[0].nume=="Danemarca"

        #Test Repo
        self.__repo_tari.adauga_tara("Ungaria",2022,7.9,100,"10_000_000")
        assert len(self.__repo_tari.lista_tari_function())==8

        #Test validari