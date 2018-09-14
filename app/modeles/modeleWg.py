#!/usr/bin/python3
# coding: utf-8

from datetime import date
from pony.orm import *


db = Database()



class Joueur(db.Entity):
    id = PrimaryKey(int, auto=True)
    nom = Required(str, 20)
    mdp = Required(str, 20)
    connecte = Required(bool)
    parties_creees = Set('Partie')


class Partie(db.Entity):
    id = PrimaryKey(int, auto=True)
    date_creation = Required(date)
    initiateur = Required(Joueur)


if __name__ == '__main__' :
	print 'Test PonyORM'
	
	db.generate_mapping()
	
	
