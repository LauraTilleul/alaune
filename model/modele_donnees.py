# -*- coding: utf-8 -*-
from __future__ import division
import mysql.connector
import json
import csv
import datetime
import string


def htmlize2(titles_and_href):
    html = ''
    for item in titles_and_href:
        html += '<h2>'
        html += '<a href="' + item[1] + '">' + item[0].strip() + '</a></h2>\n'
    return html        

#petite fonction pour enlever l'année des dates ( '2017-03-04' => '03-04')
def removeYear(date):
    date=datetime.datetime.strptime(date, '%Y-%m-%d')
    date=date.strftime('%m-%d')
    date=str(date)
    return date

# petite fonction pour changer format date ('2017-03-07' => Monday, March 7 )
def newFormat(date):
    date=datetime.datetime.strptime(date, '%Y-%m-%d')
    date=date.strftime('%A %B %d ')
    return date

config = json.loads(open('config.json', 'r').read())
cnx = mysql.connector.connect(** config)
cursor = cnx.cursor(buffered=True)


def insert_quotidien(quotidien):
    name=quotidien.get("nom")
    url=quotidien.get("URL")
    get_quotidien = "SELECT nom FROM quotidiens WHERE nom LIKE '%s'"%name
    cursor.execute(get_quotidien)
    if ( cursor.fetchone() == None ):
        add_quotidien= "INSERT INTO quotidiens (nom, URL) VALUES ('%s', '%s')"%(name,url)
        cursor.execute(add_quotidien)
        cnx.commit()

def insert_une(une):
    title=(une.get("titre")).replace("'"," ")
    get_une= "SELECT titre FROM unes WHERE titre LIKE '%s'"%title
    cursor.execute(get_une)
    if (len( cursor.fetchall() ) == 0):
        name= une.get('quotidien')
        quot_id="SELECT id FROM quotidiens WHERE nom LIKE ('%s')"%name
        cursor.execute(quot_id)
        id=cursor.fetchone()
        quot= id[0]
        URL=une.get('URL')
        date=datetime.datetime.today().strftime('%Y-%m-%d')
        add_une="INSERT INTO unes (titre,URL,date, quotidien_id) VALUES ('%s', '%s', '%s', '%s' )"%(title,URL,date, quot)
        cursor.execute(add_une)
        cnx.commit()

def select_just_une(quotidien):
    quot_id="SELECT id FROM quotidiens WHERE nom LIKE '%s' "%quotidien
    quot_id=quot_id.replace("'","\'")
    cursor.execute(quot_id)
    id=cursor.fetchone()
    date= datetime.datetime.today().strftime('%Y-%m-%d')
    get_une= "SELECT titre FROM unes WHERE quotidien_id LIKE %s AND date LIKE '%s'"%(id[0],date)
    cursor.execute(get_une)
    return (str(cursor.fetchall())).replace('\'',"\'")

def select_unes(quotidien):
    quot_id="SELECT id FROM quotidiens WHERE nom LIKE '%s' "%quotidien
    quot_id=quot_id.replace("'","\'")
    cursor.execute(quot_id)
    id=cursor.fetchone()
    date= datetime.datetime.today().strftime('%Y-%m-%d')
    get_une= "SELECT titre,URL FROM unes WHERE quotidien_id LIKE %s AND date LIKE '%s'"%(id[0],date)
    cursor.execute(get_une)
    return cursor.fetchall()

#QUAND ON CLIQUE SUR LE STREAMGRAPH 
def candidat_Unes(name,date):
    html=''
    name='%'+name+'%'
    if date !='00' :
        date= '2017-'+date
        get_une= "SELECT titre,URL FROM unes WHERE titre LIKE '%s' and date like '%s' "%(name,date)
        cursor.execute(get_une)
        if (cursor.fetchone() != None):
            cursor.execute(get_une)
            html+="<h1 id='unes'>" + newFormat(date) + "<a style='float:right; color:black; font-size:20px;' href=#00> Retour en haut de page </a></h1>"
            html+=htmlize2(cursor.fetchall())
            html+="<h1> <a style='color:black;' href=#00> Retour en haut de page </a> </h1>"
    return html
        
#calcul frequence pour le candidat candidat à la date date 
def calculFrequence(candidat, date):
    req="SELECT id FROM unes where date like '%s' "%date
    cursor.execute(req)
    nbUnesduJour=len(cursor.fetchall())
    recherche= '%'+candidat+'%'
    requete="SELECT titre FROM unes where titre like '%s' and date like '%s'  "%(recherche,date)
    print requete
    cursor.execute(requete)
    occurence= len(cursor.fetchall())
    if nbUnesduJour ==0 :
        return 0
    else :
        fqce=occurence/nbUnesduJour
        print occurence
        return fqce

#list_dates renvoie la liste des dates(format str) allant du jour base jusqu'à aujourd'hui (pour les barCharts)
def list_dates(base):
        date_list=[]
        date_list.append(datetime.datetime.strptime(base, '%Y-%m-%d').date())
        print date_list[0]
        i=0
        while (not(date_list[i]==datetime.date.today())):
            date_list.append((date_list[i] + datetime.timedelta(days=1)))
            i=i+1
        for i in range(0, len(date_list)):
            date_list[i]=str(date_list[i])
        return date_list

#list_dates2 renvoie les dates du jour base jusqu'au 1er Avril (pour le streamGraph) car je n'ai pas vraiment extrait les unes au delà du 1er avril..
def list_dates2(base):
        date_list=[]
        date_list.append(datetime.datetime.strptime(base, '%Y-%m-%d').date())
        print date_list[0]
        i=0
        while (not(date_list[i]==datetime.datetime.strptime('2017-04-01', '%Y-%m-%d').date())):
            date_list.append((date_list[i] + datetime.timedelta(days=1)))
            i=i+1
        for i in range(0, len(date_list)):
            date_list[i]=str(date_list[i])
        return date_list

#genere le fichier politiques.csv avec les fréquences de tous les candidats 
def generePolitiquesCsv():
    politiques = ['lassalle', 'asselineau','fillon', 'le pen', 'hamon', 'macron', 'poutou', 'melenchon',  'dupont', 'cheminade','arthaud' ]
    with open("static/politiques.csv", 'w') as outfile:
        writer = csv.writer(outfile, delimiter=';', lineterminator='\n')
        writer.writerow([ 'key,value,date' ])
        base = '2017-03-15' #pour l'instant je prend la date à laquelle j'ai commencé à insérer les unes le 15 Mars
        dates=list_dates2(base)
        for candidat in politiques :
                for date in dates:
                    frequence=calculFrequence(candidat, date)
                    writer.writerow([candidat +','+  str(frequence) + ',' +  date])
    
#genere le fichier barchart_name.csv avec les frequences du candidat name
def barchartCsv(name):
    with open("static/barchart_"+name+".csv", 'w') as outfile:
        writer = csv.writer(outfile, delimiter="\t", lineterminator='\n')
        writer.writerow(['letter','frequency'])
        base = '2017-03-15'
        dates=list_dates(base)
        for date in dates:
                    frequence=calculFrequence(name, date)
                    if (frequence !=0): # inutile d'afficher les 0 dans le barchart
                        date=removeYear(date)
                        writer.writerow([date ,str(frequence)])



if __name__ == '__main__':
    generePolitiquesCsv()
