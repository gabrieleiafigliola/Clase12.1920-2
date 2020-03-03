print("Esto es la clase 16")

class Jugador:

    def __init__(self,edad,correo,username, password):
        self.edad = edad
        self.correo = correo
        self.username = username
        self.password = password
        self.skins = []
    
    def jugar(self):
        pass


class Sistema:
    
    def __init__(self):
        self.jugadores = {}

    def mostrarMenu():
        pass

    def iniciarSesionConUsername(self,username,password):
        pass

    def iniciarSesionConCorreo(self,correo,password):
        pass

    def agregarJugador(self, jugador):
        self.jugadores[jugador.username] = jugador
        
    def verificarExistenciaDelJugador(self):
        pass

    def eliminarJugador(self,username):
        pass

    def cerrarSesion(self,jugador):
        pass

    def cambiarContrasena(self,contrasena):
        pass

    def mostrarJugadores(self):
        for key in self.jugadores:
            print("="*23)
            print("Username: {}".format(key))
            print("Edad: {}".format(self.jugadores[key].edad))
            print("Correo: {}".format(self.jugadores[key].correo))
            print("="*23)
sistema = Sistema()
jugador1 = Jugador(10,"user@user.com","user","1234567")
jugador2 = Jugador(11,"user2@user.com","user2","1234567")
sistema.agregarJugador(jugador1)
sistema.agregarJugador(jugador2)
sistema.mostrarJugadores()