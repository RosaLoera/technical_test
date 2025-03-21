
CREATE TABLE Usuarios (
	id int,
	nombre varchar(255),
	email varchar(255),
	fecha_de_registro date
);



INSERT INTO
	Usuarios (id, nombre, email, fecha_de_registro)
VALUES
	(1, 'Juan López', 'juan.lopez@gmail.com', '2025-03-21'),
	(2, 'Sandra Marín', 'sandra.marin@gmail.com', '2025-03-03'),
	(3, 'Luisa Gómez', 'luisa.gomez@gmail.com', '2025-02-07');

select * from Usuarios;
