# -*- coding:utf-8-*-

from modele_donnees import *
from model_extraction import CourrierInternational, LePoint, JournalduNet, LesEchos, LeDauphine, LaTribune, SudOuest, LeFigaro, LeParisien, _20minutes, LeMonde, OuestFrance

def unes(journal):
	if journal == 'courrier':
		targetURL = 'http://www.courrierinternational.com'
		titres = CourrierInternational.unes(targetURL)
	elif journal == 'lepoint':
		targetURL = 'http://www.lepoint.fr'
		titres = LePoint.unes(targetURL)
	elif journal == 'lejournaldunet':
		targetURL = 'http://www.lejournaldunet.fr'
		titres = JournalduNet.unes(targetURL)
	elif journal == 'lesechos':
		targetURL = 'http://www.lesechos.fr/'
		titres = LesEchos.unes(targetURL)
	elif journal == 'latribune':
		targetURL = 'http://www.latribune.fr/'
	elif journal == 'ledauphine':
		targetURL= 'http://ledauphine.com'
		titres=LeDauphine.unes(targetURL)
	elif journal == 'lemonde':
		targetURL = 'http://www.lemonde.fr'
		titres= LeMonde.unes(targetURL)
	elif journal == 'ouestfrance':
		targetURL = 'http://www.ouest-france.fr'
		titres=OuestFrance.unes(targetURL)
	elif journal == 'sudouest' :
		targetURL= 'http://www.sudouest.fr/'
		titres=SudOuest.unes(targetURL)
	elif journal == 'figaro' :
		targetURL= 'http://www.lefigaro.fr/'
		titres=LeFigaro.unes(targetURL)
	elif journal=='leparisien':
		targetURL='http://www.leparisien.fr'
		titres=LeParisien.unes(targetURL)
	else: # journal=='20min':
		targetURL='http://www.20minutes.fr'
		titres=_20minutes.unes(targetURL)
	return titres, targetURL

def extraction_stockage(journal):
	titres = unes(journal)
	target_URL = titres[1]
	for t in titres[0]:
		titre = t[0]
		URL = t[1]
		une = {}
		une['nom_court_quotidien'] = journal
		une['URL'] = str(URL)
		une['titre'] = titre.encode('utf8')
		insert_une(une)
	return True

if __name__ == '__main__':
	extraction_stockage('lepoint')
