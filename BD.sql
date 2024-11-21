CREATE DATABASE CitasMedicas;

USE CitasMedicas;

CREATE TABLE Citas (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    NombrePaciente NVARCHAR(100) NOT NULL,
    Edad INT NOT NULL,
    Sexo NVARCHAR(20) NOT NULL,
    Padecimiento NVARCHAR(MAX) NOT NULL,
    Especialidad NVARCHAR(50) NOT NULL,
    FechaCreacion DATETIME DEFAULT GETDATE()
);
