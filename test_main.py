import unittest
from fastapi.testclient import TestClient
# Importa o app do seu arquivo main.py
from main import app

class TestAnaliseCredito(unittest.TestCase):
    
    def setUp(self):
        # O TestClient simula as requisições para a API sem precisar subir o servidor manualmente
        self.client = TestClient(app)
        self.url = "/api/v1/simulacao"

    def test_credito_aprovado_dentro_dos_parametros(self):
        """Teste para garantir que perfis ideais sejam aprovados corretamente"""
        dados = {
            "renda_mensal": 10000.0,
            "valor_veiculo": 50000.0,
            "valor_entrada": 15000.0,  # 30% de entrada (mínimo é 20%)
            "parcelas": 36
        }
        response = self.client.post(self.url, json=dados)
        self.assertEqual(response.status_code, 200)
        
        json_data = response.json()
        self.assertEqual(json_data["status"], "APROVADO")
        self.assertIn("valor_parcela", json_data["detalhes"])

    def test_recusa_por_entrada_insuficiente(self):
        """Teste para garantir que entradas menores que 20% sejam barradas"""
        dados = {
            "renda_mensal": 5000.0,
            "valor_veiculo": 50000.0,
            "valor_entrada": 5000.0,  # 10% de entrada (reprovação automática)
            "parcelas": 48
        }
        response = self.client.post(self.url, json=dados)
        self.assertEqual(response.status_code, 200)
        
        json_data = response.json()
        self.assertEqual(json_data["status"], "REPROVADO")
        self.assertIn("entrada insuficiente", json_data["motivo"].lower())

    def test_recusa_por_comprometimento_de_renda_alto(self):
        """Teste para garantir que parcelas acima de 30% da renda sejam barradas"""
        dados = {
            "renda_mensal": 2000.0,  # Renda baixa para o valor do financiamento
            "valor_veiculo": 80000.0,
            "valor_entrada": 20000.0, # 25% de entrada (válido)
            "parcelas": 12            # Poucas parcelas sobem o valor mensal
        }
        response = self.client.post(self.url, json=dados)
        self.assertEqual(response.status_code, 200)
        
        json_data = response.json()
        self.assertEqual(json_data["status"], "REPROVADO")
        self.assertIn("ultrapassa o limite", json_data["motivo"].lower())

if __name__ == "__main__":
    unittest.main()
