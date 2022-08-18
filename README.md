# TechnicalTaskRound2
Create Simple Crud , Using Python ,HTML , CSS , JS and MYSQL

    * This Project is perform simple crud operation 

    @Module
    ~~~~~~~~          
          Public / Visitng Area
          ======================  
                  Home Page / index.py
                  ````````````````````````
                          This page is staticaly design . Using HTML , CSS , JS ,Python
                  About Page / about.py
                  `````````````````````
                          This page is staticaly design . Using HTML , CSS , JS ,Python
                  Contact Form / contact.py
                  ``````````````````````````
                          This page is perform the action. It's page store the msg , whos person wants to contact us. Using HTML , CSS , JS ,Python
                  Registration Page / registration.py
                  ```````````````````````````````````
                          This page is perform the action. It's page store the user information Authentication. Using HTML , CSS , JS ,Python
                  Login Page / login.py
                  `````````````````````
                          This page is perform the action. It's page is Authenticate the Authorize user. Using HTML , CSS , JS ,Python
                  
                  
          User  Area / After Login
          =========================
                  Profile(profile.py)
                  ```````````````````
                          This page is perform the action. It's page show the user information. Using HTML , CSS , JS ,Python
                  Update Page / update.py
                  ```````````````````````
                          This page is perform the action. It's page update the user information. Using HTML , CSS , JS ,Python
                  Contact Management Page / contactmanagement.py
                  ``````````````````````````````````````````````
                          This page is perform the action. It's page show the all contact person who's fill the form. Using HTML , CSS , JS ,Python

================================================================= Web Pages & Module ==========================================================================================

                                                  Software Service
                                                  ===============
                                                      //    \\
                                                    //        \\
                                                  //            \\
                                                //                \\
                                              //                    \\
                                            //                        \\
                                          //                            \\
                                        //                                \\
                                      //                                    \\
                             Visiting Area                               After Login
                             ||                                           ||
                             ||                                           ||== Profile Page / profile.py
                             ||== Home Page / index.py                    ||
                             ||                                           ||== Update Page / update.py
                             ||== About Page / about.py                   ||
                             ||                                           ||== Contact Management Page / contactmanagement.py
                             ||== Contact Form / contact.py               
                             ||                                           
                             ||== Registration Page / registration.py     
                             ||                                           
                             ||== Login Page / login.py                   
                           
                           
================================================================= DataBase & Table Structure =====================================================================================
                                                                      
-- phpMyAdmin SQL Dump
-- version 3.2.0.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Aug 18, 2022 at 12:42 PM
-- Server version: 5.1.36
-- PHP Version: 5.3.0

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";

--
-- Database: `task2`
--
CREATE DATABASE `task2` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `task2`;

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE IF NOT EXISTS `admin` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `number` varchar(13) NOT NULL,
  `email` varchar(30) NOT NULL,
  `password` varchar(80) NOT NULL,
  `CurDate` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id`, `name`, `number`, `email`, `password`, `CurDate`) VALUES
(3, 'AMAN MISHRA', '9964523', 'admin@admin.com', 'admin', '2022-08-18');

-- --------------------------------------------------------

--
-- Table structure for table `contact`
--

CREATE TABLE IF NOT EXISTS `contact` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `number` varchar(13) NOT NULL,
  `email` varchar(30) NOT NULL,
  `msg` varchar(80) NOT NULL,
  `CurDate` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `contact`
--

INSERT INTO `contact` (`id`, `name`, `number`, `email`, `msg`, `CurDate`) VALUES
(1, 'AMAN MISHRA', '07408736297', 'amnamnmishra@gmail.com', 'no problem testing now\r\n', '2022-08-17');
