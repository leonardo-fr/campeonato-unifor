import unittest
from unittest.mock import patch
from io import StringIO
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

#Importa a função main
from main import main

#Cria uma classe de teste para verificar se a main finalizou corretamente
class MainTest(unittest.TestCase):
    #Entrada de 85 para simular uma pontuacao mínima
    @patch('builtins.input', side_effect=[85, 's', 1])
    #Serve para capturar o que seria exibido no console
    @patch('sys.stdout', new_callable=StringIO)

    def test_main_function_output(self, mock_stdout, _):
        main()
        
        #Captura a saída simulada gerada
        output = mock_stdout.getvalue()
        
        #Serve para indicar que o programa chegou ao final de sua execução
        self.assertIn("#################( PROGRAMA ENCERRADO! )#####################", output)

    print("a Main() foi executada com sucesso!")

if __name__ == "__main__":
    unittest.main()
