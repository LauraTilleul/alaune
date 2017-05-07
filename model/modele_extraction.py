# -*- coding:utf-8 -*-
from modele_donnees import *
from extraction import CourrierInternational, LePoint, JournalduNet, LesEchos, LeDauphine, LaTribune, SudOuest, LeFigaro, LeParisien, _20minutes, LeMonde, OuestFrance

#insere ttes les unes du journal passé en paramètre dans la BD
def insert_all_unes(journal):
    if (journal=='lemonde'):
        targetURL='http://lemonde.fr'
        titres=LeMonde.unes(targetURL)
        for item in titres :
            une={'titre':item[0].strip(), 'URL':targetURL + item[1].strip(), 'quotidien':journal }
            insert_une(une)

    elif ( journal=='figaro'):
        targetURL='http://www.lefigaro.fr/'
        titres=LeFigaro.unes(targetURL)
        for item in titres :
            une={'titre':item[0].strip(), 'URL':item[1].strip(), 'quotidien':journal }
            insert_une(une)

    elif (  journal=='lejournaldunet'):
         targetURL='http://www.lejournaldunet.fr'
         titres=JournalduNet.unes(targetURL)
         for item in titres :
            une={'titre':item[0].strip(), 'URL':item[1].strip(), 'quotidien':journal }
            insert_une(une)

    elif ( journal== 'lepoint'):
        targetURL='http://www.lepoint.fr'
        titres=LePoint.unes(targetURL)
        for item in titres :
            une={'titre':item[0].strip(), 'URL':targetURL + item[1].strip(), 'quotidien':journal }
            insert_une(une)

    elif (journal=='courrier'):
        targetURL='http://www.courrierinternational.com'
        titres=CourrierInternational.unes(targetURL)
        for item in titres :
            une={'titre':item[0].strip(), 'URL':targetURL + item[1].strip(), 'quotidien':journal }
            insert_une(une)
            
    elif(journal=='lesechos'):
        targetURL='http://www.lesechos.fr/'
        titres=LesEchos.unes(targetURL)
        for item in titres :
            une={'titre':item[0].strip(), 'URL':item[1].strip(), 'quotidien':journal }
            insert_une(une)

    elif(journal=='latribune'):
        targetURL='http://www.latribune.fr/'
        titres=LaTribune.unes(targetURL)
        for item in titres :
            une={'titre':item[0].strip(), 'URL':item[1].strip(), 'quotidien':journal }
            insert_une(une)
            
    elif(journal=='ledauphine'):
        targetURL='http://ledauphine.com'
        titres=LeDauphine.unes(targetURL)
        for item in titres :
            une={'titre':item[0].strip(), 'URL':targetURL + item[1].strip(), 'quotidien':journal }
            insert_une(une)
        
    elif(journal=='ouestfrance'):
        targetURL='http://www.ouest-france.fr'
        titres=OuestFrance.unes(targetURL)
        for item in titres :
            une={'titre':item[0].strip(), 'URL':targetURL + item[1].strip(), 'quotidien':journal }
            insert_une(une)      

    elif(journal=='sudouest'):
        targetURL='http://www.sudouest.fr/'
        titres=SudOuest.unes(targetURL)
        for item in titres :
            une={'titre':item[0].strip(), 'URL':targetURL + item[1].strip(), 'quotidien':journal }
            insert_une(une)

    elif(journal=='leparisien'):
        targetURL='http://www.leparisien.fr'
        titres=LeParisien.unes('http://www.leparisien.fr')
        for item in titres :
            une={'titre':item[0].strip(), 'URL':item[1].strip(), 'quotidien':journal }
            insert_une(une)

    elif(journal=='20min'):
        targetURL='http://www.20minutes.fr'
        titres=_20minutes.unes(targetURL)
        for item in titres :
            une={'titre':item[0].strip(), 'URL':targetURL + item[1].strip(), 'quotidien':journal }
            insert_une(une)

#insère ttes les unes de tous les journaux dans la BD
def insert_all():
    journaux=['lemonde','figaro','lejournaldunet','lepoint','courrier', 'lesechos']
    journaux+=['latribune','ledauphine','ouestfrance','sudouest','leparisien','20min']
    for journal in journaux:
        insert_all_unes(journal)



if __name__ == '__main__':
    insert_all()
