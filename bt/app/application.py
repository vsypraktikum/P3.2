# coding: utf-8

import json
import cherrypy

from .database import ProjektDatabase_cl, FehlerDatabase_cl, KomponenteDatabase_cl, MitarbeiterDatabase_cl,KategorieDatabase_cl,AuswertungProjekteDatabase_cl,AuswertungKategorieDatabase_cl

# Method-Dispatching!

# Übersicht Anforderungen / Methoden

"""

Anforderung       GET          POST         PUT           DELETE
----------------------------------------------------------------
/                 Liste        -            -             -
                  Literatur
                  liefern

/Projekt          Liste        -            -             -
                  Projekte
                  liefern

/evaluated        Liste        -            -             -
                  Auswertungen
                  liefern

/Projekt/0        Projekt      Projekt     -             -
                  mit id=0     anlegen      
                  liefern
                  (Vorgabe-Werte)

/evaluated/0      Dokument     Dokument     -             -
                  mit id=0     anlegen      
                  liefern
                  (Vorgabe-Werte)

/Projekt/{id}     Projekt     -             Projekt       Projekt
                  mit {id}                  ändern        löschen
                  liefern
                  (Literatur)

/evaluated/{id}   Dokument     -            Dokument      Dokument
                  mit {id}                  ändern        löschen
                  liefern
                  (Auswertungen)

id > 0 ! 

"""

#-------------------------------------------------------
def adjustId_p(id_spl, data_opl):
#-------------------------------------------------------

   if id_spl == None:
      data_opl['id'] = ''
   elif id_spl == '':
      data_opl['id'] = ''
   elif id_spl == '0':
      data_opl['id'] = ''
   else:
      data_opl['id'] = id_spl
   return data_opl


#----------------------------------------------------------
class Projekt_cl(object):
#----------------------------------------------------------

   #-------------------------------------------------------
   def __init__(self):
   #-------------------------------------------------------
      self.db_o = ProjektDatabase_cl()

   #-------------------------------------------------------
   def GET(self, id):
   #-------------------------------------------------------
      retVal_o = {
         'data': None
      }
      if id == None:
         # Anforderung der Liste
         retVal_o['data'] = self.db_o.read_px()
      else:
         # Anforderung eines Dokuments
         data_o = self.db_o.read_px(id)
         if data_o != None:
            retVal_o['data'] = adjustId_p(id, data_o)

      return retVal_o
      
   #-------------------------------------------------------
   def POST(self, data_opl):
   #-------------------------------------------------------
      retVal_o = {
         'id': None
      }

      # data_opl: Dictionary mit den gelieferten key-value-Paaren

      data_o = {
         'name': data_opl["name_s"]
      }
      # Create-Operation
      id_s = self.db_o.create_px(data_o)
      retVal_o['id'] = id_s
         
      return retVal_o
      
   #-------------------------------------------------------
   def PUT(self, data_opl):
   #-------------------------------------------------------
      # Sichern der Daten: jetzt wird keine vollständige Seite
      # zurückgeliefert, sondern nur noch die Information, ob das
      # Speichern erfolgreich war

      retVal_o = {
         'id': None
      }

      # data_opl: Dictionary mit den gelieferten key-value-Paaren

      id_s = data_opl["id_s"]
      data_o = {
         'name': data_opl["name_s"]
      }
      # Update-Operation
      retVal_o['id'] = id_s
      if self.db_o.update_px(id_s, data_o):
         pass
      else:
         retVal_o['id'] = None

      return retVal_o

   #-------------------------------------------------------
   def DELETE(self, id):
   #-------------------------------------------------------
      # Eintrag löschen, nur noch Rückmeldung liefern
      retVal_o = {
         'id': id
      }

      if self.db_o.delete_px(id):
         pass
      else:
         retVal_o['id'] = None

      return retVal_o

