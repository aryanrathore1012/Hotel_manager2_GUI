-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 29, 2022 at 07:38 PM
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
-- Table structure for table `booking_details`
--

CREATE TABLE `booking_details` (
  `bill_id` int(11) NOT NULL,
  `room_number` varchar(100) NOT NULL,
  `book_date` date NOT NULL,
  `book_time` time NOT NULL,
  `payment_amount` int(11) NOT NULL,
  `payment_method` varchar(50) NOT NULL,
  `number_of_people` int(11) NOT NULL,
  `customer_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `booking_details`
--

INSERT INTO `booking_details` (`bill_id`, `room_number`, `book_date`, `book_time`, `payment_amount`, `payment_method`, `number_of_people`, `customer_id`) VALUES
(100, '1', '2022-12-04', '13:50:00', 8000, 'UPI', 1, 1001),
(101, '2', '2022-01-01', '09:08:01', 7000, 'UPI', 3, 1002),
(102, '3', '2022-01-02', '10:15:07', 6000, 'Net banking', 1, 1003),
(103, '4', '2022-01-03', '11:11:11', 5000, 'Credit card', 2, 1004),
(104, '5', '2022-01-03', '13:24:37', 4000, 'Debit card', 2, 1005),
(108, '10', '2022-12-28', '13:12:21', 18000, 'UPI', 3, 1008),
(110, '11', '2022-12-28', '13:16:56', 15000, 'cash', 4, 1010),
(112, '6', '2022-12-28', '15:19:39', 12000, 'card', 5, 1011),
(113, '12', '2022-12-28', '15:52:36', 10000, 'card', 1, 111),
(116, '10', '2022-12-29', '23:40:50', 6000, 'UPI', 2, 1011),
(120, '11', '2022-12-29', '23:49:53', 0, 'FREE', 3, 1019),
(123, '11', '2022-12-28', '18:27:32', 18000, 'UPI', 3, 1023);

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
(1001, 'Aryan Rathore', 9685071745, 19, 'M', 'khatiwala tank', 6313523911, '1', 100),
(1002, 'Reva bharara', 829599330, 19, 'F', 'abc street in delhi', 789645132, '2', 101),
(1003, 'murataza ', 7985123123, 19, 'M', 'gay street', 19283746, '3', 102),
(1004, 'debanik', 79852323123, 19, 'M', 'sindhi street', 19211746, '4', 103),
(1005, 'khushi', 7345123123, 22, 'F', 'khatiwala tank', 789283746, '5', 104),
(1008, 'shyam', 9898989898, 24, 'M', 'asd qwe zxc', 18273465, '', 108),
(1010, 'prakash', 9876401200, 34, 'M', 'asd yui hjk', 18213654, '', 110),
(1011, 'sonia', 7865431912, 25, 'F', 'uio hjk bnm', 102934456, '', 116),
(1019, 'Nidhi', 9685011745, 50, 'F', 'khatiwala band', 1928445566, '', 120),
(1023, 'rajesh', 1029374222, 50, 'M', 'tyu ghj bnm', 102934478, '', 123);

-- --------------------------------------------------------

--
-- Table structure for table `room`
--

CREATE TABLE `room` (
  `room_number` varchar(100) NOT NULL DEFAULT '000',
  `room_type` text NOT NULL,
  `room_rate` int(11) NOT NULL,
  `occupant` int(11) DEFAULT NULL,
  `EMPTY` varchar(255) DEFAULT 'YES'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `room`
--

INSERT INTO `room` (`room_number`, `room_type`, `room_rate`, `occupant`, `EMPTY`) VALUES
('1', '1 Bed AC', 8000, 1001, 'NO'),
('10', '1 Bed AC POOL', 1800, NULL, 'YES'),
('11', '2 Bed AC POOL', 3800, NULL, 'YES'),
('12', '1 bed non ac', 9000, NULL, 'YES'),
('2', '1 Bed Non-AC', 7000, 1002, 'NO'),
('3', '2 Bed AC', 6000, 1003, 'NO'),
('4', '2 Bed Non-AC', 5000, 1004, 'NO'),
('5', '3 Bed AC', 4000, 1005, 'NO'),
('6', '3 Bed Non-AC', 3000, NULL, 'YES'),
('7', '4 Bed AC', 2000, NULL, 'YES'),
('8', '4 Bed Non-AC', 1000, NULL, 'YES'),
('9', '1 BED AC', 10000, NULL, 'YES');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `booking_details`
--
ALTER TABLE `booking_details`
  ADD PRIMARY KEY (`bill_id`);

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`customer_id`),
  ADD UNIQUE KEY `adhaar_number` (`adhaar_number`),
  ADD UNIQUE KEY `bill_id` (`bill_id`),
  ADD KEY `room_number` (`room_number`);

--
-- Indexes for table `room`
--
ALTER TABLE `room`
  ADD PRIMARY KEY (`room_number`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `booking_details`
--
ALTER TABLE `booking_details`
  MODIFY `bill_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=124;

--
-- AUTO_INCREMENT for table `customer`
--
ALTER TABLE `customer`
  MODIFY `customer_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1024;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
