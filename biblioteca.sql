CREATE DATABASE biblioteca
CREATE TABLE livros(
    titulo varchar(255) NOT NULL,
    autor varchar(255) NOT NULL,
    genero varchar(255) NOT NULL,
    quantidade int NOT NULL,
    prateleira varchar(255),
    codigo int)