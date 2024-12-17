from business.service_materiale import ServiceMateriale
from repo.repo_materiale import Repo_materiale
from ui.consola import Consola
from Teste.teste_material import Test
from validare.validare_materiale import ValidareMateriale

#Testele nu merg

repo = Repo_materiale("repo/materiale")
validare=ValidareMateriale()
service = ServiceMateriale(repo,validare)
consola = Consola(service)
teste = Test()
teste.ruleaza_toate_testele()

consola.run()