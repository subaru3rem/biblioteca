CREATE DATABASE biblioteca
CREATE TABLE livros(
    id int PRIMARY KEY AUTO_INCREMENT,
    titulo varchar(255) NOT NULL,
    autor varchar(255) NOT NULL,
    genero varchar(255) NOT NULL,
    quantidade int NOT NULL)