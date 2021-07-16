import os
from json import load
from unittest import TestCase

try:
    from AG.Populacao import Populacao
    from AG.Individuo import Individuo
    from Trafo.CONSTANTES import VARIACOES, CONSTANTES_DADAS
    from Trafo.trafo import Trafo

except ImportError as error:
    print(f"Erro no import em {__name__}: {error}")
    #import ipdb; ipdb.set_trace()
    from .AG.Individuo import Individuo
    from .Trafo.trafo import Trafo

try:
    from .utils import erro_e_aceitavel, print_dict
except:
    from utils import erro_e_aceitavel, print_dict


class Teste_AG_Subproblema(TestCase):
    def setUp(self):
        self.pathjson = "tests/json/AG/"
        self.config = load(open("tests/config.json", "r"))
        self.teste = self.pathjson + f"teste_{self.config['n']}.json"
        self.json = load(open(self.teste))
        variaveis = self.json["variaveis"]
        self.variaveis = dict(zip(VARIACOES.keys(), variaveis))
        self.erro_aceitavel = self.config["error"]
        self.numero_populacao = self.config["npop"]

    def __teste(self):
        pass
