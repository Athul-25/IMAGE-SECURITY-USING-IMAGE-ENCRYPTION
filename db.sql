/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 5.7.9 : Database - crypto_hub
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`crypto_hub` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `crypto_hub`;

/*Table structure for table `key_request` */

DROP TABLE IF EXISTS `key_request`;

CREATE TABLE `key_request` (
  `request_id` int(11) NOT NULL AUTO_INCREMENT,
  `share_id` int(11) DEFAULT NULL,
  `staff_id` int(11) DEFAULT NULL,
  `Key_file` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`request_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `key_request` */

insert  into `key_request`(`request_id`,`share_id`,`staff_id`,`Key_file`) values 
(1,1,2,'static/share_images/c4807db8-d39f-44c2-b4f4-92833f412c88_key.png'),
(2,2,2,'static/share_images/4f28434a-d949-45a6-9525-a550d6b4461b_key.png');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `usertype` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`usertype`) values 
(1,'admin','admin','admin'),
(3,'amal','amal','staff');

/*Table structure for table `share` */

DROP TABLE IF EXISTS `share`;

CREATE TABLE `share` (
  `share_id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) DEFAULT NULL,
  `share_1` varchar(100) DEFAULT NULL,
  `share_2` varchar(100) DEFAULT NULL,
  `key` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`share_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `share` */

insert  into `share`(`share_id`,`title`,`share_1`,`share_2`,`key`,`date`) values 
(1,'anu','static/share_images/d315cb67-357d-4af9-a229-93b72be8d56cshare1.enc','static/share_images/20863ce2-7fef-452b-8511-19c4ba7e4be4share2.enc','static/share_images/c4807db8-d39f-44c2-b4f4-92833f412c88_key.png','2024-03-18'),
(2,'image','static/share_images/0223bda9-b9af-4885-bf93-4822ad75c7fbshare1.enc','static/share_images/be27a45f-d543-4348-af70-42fbb4b8afcdshare2.enc','static/share_images/4f28434a-d949-45a6-9525-a550d6b4461b_key.png','2024-03-20');

/*Table structure for table `staff` */

DROP TABLE IF EXISTS `staff`;

CREATE TABLE `staff` (
  `staff_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `first_name` varchar(100) DEFAULT NULL,
  `last_name` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `gender` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`staff_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `staff` */

insert  into `staff`(`staff_id`,`login_id`,`first_name`,`last_name`,`phone`,`email`,`address`,`gender`) values 
(2,3,'amal','james','09876543201','amaljames@gmail.com','arakkal house peramangalam','male');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
