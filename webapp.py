# -*- coding:utf-8 -*-

from flask import Flask, request
from view import plain_html
from model import modele_donnees, modele_extraction

app = Flask(__name__)

@app.route('/')
def index():
        modele_extraction.insert_all()
	return plain_html.simple_form()

@app.route('/unes')        
def unes():
        return plain_html.htmlUnes()

@app.route('/quel_journal', methods = ['POST'])
def quel_journal():
	journal = request.form['journal']
	unes = modele_donnees.select_unes(journal)
	return plain_html.htmlQuelJournal(unes, journal)


@app.route('/StreamGraph')
def StreamGraph():
        #modele_donnees.generePolitiquesCsv() plus besoin de mettre à jour le csv car finalement je prend seulement les unes du 15Mars au 1er Avril,j'avais trop peu de unes après..
        return plain_html.htmlStreamGraph()

@app.route('/candidat', methods= ['get', 'post'])
def candidat():
        name=request.args['name']
        date=request.args['date']
        page_content= plain_html.htmlCandidat(name)
        modele_donnees.barchartCsv(name)
        page_content+= plain_html.htmlBarchart(name)
        page_content+=(modele_donnees.candidat_Unes(name,date))
        return page_content




if __name__ == '__main__':
        app.run(debug=True)
