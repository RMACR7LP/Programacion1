try:
    import cPickle as pickle
except ImportError:
    import pickle


class Usuario():
    
    def __init__(self,nombre):
        self.nombre = nombre
        
        
    def asignar_ultimasciudades(self,ciudad1,ciudad2,ciudad3):
        self.ciudad1=ciudad1
        self.ciudad2=ciudad2
        self.ciudad3=ciudad3
    
    def asignar_visitas(self,visitas1,visitas2,visitas3):
        self.visitas1=visitas1
        self.visitas2=visitas2
        self.visitas3=visitas3

    
        
        
        
    
    

   
adriana = Jugador("Cristian")
adriana.asignar_ultimasciudades('Bern', 'London', 'Topeka')
adriana.asignar_visitas(4,5,6)

archivo = open("jugadores.mat", "w")
pickle.dump(adriana, archivo,1)
archivo.close()

fichero = open('jugadores.mat', 'r')
adri = pickle.load(fichero)
print adri.nombre
print adri.visitas3