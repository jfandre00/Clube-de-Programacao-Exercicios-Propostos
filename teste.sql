CREATE TABLE VendasEletronicos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_vendedor TEXT NOT NULL,
    cpf_vendedor TEXT NOT NULL,
    email_vendedor TEXT NOT NULL,
    produto TEXT NOT NULL,
    quantidade INTEGER NOT NULL,
    preco_unitario REAL NOT NULL,
    data_venda DATE NOT NULL
);

INSERT INTO VendasEletronicos (nome_vendedor, cpf_vendedor, email_vendedor, produto, quantidade, preco_unitario, data_venda) VALUES
('Carlos Santos', '654.987.321-00', 'carlos.santos@email.com', 'Smartphone', 5, 999.90, '2023-05-11'),
('Fernanda Rocha', '852.456.123-99', 'fernanda.rocha@email.com', 'Notebook', 2, 3499.90, '2023-05-12'),
('Rafael Lima', '789.654.321-22', 'rafael.lima@email.com', 'Televisor', 1, 1499.90, '2023-05-15'),
('Lucia Almeida', '159.753.486-12', 'lucia.almeida@email.com', 'Tablet', 4, 599.90, '2023-05-20'),
('Eduardo Costa', '321.987.654-31', 'eduardo.costa@email.com', 'Câmera', 3, 1999.90, '2023-06-01'),
('Mariana Ferreira', '753.159.258-78', 'mariana.ferreira@email.com', 'Fone de Ouvido', 10, 149.90, '2023-06-05'),
('Gustavo Nascimento', '258.951.357-65', 'gustavo.nascimento@email.com', 'Monitor', 2, 899.90, '2023-06-10'),
('Patrícia Gomes', '852.147.963-84', 'patricia.gomes@email.com', 'Impressora', 1, 499.90, '2023-06-15'),
('Felipe Martins', '369.852.741-47', 'felipe.martins@email.com', 'Home Theater', 1, 1299.90, '2023-06-20'),
('Isabella Moreira', '963.258.741-96', 'isabella.moreira@email.com', 'Data Show', 1, 1799.90, '2023-06-25');

select nome_vendedor
from VendasEletronicos
where data_venda between '2023-06-01' and '2023-06-20';