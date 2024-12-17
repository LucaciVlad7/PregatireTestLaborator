from infrastructura.RepoTari import RepoTari
from business.service_tari import ServiceTari
from prezentare.ui import Consola
from teste.teste_tari import Teste
from validator.validator_tari import ValidatorTari

validare=ValidatorTari()
repo=RepoTari("infrastructura/Tari.txt")
service=ServiceTari(repo,validare)
test=Teste(repo,service)
test.ruleaza_toate_testele()

consola=Consola(service)
consola.run()