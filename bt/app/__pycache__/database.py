# coding: utf-8

import os
import os.path
import codecs

import json

#----------------------------------------------------------
class Database_cl(object):
#----------------------------------------------------------

   # Daten in dieser Variante dauerhaft (persistent) speichern
   # dazu jedes Element in einer Datei, die entsprechend der id benannt ist, speichern
   # alle Elemente werden zur Laufzeit des Servers zur Vereinfachung auch im
   # Hauptspeicher abgelegt

   # die nächste zu vergebende Id wird ebenfalls dauerhaft gespeichert

   # zur Vereinfachung wird hier fest vorgegebenen, dass sich die Daten
   # im Unterverzeichnis "data/<type>" befinden (siehe Konstruktor)

   # es wird ferner angenommen, dass die Datei "data/<type>/maxid.dat" bereits existiert
   # und als einzigen Eintrag den aktuellen Wert der maximalen Id enthält

   #-------------------------------------------------------
   def __init__(self, type_spl):
   #-------------------------------------------------------
      self.type_s = type_spl
      self.path_s = os.path.join('data', type_spl)
      self.data_o = {}
      self.readData_p()

   #-------------------------------------------------------
   def create_px(self, data_opl):
   #-------------------------------------------------------
      # Überprüfung der Datenn müsste ergänzt werden!
      id_s = self.nextId_p()
      # Datei erzeugen
      file_o = codecs.open(os.path.join(self.path_s , id_s+'.dat'), 'w', 'utf-8')
      file_o.write(json.dumps(data_opl, indent=3, ensure_ascii=True))
      file_o.close()

      self.data_o[id_s] = data_opl

      return id_s
      
   #-------------------------------------------------------
   def read_px(self, id_spl = None):
   #-------------------------------------------------------
      # hier zur Vereinfachung:
      # Aufruf ohne id: alle Einträge liefern
      data_o = None
      if id_spl == None:
         data_o = self.data_o
      elif id_spl == '0':
         data_o = self.getDefault_px()
      else:
         if id_spl in self.data_o:
            data_o = self.data_o[id_spl]

      return data_o

   #-------------------------------------------------------
   def update_px(self, id_spl, data_opl):
   #-------------------------------------------------------
      # Überprüfung der Daten müsste ergänzt werden!
      status_b = False
      if id_spl in self.data_o:
         # Datei aktualisieren
         file_o = codecs.open(os.path.join(self.path_s, id_spl+'.dat'), 'w', 'utf-8')
         file_o.write(json.dumps(data_opl, indent=3, ensure_ascii=True))
         file_o.close()

         self.data_o[id_spl] = data_opl
         status_b = True
      
      return status_b

   #-------------------------------------------------------
   def delete_px(self, id_spl):
   #-------------------------------------------------------
      status_b = False
      if id_spl in self.data_o:
         # Datei entfernen
         os.remove(os.path.join(self.path_s, id_spl+'.dat'))

         del self.data_o[id_spl]
         status_b = True
      
      return status_b
         
   #-------------------------------------------------------
   def getDefault_px(self):
   #-------------------------------------------------------
      # sollte überschrieben werden!
      return {}

   #-------------------------------------------------------
   def readData_p(self):
   #-------------------------------------------------------

      files_a = os.listdir(self.path_s)
      for fileName_s in files_a:
         if fileName_s.endswith('.dat') and fileName_s != 'maxid.dat':
            file_o = codecs.open(os.path.join(self.path_s, fileName_s), 'rU', 'utf-8')
            content_s = file_o.read()
            file_o.close()
            id_s = fileName_s[:-4]
            self.data_o[id_s] = json.loads(content_s)

   #-------------------------------------------------------
   def nextId_p(self):
   #-------------------------------------------------------
      file_o = open(os.path.join(self.path_s, 'maxid.dat'), 'r+')
      maxId_s = file_o.read()
      maxId_s = str(int(maxId_s)+1)
      file_o.seek(0)
      file_o.write(maxId_s)
      file_o.close()

      return maxId_s

#----------------------------------------------------------
class ProjektDatabase_cl(Database_cl):
#----------------------------------------------------------

   #-------------------------------------------------------
   def __init__(self):
   #-------------------------------------------------------
      super().__init__('Projekt')

   #-------------------------------------------------------
   def getDefault_px(self):
   #-------------------------------------------------------

      return {
         'name': ''
      }

#----------------------------------------------------------
class FehlerDatabase_cl(Database_cl):
#----------------------------------------------------------

   #-------------------------------------------------------
   def __init__(self):
   #-------------------------------------------------------
      super().__init__('Fehler')

   #-------------------------------------------------------
   def getDefault_px(self):
   #-------------------------------------------------------

      return {
         'komponente': '',
         'beschreibung': '',
         'mitarbeiter': '',
         'datum': '',
         'kategorie': '',
         'fehlerstatus': 'erkannt'
      }

class KomponenteDatabase_cl(Database_cl):
#----------------------------------------------------------

   #-------------------------------------------------------
   def __init__(self):
   #-------------------------------------------------------
      super().__init__('Komponenten')

   #-------------------------------------------------------
   def getDefault_px(self):
   #-------------------------------------------------------

      return {
         'name': '',
         'beschreibung': '',
         'projekt': ''
      }

class MitarbeiterDatabase_cl(Database_cl):
   # ----------------------------------------------------------

   # -------------------------------------------------------
   def __init__(self):
      # -------------------------------------------------------
      super().__init__('Mitarbeiter')

   # -------------------------------------------------------
   def getDefault_px(self):
      # -------------------------------------------------------

      return {
         'name': '',
         'vorname': '',
         'alter': '',
         'abteilung': ''
      }

class KategorieDatabase_cl(Database_cl):
   # ----------------------------------------------------------

   # -------------------------------------------------------
   def __init__(self):
      # -------------------------------------------------------
      super().__init__('Kategorie')

   # -------------------------------------------------------
   def getDefault_px(self):
      # -------------------------------------------------------

      return {
         'fehlerbeschreibung': '',
         'fehlerursache': ''
      }

class AuswertungProjekteDatabase_cl(Database_cl):
   # ----------------------------------------------------------

   # -------------------------------------------------------
   def __init__(self):
      # -------------------------------------------------------
      super().__init__('AuswertungProjekte')

   # -------------------------------------------------------
   def getDefault_px(self):
      # -------------------------------------------------------

      return {
         'name': '',
         'fehlerstatus': ''
      }

class AuswertungKategorieDatabase_cl(Database_cl):
   # ----------------------------------------------------------

   # -------------------------------------------------------
   def __init__(self):
      # -------------------------------------------------------
      super().__init__('AuswertungKategorie')

   # -------------------------------------------------------
   def getDefault_px(self):
      # -------------------------------------------------------

      return {
         'Fehlerbeschreibung': '',
         'Fehlerursache': '',
         'Fehlerstatus': ''

      }
