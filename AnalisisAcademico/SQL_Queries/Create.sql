CREATE TABLE IF NOT EXISTS cursos_tmp (
    anyo INT,
    curso BIGINT PRIMARY KEY,
    texto VARCHAR(500),
    padre BIGINT
);
CREATE TABLE IF NOT EXISTS modulos_tmp (
    anyo INT,
    curso BIGINT,
    codigo VARCHAR(100),
    nombre VARCHAR(500)
);
CREATE TABLE IF NOT EXISTS modulos (
    anyo INT,
    curso_id BIGINT,
    modulo_codigo VARCHAR(100),
    modulo_nombre VARCHAR(500),
    curso_nombre VARCHAR(500),
    curso_padre BIGINT,
    curso_padre_nombre VARCHAR(500)
);
CREATE TABLE IF NOT EXISTS alumnos (
    anyo INT,
    NIA VARCHAR(200) PRIMARY KEY,
    fecha_nac DATE,
    sexo CHAR(1),
    estado_matricula CHAR(1),
    curso BIGINT,
    grupo VARCHAR(50),
    turno VARCHAR(50)
);
CREATE TABLE IF NOT EXISTS calificaciones (
    anyo INT,
    evaluacion INT,
    alumno VARCHAR(200),
    ensenanza INT,
    curso BIGINT,
    nota DECIMAL(10,2)
);
