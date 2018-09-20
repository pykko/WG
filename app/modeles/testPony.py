#!/usr/bin/python3
# coding: utf-8

from datetime import date
from pony.orm import *


db = Database()
db.bind(provider='mysql', host='localhost', user='root', passwd='azerty', db='wg')



class Joueur(db.Entity):
    id = PrimaryKey(int, auto=True)
    nom = Required(str, 20)
    mdp = Required(str, 20)
    connecte = Required(bool)
    parties_creees = Set( 'Partie' )
    
class Partie(db.Entity):
    id = PrimaryKey(int, auto=True)
    date_creation = Required(date)
    initiateur = Required(Joueur)


@db_session
def enregistrerJoueur( nom ) :
	Joueur( nom = nom , mdp = 'azerty' , connecte = False )
	
@db_session
def getJoueur( idJoueur ) :
	unJoueur = Joueur[ idJoueur ]
	return unJoueur
	
@db_session
def getJoueurs() :
	return select( unJoueur for unJoueur in Joueur )[:]
	
@db_session
def getJoueurParNom( nom ) :
	return Joueur.get( nom = 'amina' )


if __name__ == '__main__' :
	print( 'Test PonyORM' )
	
	set_sql_debug( True )
	db.generate_mapping( create_tables = True )
	
	'''
	print( 'Enregistrement d\'un nouveau joueur' )
	nomJoueur = input( 'Nom : ' )
	
	#with db_session :
	#	nouveauJoueur = Joueur( nom = nomJoueur , mdp = 'azerty' , connecte = False ) 
	
	enregistrerJoueur( nomJoueur )
	
	'''
	
	'''
	try :
		unJoueur = getJoueur( 1 )	
		print( unJoueur.nom )
	except pony.orm.core.ObjectNotFound :
		print( 'Joueur non recensé' )
		
	'''
	
	'''
	with db_session :
		print( select( j for j in Joueur )[:] )
	'''
	
	'''
	lesJoueurs = getJoueurs()
	for unJoueur in lesJoueurs :
		print( unJoueur.nom )
	'''
	
	'''
	with db_session :
		print( Joueur.get( nom = 'amina' ).id )
	'''
	
	'''
	show( Joueur )
	'''
	
	show( getJoueurs() )
	
	
	print( 'Initier une partie' )
	idJoueur = input( 'Initiateur> ' )
	with db_session :
		initiateur = Joueur[ idJoueur ]
		print( initiateur.nom )
		Partie( date_creation = date.today() , initiateur = initiateur )
		
		
	with db_session :
		for unePartie in Joueur[ idJoueur ].parties_creees :
			print( unePartie.date_creation )
	
	

