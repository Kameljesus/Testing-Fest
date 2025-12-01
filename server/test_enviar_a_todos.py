# server/test_enviar_a_todos.py
import unittest
from utils import enviar_a_todos, lista_de_clientes

class ClienteSimulado:
    """
    Cliente falso para testeo. Tiene un método 'send' que guarda los mensajes.
    """
    def __init__(self):
        self.recibidos = []

    def send(self, mensaje_bytes):
        # Decodificamos el mensaje y lo guardamos
        self.recibidos.append(mensaje_bytes.decode("utf-8"))

class TestServidor(unittest.TestCase):

    def setUp(self):
        # Limpiamos la lista global antes de cada test
        lista_de_clientes.clear()

        # Creamos clientes simulados
        self.cliente1 = ClienteSimulado()
        self.cliente2 = ClienteSimulado()
        self.cliente3 = ClienteSimulado()

        # Añadimos a la lista global (nombre, conexion)
        lista_de_clientes.extend([
            ("c1", self.cliente1),
            ("c2", self.cliente2),
            ("c3", self.cliente3)
        ])

    def test_reenvio_a_los_demas(self):
        # =========================
        # Arrange
        # =========================
        mensaje = "Hola a todos"

        # =========================
        # Act
        # =========================
        enviar_a_todos(mensaje, self.cliente1)

        # =========================
        # Assert
        # =========================

        # Verificamos que los demás clientes recibieron el mensaje
        self.assertEqual(self.cliente2.recibidos, [mensaje])
        self.assertEqual(self.cliente3.recibidos, [mensaje])

        # El cliente que envió NO debería recibirlo
        self.assertEqual(self.cliente1.recibidos, [])

if __name__ == '__main__':
    unittest.main()
