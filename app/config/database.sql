-- Criação da tabela funcionario
CREATE TABLE funcionarios (
    matricula VARCHAR PRIMARY KEY,
    nome VARCHAR NOT NULL,
    cpf VARCHAR(11) UNIQUE NOT NULL,
    telefone VARCHAR(13)
);

-- Criação da tabela veiculos
CREATE TABLE veiculos (
    placa VARCHAR(7) PRIMARY KEY,
    modelo VARCHAR NOT NULL,
    cor VARCHAR NOT NULL,
    tipo_veiculo VARCHAR NOT NULL CHECK (tipo_veiculo IN ('carro', 'moto')),
    marca VARCHAR NOT NULL,
    matricula VARCHAR,
    CONSTRAINT fk_funcionarios FOREIGN KEY (matricula) REFERENCES funcionarios (matricula)
);

-- Criação da tabela ocorrencias
CREATE TABLE ocorrencias (
    id VARCHAR PRIMARY KEY,
    criado_em TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    motivo TEXT NOT NULL,
    foto VARCHAR NOT NULL,
    placa VARCHAR(7),
    CONSTRAINT fk_veiculo FOREIGN KEY (placa) REFERENCES veiculos (placa)
);

-- Inserção de funcionários
INSERT INTO funcionarios (matricula, nome, cpf, telefone) VALUES
('123', 'Alice Silva', '11111111111', '11999999999'),
('456', 'Bruno Souza', '22222222222', '11988888888');

-- Inserção de veículos
INSERT INTO veiculos (placa, modelo, cor, tipo_veiculo, marca, matricula) VALUES
('ABC1234', 'Civic', 'Preto', 'carro', 'Honda', '123'),
('XYZ5678', 'CG 160', 'Vermelho', 'moto', 'Honda', '456');

-- Inserção de ocorrências (exemplo de massa inicial)
INSERT INTO ocorrencias (id, motivo, foto, placa) VALUES
('ocorrencia-1', 'Estacionamento em local proibido', 'https://exemplo-s3/imagem1.jpg', 'ABC1234'),
('ocorrencia-2', 'Estacionamento em vaga de deficientes', 'https://exemplo-s3/imagem2.jpg', 'XYZ5678');