class Projektkomponente_cl(object):

    def __init__(self):
        # -------------------------------------------------------
        self.db_o = KomponenteDatabase_cl()
        self.db_proj = ProjektDatabase_cl()

    # -------------------------------------------------------
    def GET(self, id):
        # -------------------------------------------------------
        retVal_o = {
            'data': None
        }
        if id != None:
            # Anforderung der Liste
            data_object = self.db_o.read_px()

            data_proj = self.db_proj.read_px(id)
            data_tmp = {}
            for key_s in data_object:
                if data_proj['name'] == data_object[key_s]['projekt']:
                    data_tmp[key_s] = data_object[key_s]
            retVal_o['data'] = data_tmp

        return retVal_o

class ProjektfehlerAuswertung_cl(object):

    def __init__(self):
        # -------------------------------------------------------
        self.db_o = ProjektDatabase_cl()
        self.db_komponent = KomponenteDatabase_cl()
        self.db_fehler = FehlerDatabase_cl()

    # -------------------------------------------------------
    def GET(self, id):
        # -------------------------------------------------------
        retVal_o = {
            'data': None,
            'data_komponent': None,
            'data_fehler': None
        }
        if id == None:
            # Anforderung der Liste
            retVal_o['data'] = self.db_o.read_px()
            # Anforderung eines Dokuments
            data_o = self.db_o.read_px(id)
            if data_o != None:
                retVal_o['data'] = adjustId_p(id, data_o)
        else:
            # Anforderung der Liste
            data_o = self.db_o.read_px(id)
            data_komponent = self.db_komponent.read_px()
            data_fehler = self.db_fehler.read_px()

            data_tmp = {}
            data_exit = {}

            for key_s in data_komponent:
                if data_o['name'] == data_komponent[key_s]['projekt']:
                    data_tmp[key_s] = data_komponent[key_s]

            for key_k in data_tmp:
                for key_f in data_fehler:
                    if data_tmp[key_k]['name'] == data_fehler[key_f]['komponente']:
                        data_exit[key_f] = data_fehler[key_f]


            # Anforderung eines Dokuments
            retVal_o['data'] = data_exit
            retVal_o['data_komponent'] = data_o


        return retVal_o

class ProjektKategorieAuswertung_cl(object):

    def __init__(self):
        # -------------------------------------------------------
        self.db_o = KategorieDatabase_cl()
        self.db_fehler = FehlerDatabase_cl()

    # -------------------------------------------------------
    def GET(self, id):
        # -------------------------------------------------------
        retVal_o = {
            'data': None,
            'data_fehler': None
        }
        if id == None:
            # Anforderung der Liste
            retVal_o['data'] = self.db_o.read_px()
            # Anforderung eines Dokuments
            data_o = self.db_o.read_px(id)
            if data_o != None:
                retVal_o['data'] = adjustId_p(id, data_o)
        else:
            # Anforderung der Liste
            data_o = self.db_o.read_px(id)
            data_fehler = self.db_fehler.read_px()

            data_tmp = {}

            for key_s in data_fehler:
                if id == data_fehler[key_s]['kategorie']:
                    data_tmp[key_s] = data_fehler[key_s]


            # Anforderung eines Dokuments
            retVal_o['data'] = data_tmp


        return retVal_o

