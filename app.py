import cherrypy
import tenjin
from tenjin.helpers import *

class SimpleSample:
    @cherrypy.expose
    def index(self):
        return "Hello World!"

    @cherrypy.expose
    def tenjin(self):
        context = {
            'sample1': 'teste',
            'sample2': 'Olá mundo'
        }

        engine = tenjin.Engine(path=['views'])
        html = engine.render('mytemplate1.pyhtml', context)
        return html

if __name__ == '__main__':
    cherrypy.quickstart(SimpleSample(), '/')
