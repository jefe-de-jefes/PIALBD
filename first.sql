/*M!999999\- enable the sandbox mode */ 
-- MariaDB dump 10.19-11.8.3-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: First
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

CREATE DATABASE IF NOT EXISTS First;
USE First;

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
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clientes`
--

LOCK TABLES `clientes` WRITE;
/*!40000 ALTER TABLE `clientes` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `clientes` VALUES
(15,'Luis Fernando','luis@gmail.com',19,0,'M'),
(16,'Beto','beto@icloud.com',20,1,'M'),
(17,'Aldo','aldo@hotmail.com',30,1,'M');
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
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `productos`
--

LOCK TABLES `productos` WRITE;
/*!40000 ALTER TABLE `productos` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `productos` VALUES
(1,'Laptop',49,15000.00,NULL),
(2,'PC',95,20000.00,NULL),
(3,'Phone',200,10000.00,NULL),
(4,'Tablet',25,10000.00,NULL),
(5,'Desk',10,6000.00,NULL),
(6,'Shoes',495,2000.00,NULL),
(7,'Hat',200,3000.00,NULL),
(8,'Router',60,50000.00,NULL),
(9,'Car',6,800000.00,NULL);
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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proveedores`
--

LOCK TABLES `proveedores` WRITE;
/*!40000 ALTER TABLE `proveedores` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `proveedores` VALUES
(1,'1234567890','Muebleriasa'),
(2,'1987654321','Samsung');
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
  CONSTRAINT `fk_ventas_cliente` FOREIGN KEY (`id_cliente`) REFERENCES `clientes` (`id_cliente`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_ventas_producto` FOREIGN KEY (`id_producto`) REFERENCES `productos` (`id_producto`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ventas`
--

LOCK TABLES `ventas` WRITE;
/*!40000 ALTER TABLE `ventas` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `ventas` VALUES
(3,1,16,1,15000.00,'2025-08-31 20:46:51'),
(4,6,17,5,10000.00,'2025-11-06 22:36:37');
/*!40000 ALTER TABLE `ventas` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Dumping routines for database 'First'
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
    SELECT * FROM clientes ORDER BY nombre;
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
    COMMIT;
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
    COMMIT;
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
    COMMIT;
END ;;
DELIMITER ;

/*!50003 DROP PROCEDURE IF EXISTS `sp_actualizar_cliente_sexo` */;
DELIMITER ;;
CREATE PROCEDURE `sp_actualizar_cliente_edad`(
    IN in_id_cliente INT,
    IN in_nuevo_sexo ENUM('M', 'F')
)
BEGIN
    UPDATE clientes SET edad = in_nuevo_edad WHERE id_cliente = in_id_cliente;
    COMMIT;
END ;;
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