class Komponenten_cl(object):

    def __init__(self):
        self.db_o = KomponenteDatabase_cl()
        self.db_proj = ProjektDatabase_cl()

    # -------------------------------------------------------
    def GET(self, id):
        # -------------------------------------------------------
        retVal_o = {
            'data': None,
            'data_projekt': None
        }

        if id == None:
            # Anforderung der Liste
            retVal_o['data'] = self.db_o.read_px()
            retVal_o['data_projekt'] = self.db_proj.read_px()
        else:
            # Anforderung eines Dokuments
            data_o = self.db_o.read_px(id)
            data_proj = self.db_proj.read_px(id)
            if data_o != None:
                retVal_o['data'] = adjustId_p(id, data_o)
            if data_proj != None:
                retVal_o['data_projekt'] = data_proj

        print(retVal_o['data_projekt'])
        print(retVal_o)
        return retVal_o

    # -------------------------------------------------------
    def POST(self, data_opl):
        # -------------------------------------------------------
        retVal_o = {
            'id': None
        }

        # data_opl: Dictionary mit den gelieferten key-value-Paaren

        data_o = {
            'name': data_opl["name_s"],
            'beschreibung': data_opl["beschreibung_s"],
            'projekt': data_opl["projekt_s"]
        }
        # Create-Operation
        id_s = self.db_o.create_px(data_o)
        retVal_o['id'] = id_s

        return retVal_o

    # -------------------------------------------------------
    def PUT(self, data_opl):
        # -------------------------------------------------------
        # Sichern der Daten: jetzt wird keine vollständige Seite
        # zurückgeliefert, sondern nur noch die Information, ob das
        # Speichern erfolgreich war

        retVal_o = {
            'id': None
        }

        # data_opl: Dictionary mit den gelieferten key-value-Paaren

        id_s = data_opl["id_s"]
        data_o = {
            'name': data_opl["name_s"],
            'beschreibung': data_opl["beschreibung_s"],
            'projekt': data_opl["projekt_s"]
        }
        # Update-Operation
        retVal_o['id'] = id_s
        if self.db_o.update_px(id_s, data_o):
            pass
        else:
            retVal_o['id'] = None

        return retVal_o

    # -------------------------------------------------------
    def DELETE(self, id):
        # -------------------------------------------------------
        # Eintrag löschen, nur noch Rückmeldung liefern
        retVal_o = {
            'id': id
        }

        if self.db_o.delete_px(id):
            pass
        else:
            retVal_o['id'] = None

        return retVal_o

class Fehler_cl(object):
#----------------------------------------------------------

   #-------------------------------------------------------
   def __init__(self):
   #-------------------------------------------------------
      self.db_o = FehlerDatabase_cl()
      self.db_komponente = KomponenteDatabase_cl()
      self.db_mitarbeiter = MitarbeiterDatabase_cl()
      self.db_kategorie = KategorieDatabase_cl()

   #-------------------------------------------------------
   def GET(self, id, **kwargs):
   #-------------------------------------------------------
      retVal_o = {
         'data': None,
         'data_komponente': None,
         'data_kategorie': None,
         'data_mitarbeiter': None,
         'abteilung': None
      }

      if kwargs != {}:
          type = kwargs['type']
          data_o = self.db_o.read_px(id)

          data_tmp = {}
          for key_s in data_o:
              if data_o[key_s]['fehlerstatus'] == type:
                  data_tmp[key_s] = data_o[key_s]
          retVal_o['data'] = data_tmp


      elif id == None:
         # Anforderung der Liste
         retVal_o['data'] = self.db_o.read_px()
         retVal_o['data_komponente'] = self.db_komponente.read_px()
         retVal_o['data_kategorie'] = self.db_kategorie.read_px()
         retVal_o['data_mitarbeiter'] = self.db_mitarbeiter.read_px()

      else:
         # Anforderung eines Dokuments
         data_o = self.db_o.read_px(id)
         data_komponente = self.db_komponente.read_px()
         data_mitarbeiter = self.db_mitarbeiter.read_px()
         data_kategorie = self.db_kategorie.read_px()
         if data_o != None:
            retVal_o['data'] = adjustId_p(id, data_o)
         if data_komponente != None:
            retVal_o['data_komponente'] = data_komponente
         if data_mitarbeiter != None:
            retVal_o['data_mitarbeiter'] = data_mitarbeiter
         if data_kategorie != None:
            retVal_o['data_kategorie'] = data_kategorie

      print(id)
      if id == '0' or id == None or id == 0:
          retVal_o['abteilung'] = 'QS'
      else:
          retVal_o['abteilung'] = 'SW'

      print(retVal_o)
      return retVal_o
      
   #-------------------------------------------------------
   def POST(self, data_opl):
   #-------------------------------------------------------
      retVal_o = {
         'id': None
      }
      print(data_opl)
      # data_opl: Dictionary mit den gelieferten key-value-Paaren

      # hier müsste man prüfen, ob die Daten korrekt vorliegen!


      data_o = {
         'komponente': data_opl["komponente_s"],
         'beschreibung': data_opl["beschreibung_s"],
         'mitarbeiter': data_opl["mitarbeiter_s"],
         'datum': data_opl["datum_s"],
         'kategorie': data_opl["kategorie_s"],
         'fehlerstatus': data_opl["fehlerstatus_s"]
      }
      # Create-Operation
      id_s = self.db_o.create_px(data_o)
      retVal_o['id'] = id_s

      return retVal_o
      
   #-------------------------------------------------------
   def PUT(self, data_opl):
   #-------------------------------------------------------
      # Sichern der Daten: jetzt wird keine vollständige Seite
      # zurückgeliefert, sondern nur noch die Information, ob das
      # Speichern erfolgreich war

      retVal_o = {
         'id': None
      }

      # data_opl: Dictionary mit den gelieferten key-value-Paaren
      # hier müsste man prüfen, ob die Daten korrekt vorliegen!

      id_s = data_opl["id_s"]
      data_o = {
         'komponente': data_opl["komponente_s"],
         'beschreibung': data_opl["beschreibung_s"],
         'mitarbeiter': data_opl["mitarbeiter_s"],
         'datum': data_opl["datum_s"],
         'kategorie': data_opl["kategorie_s"],
         'fehlerstatus': data_opl["fehlerstatus_s"]
      }
      # Update-Operation
      data_o['fehlerstatus'] = 'behoben'
      retVal_o['id'] = id_s
      if self.db_o.update_px(id_s, data_o):
         pass
      else:
         retVal_o['id'] = None

      return retVal_o

   #-------------------------------------------------------
   def DELETE(self, id):
   #-------------------------------------------------------
      # Eintrag löschen, nur noch Rückmeldung liefern
      retVal_o = {
         'id': id
      }

      if self.db_o.delete_px(id):
         pass
      else:
         retVal_o['id'] = None

      return retVal_o

