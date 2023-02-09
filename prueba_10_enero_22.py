class Registro:
    def __init__(self, fecha: float, servidor: str, usuario: str, contraseña: str):
        self.fecha: float = fecha
        self.servidor: str = servidor
        self.usuario: str = usuario
        self.contraseña: str = contraseña
class Ataque:
    def __init__(self, tipo: str, fecha_det: float, fecha_sol: float, servidores: list[str]):
        self.tipo: str = tipo
        self.fecha_detectado: float = fecha_det
        self.fecha_solucionado: float = fecha_sol
        self.servidores: list[str] = servidores
