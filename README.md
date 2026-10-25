# 🚀 Microsserviço de Simulação e Análise de Crédito Automotivo

Este é um microsserviço full-stack focado no setor financeiro e bancário, desenvolvido para automatizar o processo de simulação de financiamento veicular e avaliação de risco de crédito em tempo real. 

A aplicação valida parâmetros rigorosos de entrada, calcula taxas de juros compostos sobre o saldo financiado e analisa o comprometimento de renda do cliente com base em regras de negócio reais do mercado de crédito.

---

## 🛠️ Tecnologias e Ferramentas Utilizadas

### Back-End
* **Python**: Linguagem core para construção de scripts e processamento lógico.
* **FastAPI**: Framework moderno de alta performance para a construção de APIs RESTful rápidas e leves.
* **Pydantic**: Validação estrita de tipos de dados nos contratos das requisições (schemas).
* **Uvicorn**: Servidor ASGI de alta velocidade para rodar a aplicação.

### Front-End
* **HTML5 & CSS3**: Estruturação visual moderna com design responsivo (Mobile-First) em modo escuro.
* **JavaScript (Vanilla ES6+)**: Manipulação assíncrona de requisições utilizando a Fetch API para comunicação em tempo real com o servidor back-end sem recarregamento de página.

### Metodologia de Desenvolvimento e Engenharia de IA
* **Aceleração por IA**: Desenvolvimento ágil focado em engenharia de prompt avançada e arquitetura limpa. Utilização estratégica de IA para otimização lógica, refinamento de segurança e aceleração de entregas de ponta a ponta.
* **Ambiente de Desenvolvimento**: Projeto concebido, codificado, testado e estruturado inteiramente a partir de um dispositivo móvel, demonstrando adaptabilidade e alta capacidade de resolução técnica autônoma.

---

## ⚙️ Regras de Negócio Implementadas

A API processa cada simulação aplicando três filtros rígidos de aprovação:
1. **Validação da Entrada**: O sistema exige uma entrada mínima obrigatória de **20%** do valor total do veículo avaliado.
2. **Cálculo de Juros Compostos**: O saldo restante é financiado aplicando uma taxa de juros simulada de **1.5% ao mês** diluída no número de parcelas escolhido.
3. **Margem de Consignável (Comprometimento de Renda)**: O valor final da parcela mensal gerada **não pode ultrapassar 30% da renda mensal** informada pelo cliente. Caso ultrapasse, o crédito é automaticamente recusado.

---

## 📁 Estrutura do Repositório

```text
credit-analysis-microservice/
│
├── templates/
│   └── index.html      # Interface gráfica responsiva (Front-End)
│
├── main.py            # Servidor FastAPI, rotas da API e renderização
├── requirements.txt   # Dependências estruturais do projeto
└── README.md          # Documentação técnica do sistema
```

