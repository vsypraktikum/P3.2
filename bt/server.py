#coding: utf-8
import os
import cherrypy
from app import application, templates, navigation

#--------------------------------------
def main():
#--------------------------------------
   # Get current directory
   try:
      current_dir = os.path.dirname(os.path.abspath(__file__))
   except:
      current_dir = os.path.dirname(os.path.abspath(sys.executable))
   # disable autoreload and timeout_monitor
   cherrypy.engine.autoreload.unsubscribe()
   # cherrypy.engine.timeout_monitor.unsubscribe()
   # Static content config
   staticConfig_o = {
      '/': {
            'tools.staticdir.root': current_dir,
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './static',
            'tools.staticdir.index': './html/index.html',
            'request.dispatch': cherrypy.dispatch.MethodDispatcher()
      },
      '/favicon.ico': {
         'tools.staticfile.on': True,
         'tools.staticfile.filename': current_dir+'/static/images/favicon.ico'
      }
   }
   staticConfig2_o = {
      '/': {
         'request.dispatch': cherrypy.dispatch.MethodDispatcher()
      }
   }
   cherrypy.config.update({
      'tools.log_headers.on':  True,
      'tools.sessions.on':     False,  
      'tools.encode.on':       True,
      'tools.encode.encoding': 'utf-8',
      'server.socket_port':    8080,   
      'server.socket_timeout': 60,    
      'server.thread_pool':    10,      
      'server.environment':    'production',
      'log.screen':            True,
      'request.show_tracebacks': False
   })

   # Request-Handler definieren
   cherrypy.tree.mount(application.Application_cl(), '/', staticConfig_o)
   cherrypy.tree.mount(templates.Templates_cl(), '/templates', staticConfig2_o)
   cherrypy.tree.mount(navigation.Navigation_cl(), '/navigation', staticConfig2_o)

   # Start server
   cherrypy.engine.start()
   cherrypy.engine.block()

#--------------------------------------
if __name__ == '__main__':
#--------------------------------------
   main()
# EOF
