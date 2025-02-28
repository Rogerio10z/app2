CREATE TABLE Crianças (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(255),
    impressao_digital BLOB,  -- Para armazenar dados da impressão digital
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Presenca (
    id INT PRIMARY KEY AUTO_INCREMENT,
    crianca_id INT,
    data_presenca TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (crianca_id) REFERENCES Crianças(id)
);