class Mitarbeiter_cl(object):
    # ----------------------------------------------------------

    # -------------------------------------------------------
    def __init__(self):
        # -------------------------------------------------------
        self.db_o = MitarbeiterDatabase_cl()

    # -------------------------------------------------------
    def GET(self, id):
        # -------------------------------------------------------
        retVal_o = {
            'data': None
        }
        if id == None:
            # Anforderung der Liste
            retVal_o['data'] = self.db_o.read_px()
        else:
            # Anforderung eines Dokuments
            data_o = self.db_o.read_px(id)
            if data_o != None:
                retVal_o['data'] = adjustId_p(id, data_o)

        return retVal_o

    # -------------------------------------------------------
    def POST(self, data_opl):
        # -------------------------------------------------------
        retVal_o = {
            'id': None
        }

        # data_opl: Dictionary mit den gelieferten key-value-Paaren

        data_o = {
            'name': data_opl["name_s"],
            'vorname': data_opl["vorname_s"],
            'alter': data_opl["alter_s"],
            'abteilung': data_opl["abteilung_s"]
        }
        # Create-Operation
        id_s = self.db_o.create_px(data_o)
        retVal_o['id'] = id_s

        return retVal_o

    # -------------------------------------------------------
    def PUT(self, data_opl):
        # -------------------------------------------------------
        # Sichern der Daten: jetzt wird keine vollständige Seite
        # zurückgeliefert, sondern nur noch die Information, ob das
        # Speichern erfolgreich war

        retVal_o = {
            'id': None
        }

        # data_opl: Dictionary mit den gelieferten key-value-Paaren

        id_s = data_opl["id_s"]
        data_o = {
            'name': data_opl["name_s"],
            'vorname': data_opl["vorname_s"],
            'alter': data_opl["alter_s"],
            'abteilung': data_opl["abteilung_s"]
        }
        # Update-Operation
        retVal_o['id'] = id_s
        if self.db_o.update_px(id_s, data_o):
            pass
        else:
            retVal_o['id'] = None

        return retVal_o

    # -------------------------------------------------------
    def DELETE(self, id):
        # -------------------------------------------------------
        # Eintrag löschen, nur noch Rückmeldung liefern
        retVal_o = {
            'id': id
        }

        if self.db_o.delete_px(id):
            pass
        else:
            retVal_o['id'] = None

        return retVal_o

