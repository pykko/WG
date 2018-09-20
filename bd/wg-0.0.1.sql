DROP DATABASE IF EXISTS wg ;

CREATE DATABASE IF NOT EXISTS wg DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci ;


use wg ;


CREATE TABLE `joueur` (
  `id` INTEGER PRIMARY KEY AUTO_INCREMENT,
  `nom` VARCHAR(20) NOT NULL,
  `mdp` VARCHAR(20) NOT NULL,
  `connecte` BOOLEAN NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



insert into joueur(nom,mdp) values('amal','azerty') ;
insert into joueur(nom,mdp) values('ewen','azerty') ;
insert into joueur(nom,mdp) values('léo','azerty') ;
insert into joueur(nom,mdp) values('jean-yves','azerty') ;
insert into joueur(nom,mdp) values('samia','azerty') ;



