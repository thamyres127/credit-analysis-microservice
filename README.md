# Simulação e Análise de Crédito Automotivo 🚀

Este é um projeto full-stack focado no ecossistema financeiro e bancário, desenvolvido para simular a esteira automatizada de aprovação e análise de risco para financiamento veicular.

O projeto foi desenhado seguindo os conceitos de **Sistemas Distribuídos** e **Microsserviços**, simulando o padrão de grandes instituições financeiras (onde sistemas centrais em **Java/Spring Boot** realizam a orquestração de contratos e conversam com microsserviços especializados em **Python** para cálculos de risco).

---

## 🎮 Como Testar o Projeto (Demonstração Online)

Para facilitar a avaliação e garantir acessibilidade total, o projeto conta com uma arquitetura híbrida de execução:

### 🔗 Opção 1: Demonstração Direta (GitHub Pages)
Você pode testar a interface visual e as regras de negócio agora mesmo, diretamente pelo navegador do seu celular ou computador. O Front-End possui uma **lógica espelho em JavaScript** que assume o processamento das regras de crédito caso o servidor principal em Python esteja offline, garantindo resiliência e funcionamento 100% autônomo da aplicação.

### 💻 Opção 2: Execução do Back-End Completo (GitHub Codespaces)
Se você for um avaliador técnico e desejar rodar o motor nativo em Python (FastAPI), utilize o ambiente em nuvem oficial embutido no repositório:

1. Clique no botão de inicialização do Codespaces.
2. Aguarde a inicialização automática do ambiente (`.devcontainer`) e das dependências.
3. No terminal inferior do Codespaces, inicie o servidor:
```bash
uvicorn main:app --reload
```

---

## 🛠️ Tecnologias e Camadas do Projeto

### Camada de Inteligência e API (Back-End)
*   **Python**: Processamento central das regras de dados.
*   **FastAPI**: Framework assíncrono de alta performance para a disponibilização dos endpoints RESTful.
*   **Pydantic**: Validação estrita e tipagem dos contratos de entrada de dados (schemas).

### Camada de Apresentação e Simulação Local (Front-End)
*   **HTML5 & CSS3**: Interface gráfica limpa, moderna e responsiva baseada nas paletas suaves das Fintechs atuais.
*   **JavaScript (Vanilla ES6+)**: Consumo assíncrono da API (Fetch API) e motor de contingência local para simular as regras de risco diretamente no cliente.

### Engenharia de Prompt e Desenvolvimento Ágil
*   **Aceleração por IA**: Utilização avançada e estratégica de IA (engenharia de contexto e prompts estruturados) para ganho de eficiência no design lógico e na segurança do código.
*   **Desenvolvimento Mobile-First**: Todo o esqueleto, lógica, testes e deploy do ecossistema foram concebidos de forma autônoma a partir de um dispositivo móvel.

---

## ⚙️ Regras de Negócio Financeiras Implementadas

O motor de análise avalia a proposta recebida através de três critérios rígidos:

1.  **Filtro de Entrada Mínima**: O valor da entrada deve corresponder a, no mínimo, **20%** do valor de tabela do veículo.
2.  **Amortização e Juros Compostos**: O saldo devedor é calculado aplicando uma taxa de juros simulada de **1.5% ao mês** distribuída no prazo de parcelamento selecionado.
3.  **Margem Consignável (Comprometimento de Renda)**: O valor da parcela gerada não pode ultrapassar o teto de **30%** da renda mensal informada pelo cliente. Caso ultrapasse, o crédito é imediatamente recusado por risco de inadimplência.

---

## 📁 Estrutura Estrutural do Repositório

```text
credit-analysis-microservice/
├── .devcontainer/
│   └── devcontainer.json  # Configuração de ambiente GitHub Codespaces
├── database.sql           # Script de estrutura do banco de dados relacional
├── index.html             # Interface visual (Front-End) e lógica de contingência
├── main.py                # Servidor API principal e rotas do FastAPI
├── requirements.txt       # Manifesto de dependências do ambiente Python
├── test_main.py           # Bateria de testes unitários automatizados
└── README.md              # Documentação oficial do projeto
```
