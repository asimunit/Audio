-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Mar 12, 2021 at 03:23 PM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 8.0.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `audio`
--

-- --------------------------------------------------------

--
-- Table structure for table `audio_book`
--

CREATE TABLE `audio_book` (
  `id` int(11) NOT NULL,
  `title` varchar(200) DEFAULT NULL,
  `author` varchar(200) DEFAULT NULL,
  `narrator` varchar(200) DEFAULT NULL,
  `duration` int(10) UNSIGNED DEFAULT NULL,
  `uploaded_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `audio_book`
--

INSERT INTO `audio_book` (`id`, `title`, `author`, `narrator`, `duration`, `uploaded_at`) VALUES
(1, 'bad blood', 'ranbeer', 'king', 5, '2021-03-11 20:25:29'),
(2, 'bad blood', 'ranbeer2', 'king2', 5, '2021-03-11 20:27:35'),
(3, 'rrrrrrrrrr', 'rrrrrrrrrrr', 'rrrrrrrrrrr', 222, '2021-03-12 06:55:33');

-- --------------------------------------------------------

--
-- Table structure for table `podcast`
--

CREATE TABLE `podcast` (
  `id` int(11) NOT NULL,
  `name` varchar(200) DEFAULT NULL,
  `duration` int(10) UNSIGNED DEFAULT NULL,
  `uploaded_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `host` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `podcast`
--

INSERT INTO `podcast` (`id`, `name`, `duration`, `uploaded_at`, `host`) VALUES
(1, 'bad blood', 5, '2021-03-11 20:22:06', 'ranbeer'),
(2, 'ravi ravi', 3, '2021-03-12 06:55:15', 'sameer'),
(3, 'tttttt', 1111, '2021-03-12 13:40:59', 'qqqqqqqqq');

-- --------------------------------------------------------

--
-- Table structure for table `song`
--

CREATE TABLE `song` (
  `id` int(11) NOT NULL,
  `name` varchar(200) DEFAULT NULL,
  `duration` int(10) UNSIGNED DEFAULT NULL,
  `uplaoded_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `song`
--

INSERT INTO `song` (`id`, `name`, `duration`, `uplaoded_at`) VALUES
(1, 'fsd', 3423, '2021-03-11 20:17:28'),
(7, 'unknown', 222, '2021-03-12 13:58:24');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `audio_book`
--
ALTER TABLE `audio_book`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `podcast`
--
ALTER TABLE `podcast`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `song`
--
ALTER TABLE `song`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `audio_book`
--
ALTER TABLE `audio_book`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `podcast`
--
ALTER TABLE `podcast`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `song`
--
ALTER TABLE `song`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
