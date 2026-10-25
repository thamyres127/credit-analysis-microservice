-- Criação da tabela de propostas de crédito automotivo
CREATE TABLE propostas_credito (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cpf_cliente VARCHAR(14) NOT NULL,
    renda_mensal DECIMAL(12, 2) NOT NULL,
    valor_veiculo DECIMAL(12, 2) NOT NULL,
    valor_entrada DECIMAL(12, 2) NOT NULL,
    valor_financiado DECIMAL(12, 2) NOT NULL,
    quantidade_parcelas INT NOT NULL,
    valor_parcela_calculada DECIMAL(12, 2) NOT NULL,
    status_analise VARCHAR(20) NOT NULL, -- 'APROVADO' ou 'REPROVADO'
    motivo_recusa TEXT,                  -- Preenchido apenas se for reprovado
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Índices para otimização de buscas (Bancos adoram isso para performance!)
CREATE INDEX idx_cpf_cliente ON propostas_credito(cpf_cliente);
CREATE INDEX idx_status_analise ON propostas_credito(status_analise);
