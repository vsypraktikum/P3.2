# coding: utf-8

import json

import cherrypy

# Method-Dispatching!

# Übersicht Anforderungen / Methoden
# (beachte: / relativ zu /navigation, siehe Konfiguration Server!)

"""

Anforderung       GET          PUT          POST          DELETE
----------------------------------------------------------------
/                 Nav-Entries  -            -             -

"""

#----------------------------------------------------------
class Navigation_cl(object):
#----------------------------------------------------------

   exposed = True # gilt für alle Methoden

   #-------------------------------------------------------
   def __init__(self):
   #-------------------------------------------------------
      pass

   #-------------------------------------------------------
   def GET(self):
   #-------------------------------------------------------
      # Hinweis: könnte man auch aus einer Datei einlesen
      retVal_o = [
         {'action': 'Fehler', 'text': 'Bearbeitung Fehlerdaten'},
         {'action': 'Projekt', 'text': 'Pflege Projekte'},
         {'action': 'Komponenten', 'text': 'Pflege Komponenten'},
         {'action': 'Mitarbeiter', 'text': 'Pflege Daten Mitarbeiter'},
         {'action': 'Kategorie', 'text': 'Pflege Kategorien'},
         {'action': 'AuswertungProjekte', 'text': 'Auswertung Projekte/Fehler'},
         {'action': 'AuswertungKategorie', 'text': 'Auswertung Kategorien/Fehler'}
      ]

      return json.dumps(retVal_o)
      
# EOF