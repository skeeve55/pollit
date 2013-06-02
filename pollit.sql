-- phpMyAdmin SQL Dump
-- version 3.5.2.2
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Erstellungszeit: 02. Jun 2013 um 20:31
-- Server Version: 5.5.27
-- PHP-Version: 5.4.7

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Datenbank: `pollit`
--

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `polls`
--

CREATE TABLE IF NOT EXISTS `polls` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Topic` varchar(200) NOT NULL,
  `User_Id` int(11) NOT NULL,
  `Creation` datetime NOT NULL,
  PRIMARY KEY (`Id`),
  KEY `User_Id` (`User_Id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Daten für Tabelle `polls`
--

INSERT INTO `polls` (`Id`, `Topic`, `User_Id`, `Creation`) VALUES
(1, 'testi', 1, '2013-06-04 00:00:00'),
(2, 'nagnag', 1, '2013-05-21 00:00:00');

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `users`
--

CREATE TABLE IF NOT EXISTS `users` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Username` varchar(100) NOT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Daten für Tabelle `users`
--

INSERT INTO `users` (`Id`, `Username`) VALUES
(1, 'rischat');

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `user_votes`
--

CREATE TABLE IF NOT EXISTS `user_votes` (
  `User_Id` int(11) NOT NULL,
  `Vote_Id` int(11) NOT NULL,
  `Creation` datetime NOT NULL,
  UNIQUE KEY `User_Id_2` (`User_Id`,`Vote_Id`),
  KEY `User_Id` (`User_Id`),
  KEY `Vote_Id` (`Vote_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `votes`
--

CREATE TABLE IF NOT EXISTS `votes` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Vote` varchar(100) NOT NULL,
  `User_Id` int(11) NOT NULL,
  `Creation` datetime NOT NULL,
  `Poll_Id` int(11) NOT NULL,
  PRIMARY KEY (`Id`),
  KEY `User_Id` (`User_Id`),
  KEY `Poll_Id` (`Poll_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Constraints der exportierten Tabellen
--

--
-- Constraints der Tabelle `polls`
--
ALTER TABLE `polls`
  ADD CONSTRAINT `polls_ibfk_1` FOREIGN KEY (`User_Id`) REFERENCES `users` (`Id`);

--
-- Constraints der Tabelle `votes`
--
ALTER TABLE `votes`
  ADD CONSTRAINT `votes_ibfk_1` FOREIGN KEY (`Poll_Id`) REFERENCES `polls` (`Id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