class Kategorie_cl(object):

        # -------------------------------------------------------
        def __init__(self):
            # -------------------------------------------------------
            self.db_o = KategorieDatabase_cl()
        # -------------------------------------------------------
        def GET(self, id):
            # -------------------------------------------------------
            retVal_o = {
                'data': None
            }
            if id == None:
                # Anforderung der Liste
                retVal_o['data'] = self.db_o.read_px()
            else:
                # Anforderung eines Dokuments
                data_o = self.db_o.read_px(id)
                if data_o != None:
                    retVal_o['data'] = adjustId_p(id, data_o)

            return retVal_o

        # -------------------------------------------------------
        def POST(self, data_opl):
            # -------------------------------------------------------
            retVal_o = {
                'id': None
            }
            # data_opl: Dictionary mit den gelieferten key-value-Paaren
            # hier müsste man prüfen, ob die Daten korrekt vorliegen!
            data_o = {
                'fehlerbeschreibung': data_opl["fehlerbeschreibung_s"],
                'fehlerursache': data_opl["fehlerursache_s"]
                }
            # Create-Operation
            id_s = self.db_o.create_px(data_o)
            retVal_o['id'] = id_s
            return retVal_o

        # -------------------------------------------------------
        def PUT(self, data_opl):
            # -------------------------------------------------------
            # Sichern der Daten: jetzt wird keine vollständige Seite
            # zurückgeliefert, sondern nur noch die Information, ob das
            # Speichern erfolgreich war

            retVal_o = {
                'id': None
            }

            # data_opl: Dictionary mit den gelieferten key-value-Paaren
            # hier müsste man prüfen, ob die Daten korrekt vorliegen!

            id_s = data_opl["id_s"]
            data_o = {
                'fehlerbeschreibung': data_opl["fehlerbeschreibung_s"],
                'fehlerursache': data_opl["fehlerursache_s"]
            }
            # Update-Operation
            retVal_o['id'] = id_s
            if self.db_o.update_px(id_s, data_o):
                pass
            else:
                retVal_o['id'] = None

            return retVal_o

        # -------------------------------------------------------
        def DELETE(self, id):
            # -------------------------------------------------------
            # Eintrag löschen, nur noch Rückmeldung liefern
            retVal_o = {
                'id': id
            }

            if self.db_o.delete_px(id):
                pass
            else:
                retVal_o['id'] = None

            return retVal_o

