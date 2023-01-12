-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 12, 2023 at 09:54 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.1.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hotel_database`
--

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `customer_id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `phone` bigint(20) DEFAULT NULL,
  `age` int(11) NOT NULL,
  `sex` varchar(10) NOT NULL,
  `address` varchar(255) NOT NULL,
  `adhaar_number` bigint(20) DEFAULT NULL,
  `room_number` varchar(100) NOT NULL,
  `bill_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`customer_id`, `name`, `phone`, `age`, `sex`, `address`, `adhaar_number`, `room_number`, `bill_id`) VALUES
(1001, 'Aryan_Rathore', 9685071745, 19, 'M', 'khatiwala tank', 6313523911, '2011', 222),
(1002, 'Reva_bharara', 829599330, 19, 'F', 'abc street in delhi', 789645132, '2', 101),
(1003, 'murataza ', 7985123123, 19, 'M', 'gay street', 19283746, '3', 102),
(1004, 'debanik', 79852323123, 19, 'M', 'sindhi street', 19211746, '', 103),
(1005, 'khushi', 7345123123, 22, 'F', 'khatiwala tank', 789283746, '', 104),
(1008, 'shyam', 9898989898, 24, 'M', 'asd qwe zxc', 18273465, '', 108),
(1010, 'prakash', 9876401200, 34, 'M', 'asd yui hjk', 18213654, '', 309),
(1011, 'sonia', 7865431912, 25, 'F', 'uio hjk bnm', 102934456, '', 116),
(1019, 'Nidhi', 9685011745, 50, 'F', 'khatiwala band', 1928445566, '', 891),
(1023, 'rajesh', 1029374222, 50, 'M', 'tyu ghj bnm', 102934478, '', 892),
(1024, 'sonia2', 123123, 18, 'M', 'asdqwewqeasd', 1233450, '', 999),
(1069, 'best_of_luck', 123123399, 76, 'M', 'adasdasdasd', 0, '', 216),
(1070, 'depika_padukon', 871256371, 40, 'M', 'asdasdasdas11', 1231231333, '', 897),
(1080, 'ADHAY_PRATAP_SINGH', 7894444444, 10, 'M', 'asdasdasdqwqqqq', 73457816411, '', 972),
(1090, 'rainbow_man', 172638911, 56, 'M', 'asdqwefghfgh', 1782571211, '', 900);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`customer_id`),
  ADD UNIQUE KEY `adhaar_number` (`adhaar_number`),
  ADD UNIQUE KEY `bill_id` (`bill_id`),
  ADD KEY `room_number` (`room_number`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `customer`
--
ALTER TABLE `customer`
  MODIFY `customer_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1091;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
