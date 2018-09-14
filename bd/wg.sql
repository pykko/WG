DROP DATABASE IF EXISTS wg ;

CREATE DATABASE IF NOT EXISTS wg DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci ;


use wg ;


CREATE TABLE `joueur` (
  `id` INTEGER PRIMARY KEY AUTO_INCREMENT,
  `nom` VARCHAR(20) NOT NULL,
  `mdp` VARCHAR(20) NOT NULL,
  `connecte` BOOLEAN NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `partie` (
  `id` INTEGER PRIMARY KEY AUTO_INCREMENT,
  `date_creation` DATE NOT NULL,
  `initiateur` INTEGER NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE INDEX `idx_partie__initiateur` ON `partie` (`initiateur`);

ALTER TABLE `partie` ADD CONSTRAINT `fk_partie__initiateur` FOREIGN KEY (`initiateur`) REFERENCES `joueur` (`id`) ;

insert into joueur(nom,mdp) values('Amal','azerty') ;
insert into joueur(nom,mdp) values('Ewen','azerty') ;
insert into joueur(nom,mdp) values('Léo','azerty') ;
insert into joueur(nom,mdp) values('Jean-Yves','azerty') ;
insert into joueur(nom,mdp) values('Samia','azerty') ;