class AuswertungProjekte_cl(object):
            # ----------------------------------------------------------

            # -------------------------------------------------------
            def __init__(self):
                # -------------------------------------------------------
                self.db_o = AuswertungProjekteDatabase_cl()

            # -------------------------------------------------------
            def GET(self, id):
                # -------------------------------------------------------
                retVal_o = {
                    'data': None
                }
                if id == None:
                    # Anforderung der Liste
                    retVal_o['data'] = self.db_o.read_px()
                else:
                    # Anforderung eines Dokuments
                    data_o = self.db_o.read_px(id)
                    if data_o != None:
                        retVal_o['data'] = adjustId_p(id, data_o)

                return retVal_o

            # -------------------------------------------------------
            def POST(self, data_opl):
                # -------------------------------------------------------
                retVal_o = {
                    'id': None
                }

                # data_opl: Dictionary mit den gelieferten key-value-Paaren

                # hier müsste man prüfen, ob die Daten korrekt vorliegen!

                data_o = {
                    'name': data_opl["name_s"],
                    'fehlerstatus': data_opl["fehlerstatus_s"]

                }
                # Create-Operation
                id_s = self.db_o.create_px(data_o)
                retVal_o['id'] = id_s

                return retVal_o

            # -------------------------------------------------------
            def PUT(self, data_opl):
                # -------------------------------------------------------
                # Sichern der Daten: jetzt wird keine vollständige Seite
                # zurückgeliefert, sondern nur noch die Information, ob das
                # Speichern erfolgreich war

                retVal_o = {
                    'id': None
                }

                # data_opl: Dictionary mit den gelieferten key-value-Paaren
                # hier müsste man prüfen, ob die Daten korrekt vorliegen!

                id_s = data_opl["id_s"]
                data_o = {
                    'name': data_opl["name_s"],
                    'fehlerstatus': data_opl["fehlerstatus_s"]
                }
                # Update-Operation
                retVal_o['id'] = id_s
                if self.db_o.update_px(id_s, data_o):
                    pass
                else:
                    retVal_o['id'] = None

                return retVal_o

            # -------------------------------------------------------
            def DELETE(self, id):
                # -------------------------------------------------------
                # Eintrag löschen, nur noch Rückmeldung liefern
                retVal_o = {
                    'id': id
                }

                if self.db_o.delete_px(id):
                    pass
                else:
                    retVal_o['id'] = None

                return retVal_o

class AuswertungKategorie_cl(object):
                # ----------------------------------------------------------

                # -------------------------------------------------------
                def __init__(self):
                    # -------------------------------------------------------
                    self.db_o = AuswertungKategorieDatabase_cl()

                # -------------------------------------------------------
                def GET(self, id):
                    # -------------------------------------------------------
                    retVal_o = {
                        'data': None
                    }
                    if id == None:
                        # Anforderung der Liste
                        retVal_o['data'] = self.db_o.read_px()
                    else:
                        # Anforderung eines Dokuments
                        data_o = self.db_o.read_px(id)
                        if data_o != None:
                            retVal_o['data'] = adjustId_p(id, data_o)

                    return retVal_o

                # -------------------------------------------------------
                def POST(self, data_opl):
                    # -------------------------------------------------------
                    retVal_o = {
                        'id': None
                    }

                    # data_opl: Dictionary mit den gelieferten key-value-Paaren

                    # hier müsste man prüfen, ob die Daten korrekt vorliegen!

                    data_o = {
                        'fehlerbeschreibung': data_opl["fehlerbeschreibung_s"],
                        'fehlerursache': data_opl["fehlerursache_s"],
                        'fehlerstatus': data_opl["fehlerstatus_s"]

                    }
                    # Create-Operation
                    id_s = self.db_o.create_px(data_o)
                    retVal_o['id'] = id_s

                    return retVal_o

                # -------------------------------------------------------
                def PUT(self, data_opl):
                    # -------------------------------------------------------
                    # Sichern der Daten: jetzt wird keine vollständige Seite
                    # zurückgeliefert, sondern nur noch die Information, ob das
                    # Speichern erfolgreich war

                    retVal_o = {
                        'id': None
                    }

                    # data_opl: Dictionary mit den gelieferten key-value-Paaren
                    # hier müsste man prüfen, ob die Daten korrekt vorliegen!

                    id_s = data_opl["id_s"]
                    data_o = {
                        'fehlerbeschreibung': data_opl["fehlerbeschreibung_s"],
                        'fehlerursache': data_opl["fehlerursache_s"],
                        'fehlerstatus': data_opl["fehlerstatus_s"]
                    }
                    # Update-Operation
                    retVal_o['id'] = id_s
                    if self.db_o.update_px(id_s, data_o):
                        pass
                    else:
                        retVal_o['id'] = None

                    return retVal_o

                # -------------------------------------------------------
                def DELETE(self, id):
                    # -------------------------------------------------------
                    # Eintrag löschen, nur noch Rückmeldung liefern
                    retVal_o = {
                        'id': id
                    }

                    if self.db_o.delete_px(id):
                        pass
                    else:
                        retVal_o['id'] = None

                    return retVal_o



