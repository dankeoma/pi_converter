-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: pi_converter
-- ------------------------------------------------------
-- Server version	8.0.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `params`
--

DROP TABLE IF EXISTS `params`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `params` (
  `paramID` int NOT NULL AUTO_INCREMENT,
  `apiKey` varchar(255) DEFAULT NULL,
  `vendorCode` varchar(255) DEFAULT NULL,
  `vendor` varchar(100) DEFAULT NULL,
  `createdAt` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `expiresAt` date DEFAULT NULL,
  `db` varchar(100) DEFAULT NULL,
  `status` tinyint DEFAULT '1',
  `director` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`paramID`),
  UNIQUE KEY `apiKey` (`apiKey`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `params`
--

LOCK TABLES `params` WRITE;
/*!40000 ALTER TABLE `params` DISABLE KEYS */;
INSERT INTO `params` VALUES (1,'5LU7#3UD4UXICLFU@072W5$BP','2576885106','University of Nigeria Nsuka','2024-10-06 01:08:08','2025-01-06','school',1,NULL),(2,'f44264c3bf9fd8ab208aac9f474f586603acab50a7e9680506cc92bb460400fb','2673046699','University of Benin','2024-11-21 23:00:00','2024-03-22','school',1,'Nwankwo Daniel'),(3,'15fdc33684407818c065c78228ea45d156583430b19a87effed00f1fcf3f0d5b','1009848741','University of Benin','2024-11-21 23:00:00','2024-03-22','school',1,'Nwankwo Daniel'),(4,'8aabdffe11b8ad1285e2ea3050d5663b16fc39cdace423532c11b05f0cb77d1b','8216457317','University of Benin','2024-11-21 23:00:00','2025-02-22','school',1,'Nwankwo Daniel');
/*!40000 ALTER TABLE `params` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-26  2:36:39
