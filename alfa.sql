/*M!999999\- enable the sandbox mode */ 
-- MariaDB dump 10.19-11.8.3-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: ALFA
-- ------------------------------------------------------
-- Server version	11.8.3-MariaDB-1+b1 from Debian

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*M!100616 SET @OLD_NOTE_VERBOSITY=@@NOTE_VERBOSITY, NOTE_VERBOSITY=0 */;

--
-- Table structure for table `clientes`
--

DROP DATABASE IF EXISTS ALFA;
CREATE DATABASE ALFA;
USE ALFA;

DROP TABLE IF EXISTS `clientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `clientes` (
  `id_cliente` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `edad` int(11) NOT NULL,
  `tot_pedidos` int(11) DEFAULT 0,
  `sexo` enum('M','F') NOT NULL DEFAULT 'M',
  PRIMARY KEY (`id_cliente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clientes`
--

LOCK TABLES `clientes` WRITE;
/*!40000 ALTER TABLE `clientes` DISABLE KEYS */;
set autocommit=0;
INSERT INTO clientes (nombre, email, edad, tot_pedidos, sexo) VALUES
('Luis', 'luis@gmail.com', 25, 0, 'M'),
('Alexis', 'alexis@hotmail.com', 28, 0, 'F'),
('Aldo', 'aldo@icloud.com', 35, 0, 'M'),
('Maria', 'maria@gmail.com', 22, 0, 'F'),
('Jose', 'jose@gmail.com', 40, 0, 'M'),
('Laura', 'laura@yahoo.com', 27, 0, 'F'),
('Fernando', 'fernando@gmail.com', 30, 0, 'M'),
('Isabel', 'isabel@hotmail.com', 31, 0, 'F'),
('Pedro', 'pedro@gmail.com', 45, 0, 'M'),
('Sofia', 'sofia@gmail.com', 20, 0, 'F');
/*!40000 ALTER TABLE `clientes` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `productos`
--

DROP TABLE IF EXISTS `productos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `productos` (
  `id_producto` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_producto` varchar(100) DEFAULT NULL,
  `stock` int(11) NOT NULL DEFAULT 0,
  `precio` decimal(10,2) DEFAULT NULL,
  `id_proveedor` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_producto`),
  KEY `fk_produ_provee` (`id_proveedor`),
  CONSTRAINT `fk_produ_provee` FOREIGN KEY (`id_proveedor`) REFERENCES `proveedores` (`id_proveedor`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `productos`
--

LOCK TABLES `productos` WRITE;
/*!40000 ALTER TABLE `productos` DISABLE KEYS */;
set autocommit=0;
INSERT INTO productos (nombre_producto, stock, precio, id_proveedor) VALUES
('Laptop HP', 40, 15000.00, 1),
('Monitor LG', 30, 5000.00, 2),
('Mouse Logitech', 100, 600.00, 3),
('Teclado Razer', 70, 1200.00, 3),
('Tablet Samsung', 25, 8500.00, 2),
('Silla ergonómica', 15, 3000.00, 8),
('Escritorio', 10, 4500.00, 8),
('Smartphone Xiaomi', 50, 7000.00, 2),
('Audífonos Sony', 60, 1800.00, 3),
('Impresora Epson', 20, 4000.00, 4),
('Zapatos deportivos', 80, 1200.00, 5),
('Camisa formal', 150, 800.00, 5),
('Cafetera Philips', 25, 2200.00, 6),
('Sofá reclinable', 8, 9500.00, 8),
('Router TP-Link', 35, 1300.00, 7),
('Monitor Curvo Samsung', 18, 7500.00, 2),
('Auriculares JBL', 55, 1500.00, 3),
('Reloj inteligente', 40, 4000.00, 2),
('Teclado mecánico', 50, 1800.00, 3),
('Mousepad RGB', 100, 500.00, 3);
/*!40000 ALTER TABLE `productos` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `proveedores`
--

DROP TABLE IF EXISTS `proveedores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `proveedores` (
  `id_proveedor` int(11) NOT NULL AUTO_INCREMENT,
  `telefono` varchar(20) DEFAULT NULL,
  `nombre_proveedor` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_proveedor`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proveedores`
--

LOCK TABLES `proveedores` WRITE;
/*!40000 ALTER TABLE `proveedores` DISABLE KEYS */;
set autocommit=0;
INSERT INTO proveedores (telefono, nombre_proveedor) VALUES
('8112345678', 'TechMex'),
('8187654321', 'ElectroPlus'),
('8199998888', 'Computodo'),
('8181122334', 'OfiLine'),
('8111122233', 'ModaExpress'),
('8123459876', 'CasaCenter'),
('8110099887', 'GadgetsPro'),
('8198877665', 'MueblesMX');
/*!40000 ALTER TABLE `proveedores` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `ventas`
--

DROP TABLE IF EXISTS `ventas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `ventas` (
  `id_venta` int(11) NOT NULL AUTO_INCREMENT,
  `id_producto` int(11) DEFAULT NULL,
  `id_cliente` int(11) DEFAULT NULL,
  `total_articulos` int(11) DEFAULT NULL,
  `total_venta` decimal(10,2) DEFAULT NULL,
  `fecha_venta` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id_venta`),
  KEY `fk_ventas_producto` (`id_producto`),
  KEY `fk_ventas_cliente` (`id_cliente`),
  CONSTRAINT `fk_ventas_cliente` FOREIGN KEY (`id_cliente`) REFERENCES `clientes` (`id_cliente`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `fk_ventas_producto` FOREIGN KEY (`id_producto`) REFERENCES `productos` (`id_producto`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ventas`
--

LOCK TABLES `ventas` WRITE;
/*!40000 ALTER TABLE `ventas` DISABLE KEYS */;
set autocommit=0;
INSERT INTO ventas (id_producto, id_cliente, total_articulos, total_venta, fecha_venta) VALUES
(1, 1, 1, 15000.00, '2025-10-01 09:15:00'),
(2, 2, 2, 10000.00, '2025-10-02 10:20:00'),
(3, 3, 3, 1800.00, '2025-10-03 11:10:00'),
(4, 4, 1, 1200.00, '2025-10-04 12:45:00'),
(5, 5, 1, 8500.00, '2025-10-05 14:30:00'),
(6, 6, 2, 6000.00, '2025-10-06 15:15:00'),
(7, 7, 1, 4500.00, '2025-10-07 16:05:00'),
(8, 8, 2, 14000.00, '2025-10-08 17:25:00'),
(9, 9, 1, 1800.00, '2025-10-09 18:15:00'),
(10, 10, 1, 4000.00, '2025-10-10 19:40:00'),
(11, 1, 3, 3600.00, '2025-10-11 10:35:00'),
(12, 2, 4, 3200.00, '2025-10-12 11:50:00'),
(13, 3, 2, 4400.00, '2025-10-13 13:05:00'),
(14, 4, 1, 9500.00, '2025-10-14 14:55:00'),
(15, 5, 2, 2600.00, '2025-10-15 16:10:00'),
(16, 6, 1, 7500.00, '2025-10-16 17:45:00'),
(17, 7, 2, 3000.00, '2025-10-17 18:50:00'),
(18, 8, 1, 4000.00, '2025-10-18 19:20:00'),
(19, 9, 1, 1800.00, '2025-10-19 20:30:00'),
(20, 10, 2, 1000.00, '2025-10-20 09:40:00'),
(1, 3, 1, 15000.00, '2025-10-21 10:25:00'),
(4, 7, 2, 2400.00, '2025-10-22 11:15:00'),
(5, 8, 1, 8500.00, '2025-10-23 12:00:00'),
(9, 5, 3, 5400.00, '2025-10-24 13:45:00'),
(2, 9, 1, 5000.00, '2025-10-25 15:00:00'),
(8, 6, 2, 14000.00, '2025-10-26 16:20:00'),
(7, 4, 1, 4500.00, '2025-10-27 17:35:00'),
(13, 2, 2, 4400.00, '2025-10-28 18:25:00'),
(15, 1, 1, 1300.00, '2025-10-29 19:10:00'),
(19, 10, 1, 1800.00, '2025-10-30 20:00:00');

COMMIT;
/*!40000 ALTER TABLE `ventas` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Dumping routines for database 'ALFA'
--

/*!50003 DROP FUNCTION IF EXISTS `fn_calcular_total_con_iva` */;
DELIMITER ;;
CREATE FUNCTION `fn_calcular_total_con_iva`(
    in_precio_unitario DECIMAL(10, 2),
    in_cantidad INT
) 
RETURNS DECIMAL(10, 2)
DETERMINISTIC
BEGIN
    DECLARE v_subtotal DECIMAL(10, 2);
    DECLARE v_total_con_iva DECIMAL(10, 2);
    
    SET v_subtotal = in_precio_unitario * in_cantidad;
    SET v_total_con_iva = v_subtotal * 1.16; -- Se aplica el 16% de IVA
    
    RETURN v_total_con_iva;
END ;;
DELIMITER ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */;
/*!50003 DROP PROCEDURE IF EXISTS `sp_crear_venta` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_crear_venta`(
    IN in_id_cliente INT,
    IN in_id_producto INT,
    IN in_cantidad INT,
    OUT out_id_venta INT  
)
BEGIN
    
    DECLARE v_stock_actual INT;
    DECLARE v_precio_producto DECIMAL(10, 2);
    DECLARE v_total_venta DECIMAL(10, 2);
    DECLARE v_cliente_existe INT;

    
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        
        ROLLBACK;
        
        RESIGNAL; 
    END;
    
    START TRANSACTION;

    SELECT COUNT(*) INTO v_cliente_existe FROM clientes WHERE id_cliente = in_id_cliente;
    IF v_cliente_existe = 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error: El cliente no existe.';
    END IF;

    
    
    SELECT 
        stock, precio 
    INTO 
        v_stock_actual, v_precio_producto 
    FROM 
        productos 
    WHERE 
        id_producto = in_id_producto 
    FOR UPDATE;

    
    IF v_precio_producto IS NULL THEN
        
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error: Producto no encontrado.';
    ELSEIF v_stock_actual < in_cantidad THEN
        
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error: No hay stock suficiente.';
    END IF;

    
    SET v_total_venta = fn_calcular_total_con_iva(v_precio_producto, in_cantidad);

    
    INSERT INTO ventas (id_cliente, id_producto, total_articulos, total_venta, fecha_venta) 
    VALUES (in_id_cliente, in_id_producto, in_cantidad, v_total_venta, NOW());

    
    SET out_id_venta = LAST_INSERT_ID();

    
    UPDATE productos 
    SET stock = stock - in_cantidad 
    WHERE id_producto = in_id_producto;

    
    UPDATE clientes 
    SET tot_pedidos = tot_pedidos + 1 
    WHERE id_cliente = in_id_cliente;

    
    COMMIT;

END ;;
DELIMITER ;

/*!50003 DROP PROCEDURE IF EXISTS `sp_insertar_cliente` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_insertar_cliente`(
    IN in_nombre VARCHAR(100),
    IN in_email VARCHAR(100),
    IN in_edad INT,
    IN in_sexo ENUM('M', 'F'),
    OUT out_id_cliente INT
)
BEGIN
    DECLARE EXIT HANDLER FOR 1062
    BEGIN
        ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error: El correo electrónico ya está registrado.';
    END;

    START TRANSACTION;
    
    INSERT INTO clientes (nombre, email, edad, sexo) 
    VALUES (in_nombre, in_email, in_edad, in_sexo);
    
    SET out_id_cliente = LAST_INSERT_ID();
    
    COMMIT;
END ;;
DELIMITER ;

/*!50003 DROP PROCEDURE IF EXISTS `sp_reporte_clientes` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_reporte_clientes`()
BEGIN
    SELECT 
        id_cliente,
        nombre,
        email,
        edad,
        tot_pedidos,
        sexo,
        fn_calcular_gasto_total_cliente(id_cliente) AS Gasto_Total
    FROM clientes 
    ORDER BY nombre;
END ;;
DELIMITER ;

/*!50003 DROP PROCEDURE IF EXISTS `sp_actualizar_cliente_nombre` */;
DELIMITER ;;
CREATE PROCEDURE `sp_actualizar_cliente_nombre`(
    IN in_id_cliente INT,
    IN in_nuevo_nombre VARCHAR(100)
)
BEGIN
    UPDATE clientes SET nombre = in_nuevo_nombre WHERE id_cliente = in_id_cliente;
END ;;
DELIMITER ;

/*!50003 DROP PROCEDURE IF EXISTS `sp_actualizar_cliente_email` */;
DELIMITER ;;
CREATE PROCEDURE `sp_actualizar_cliente_email`(
    IN in_id_cliente INT,
    IN in_nuevo_email VARCHAR(100)
)
BEGIN
    UPDATE clientes SET email = in_nuevo_email WHERE id_cliente = in_id_cliente;
END ;;
DELIMITER ;

/*!50003 DROP PROCEDURE IF EXISTS `sp_actualizar_cliente_edad` */;
DELIMITER ;;
CREATE PROCEDURE `sp_actualizar_cliente_edad`(
    IN in_id_cliente INT,
    IN in_nuevo_edad INT
)
BEGIN
    UPDATE clientes SET edad = in_nuevo_edad WHERE id_cliente = in_id_cliente;
END ;;
DELIMITER ;

/*!50003 DROP PROCEDURE IF EXISTS `sp_actualizar_cliente_sexo` */;
DELIMITER ;;
CREATE PROCEDURE `sp_actualizar_cliente_sexo`(
    IN in_id_cliente INT,
    IN in_nuevo_sexo ENUM('M', 'F')
)
BEGIN
    UPDATE clientes SET sexo = in_nuevo_sexo WHERE id_cliente = in_id_cliente;
END ;;
DELIMITER ;

/*!50003 DROP PROCEDURE IF EXISTS `sp_insertar_proveedor` */;
DELIMITER ;;
CREATE PROCEDURE `sp_insertar_proveedor`(
    IN in_telefono VARCHAR(20),
    IN in_nombre VARCHAR(100),
    OUT out_id_proveedor INT
)
BEGIN
    DECLARE EXIT HANDLER FOR 1062 -- Telefono duplicado
    BEGIN
        ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error: El teléfono ya está registrado.';
    END;

    START TRANSACTION;
    INSERT INTO proveedores (telefono, nombre_proveedor) 
    VALUES (in_telefono, in_nombre);
    SET out_id_proveedor = LAST_INSERT_ID();
    COMMIT;
END ;;
DELIMITER ;

/*!50003 DROP PROCEDURE IF EXISTS `sp_reporte_ventas_general` */;
DELIMITER ;;
CREATE PROCEDURE `sp_reporte_ventas_general`()
BEGIN
    SELECT 
        v.id_venta, 
        c.nombre AS Cliente, 
        p.nombre_producto AS Producto, 
        v.total_articulos, 
        v.total_venta, 
        v.fecha_venta
    FROM ventas v
    JOIN clientes c ON v.id_cliente = c.id_cliente
    JOIN productos p ON v.id_producto = p.id_producto
    ORDER BY v.fecha_venta DESC;
END ;;
DELIMITER ;

/*!50003 DROP PROCEDURE IF EXISTS `sp_consultar_ventas_cliente_fecha` */;
DELIMITER ;;
CREATE PROCEDURE `sp_consultar_ventas_cliente_fecha`(
    IN in_id_cliente INT,
    IN in_fecha_inicio DATE
)
BEGIN
    SELECT 
        v.id_venta, 
        p.nombre_producto, 
        v.total_articulos, 
        v.total_venta, 
        v.fecha_venta
    FROM ventas v
    JOIN clientes c ON v.id_cliente = c.id_cliente
    JOIN productos p ON v.id_producto = p.id_producto
    WHERE 
        c.id_cliente = in_id_cliente
        AND DATE(v.fecha_venta) >= in_fecha_inicio
    ORDER BY v.fecha_venta DESC;
END ;;
DELIMITER ;

/*!50003 DROP PROCEDURE IF EXISTS `sp_reporte_productos_en_stock` */;
DELIMITER ;;
CREATE PROCEDURE `sp_reporte_productos_en_stock`()
BEGIN
    SELECT * FROM productos WHERE stock > 0 ORDER BY nombre_producto;
END ;;
DELIMITER ;

/*!50003 DROP FUNCTION IF EXISTS `fn_calcular_gasto_total_cliente` */;
DELIMITER ;;
CREATE FUNCTION `fn_calcular_gasto_total_cliente`(
    in_id_cliente INT
) 
RETURNS DECIMAL(10, 2)
DETERMINISTIC
READS SQL DATA
BEGIN
    DECLARE v_total_gastado DECIMAL(10, 2);
    
    SELECT SUM(total_venta) 
    INTO v_total_gastado 
    FROM ventas 
    WHERE id_cliente = in_id_cliente;
    
    IF v_total_gastado IS NULL THEN
        RETURN 0.00;
    END IF;
    
    RETURN v_total_gastado;
END ;;
DELIMITER ;

/*!50003 DROP FUNCTION IF EXISTS `fn_formatear_moneda` */;
DELIMITER ;;
CREATE FUNCTION `fn_formatear_moneda`(
    in_valor DECIMAL(10, 2)
) 
RETURNS VARCHAR(20)
DETERMINISTIC
BEGIN
    RETURN CONCAT('$', FORMAT(in_valor, 2));
END ;;
DELIMITER ;



/*!50003 DROP PROCEDURE IF EXISTS `sp_actualizar_producto_nombre` */;
DELIMITER ;;
CREATE PROCEDURE `sp_actualizar_producto_nombre`(
    IN in_id_producto INT,
    IN in_nuevo_nombre VARCHAR(100)
)
BEGIN
    UPDATE productos SET nombre_producto = in_nuevo_nombre 
    WHERE id_producto = in_id_producto;
END ;;
DELIMITER ;

/*!50003 DROP PROCEDURE IF EXISTS `sp_actualizar_producto_stock` */;
DELIMITER ;;
CREATE PROCEDURE `sp_actualizar_producto_stock`(
    IN in_id_producto INT,
    IN in_nuevo_stock INT
)
BEGIN
    UPDATE productos SET stock = in_nuevo_stock 
    WHERE id_producto = in_id_producto;
END ;;
DELIMITER ;

/*!50003 DROP PROCEDURE IF EXISTS `sp_actualizar_producto_precio` */;
DELIMITER ;;
CREATE PROCEDURE `sp_actualizar_producto_precio`(
    IN in_id_producto INT,
    IN in_nuevo_precio DECIMAL(10, 2)
)
BEGIN
    UPDATE productos SET precio = in_nuevo_precio 
    WHERE id_producto = in_id_producto;
END ;;
DELIMITER ;


/*!50003 DROP PROCEDURE IF EXISTS `sp_reporte_stock` */;
DELIMITER ;;
CREATE PROCEDURE `sp_reporte_stock`()
BEGIN
    SELECT 
        id_producto,
        nombre_producto,
        stock,
        fn_formatear_moneda(precio) AS precio,
        id_proveedor
    FROM productos
    ORDER BY nombre_producto;
END ;;
DELIMITER ;


/*!50003 DROP PROCEDURE IF EXISTS `sp_actualizar_proveedor_telefono` */;
DELIMITER ;;
CREATE PROCEDURE `sp_actualizar_proveedor_telefono`(
    IN in_id_proveedor INT,
    IN in_nuevo_telefono VARCHAR(20)
)
BEGIN
    UPDATE proveedores SET telefono = in_nuevo_telefono 
    WHERE id_proveedor = in_id_proveedor;
END ;;
DELIMITER ;

/*!50003 DROP PROCEDURE IF EXISTS `sp_actualizar_proveedor_nombre` */;
DELIMITER ;;
CREATE PROCEDURE `sp_actualizar_proveedor_nombre`(
    IN in_id_proveedor INT,
    IN in_nuevo_nombre VARCHAR(100)
)
BEGIN
    UPDATE proveedores SET nombre_proveedor = in_nuevo_nombre 
    WHERE id_proveedor = in_id_proveedor;
END ;;
DELIMITER ;


/*!50003 DROP PROCEDURE IF EXISTS `sp_reporte_proveedores` */;
DELIMITER ;;
CREATE PROCEDURE `sp_reporte_proveedores`()
BEGIN
    SELECT * FROM proveedores ORDER BY nombre_proveedor;
END ;;
DELIMITER ;

/*!50003 DROP PROCEDURE IF EXISTS `sp_actualizar_producto_proveedor` */;
DELIMITER ;;
CREATE PROCEDURE `sp_actualizar_producto_proveedor`(
    IN in_id_producto INT,
    IN in_nuevo_id_proveedor INT
)
BEGIN
    DECLARE v_id_proveedor INT;

    IF in_nuevo_id_proveedor = 0 THEN
        SET v_id_proveedor = NULL;
    ELSE
        SET v_id_proveedor = in_nuevo_id_proveedor;
    END IF;

    IF v_id_proveedor IS NOT NULL AND (SELECT COUNT(*) FROM proveedores WHERE id_proveedor = v_id_proveedor) = 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error: El proveedor con ese ID no existe.';
    END IF;

    UPDATE productos SET id_proveedor = v_id_proveedor 
    WHERE id_producto = in_id_producto;
END ;;
DELIMITER ;

/*!50003 DROP PROCEDURE IF EXISTS `sp_insertar_producto` */;
DELIMITER ;;
CREATE PROCEDURE `sp_insertar_producto`(
    IN in_nombre VARCHAR(100),
    IN in_stock INT,
    IN in_precio DECIMAL(10, 2),
    IN in_id_proveedor INT,
    OUT out_id_producto INT
)
BEGIN
    DECLARE v_id_proveedor INT;

    IF in_id_proveedor = 0 THEN
        SET v_id_proveedor = NULL;
    ELSE
        SET v_id_proveedor = in_id_proveedor;
    END IF;

    IF v_id_proveedor IS NOT NULL AND (SELECT COUNT(*) FROM proveedores WHERE id_proveedor = v_id_proveedor) = 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error: El proveedor con ese ID no existe.';
    END IF;
    
    START TRANSACTION;
    INSERT INTO productos (nombre_producto, stock, precio, id_proveedor)
    VALUES (in_nombre, in_stock, in_precio, v_id_proveedor);
    SET out_id_producto = LAST_INSERT_ID();
    COMMIT;
END;;
DELIMITER ;

/*!50003 DROP PROCEDURE IF EXISTS `sp_eliminar_cliente` */;
DELIMITER ;;
CREATE PROCEDURE `sp_eliminar_cliente`(
    IN in_id_cliente INT
)
BEGIN
    DELETE FROM clientes WHERE id_cliente = in_id_cliente;
END;;
DELIMITER ;

/*!50003 DROP PROCEDURE IF EXISTS `sp_eliminar_producto` */;
DELIMITER ;;
CREATE PROCEDURE `sp_eliminar_producto`(
    IN in_id_producto INT
)
BEGIN
    DELETE FROM productos WHERE id_producto = in_id_producto;
END;;
DELIMITER ;

/*!50003 DROP PROCEDURE IF EXISTS `sp_eliminar_proveedor` */;
DELIMITER ;;
CREATE PROCEDURE `sp_eliminar_proveedor`(
    IN in_id_proveedor INT
)
BEGIN
    DELETE FROM proveedores WHERE id_proveedor = in_id_proveedor;
END;;

DELIMITER ;

/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*M!100616 SET NOTE_VERBOSITY=@OLD_NOTE_VERBOSITY */;

-- Dump completed on 2025-11-06 16:51:38