#----------------------------------------------------------
class Application_cl(object):
#----------------------------------------------------------

   exposed = True # gilt für alle Methoden

   #-------------------------------------------------------
   def __init__(self):
   #-------------------------------------------------------
      self.handler_o = {
         'Projekt': Projekt_cl(),
         'Fehler': Fehler_cl(),
         'Komponenten': Komponenten_cl(),
         'Mitarbeiter': Mitarbeiter_cl(),
         'Kategorie': Kategorie_cl(),
         'AuswertungProjekte': ProjektfehlerAuswertung_cl(),
         'AuswertungKategorie': ProjektKategorieAuswertung_cl(),
         'Projektkomponente': Projektkomponente_cl()
      }

   # es wird keine index-Methode vorgesehen, weil stattdessen
   # die Webseite index.html ausgeliefert wird (siehe Konfiguration)

   #-------------------------------------------------------
   def GET(self, path_spl = 'Projekt', id=None):
   #-------------------------------------------------------
      retVal_o = {
         'data': None
      }

      if path_spl in self.handler_o:
         retVal_o = self.handler_o[path_spl].GET(id)

      if retVal_o['data'] == None:
         cherrypy.response.status = 404

      return json.dumps(retVal_o)


   def GET(self, path_spl='Fehler', id=None, **kwargs):
    # -------------------------------------------------------
        retVal_o = {
            'data': None
        }

        if path_spl in self.handler_o:
            retVal_o = self.handler_o[path_spl].GET(id, **kwargs)

        if retVal_o['data'] == None:
            cherrypy.response.status = 404

        return json.dumps(retVal_o)
      
   #-------------------------------------------------------

   def POST(self, path_spl = 'Projekt', **data_opl):
   #-------------------------------------------------------
      retVal_o = {
         'id': None
      }

      # data_opl: Dictionary mit den gelieferten key-value-Paaren

      # hier müsste man prüfen, ob die Daten korrekt vorliegen!

      if path_spl in self.handler_o:
         retVal_o = self.handler_o[path_spl].POST(data_opl)

      if retVal_o['id'] == None:
         cherrypy.response.status = 409
         
      return json.dumps(retVal_o)
      
   #-------------------------------------------------------
   def PUT(self, path_spl = 'Projekt', **data_opl):
   #-------------------------------------------------------
      # Sichern der Daten: jetzt wird keine vollständige Seite
      # zurückgeliefert, sondern nur noch die Information, ob das
      # Speichern erfolgreich war

      retVal_o = {
         'id': None
      }

      # data_opl: Dictionary mit den gelieferten key-value-Paaren
      # hier müsste man prüfen, ob die Daten korrekt vorliegen!

      if path_spl in self.handler_o:
         retVal_o = self.handler_o[path_spl].PUT(data_opl)

      if retVal_o['id'] == None:
         cherrypy.response.status = 404

      return json.dumps(retVal_o)

   #-------------------------------------------------------
   def DELETE(self, path_spl = 'Projekt', id=None):
   #-------------------------------------------------------
      # Eintrag löschen, nur noch Rückmeldung liefern
      retVal_o = {
         'id': id
      }

      if path_spl in self.handler_o:
         retVal_o = self.handler_o[path_spl].DELETE(id)

      if retVal_o['id'] == None:
         cherrypy.response.status = 404

      return json.dumps(retVal_o)

   #-------------------------------------------------------
   def default(self, *arguments, **kwargs):
   #-------------------------------------------------------
      msg_s = "unbekannte Anforderung: " + \
              str(arguments) + \
              ' ' + \
              str(kwargs)
      raise cherrypy.HTTPError(404, msg_s) 

# EOF
