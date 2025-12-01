# server/test_manejar_cliente.py

import unittest
from unittest.mock import MagicMock, patch
from utils import manejar_cliente, lista_de_clientes, enviar_a_todos

class TestManejarCliente(unittest.TestCase):
    """
    Testea la función manejar_cliente de utils.py.
    
    Casos:
    1. Desconexión abrupta (mensaje vacío)
    2. Desconexión controlada (/exit)
    3. Envío de mensaje normal (reenvío + confirmación)
    """

    def setUp(self):
        # =========================
        # Arrange común a todos los tests
        # =========================
        lista_de_clientes.clear()  # Limpiamos la lista global antes de cada test

        # Creamos un mock de conexión
        self.mock_conexion = MagicMock()
        self.mock_conexion.send = MagicMock()
        self.mock_conexion.close = MagicMock()

        # Mock de server_socket
        self.mock_server_socket = MagicMock()

        # Dirección simulada del cliente
        self.addr = ('127.0.0.1', 12345)

    # -------------------------
    # Test 1: Desconexión abrupta
    # -------------------------
    def test_desconexion_abrupta(self):
        # =========================
        # Arrange
        # Cliente se desconecta abruptamente enviando mensaje vacío
        self.mock_conexion.recv = MagicMock(side_effect=[b'ClienteAbrupto', b''])
        
        # =========================
        # Act
        manejar_cliente(self.mock_server_socket, lista_de_clientes, self.mock_conexion, self.addr)
        
        # =========================
        # Assert
        # Verificar que el cliente se removió de la lista y se cerró la conexión
        self.assertNotIn(('ClienteAbrupto', self.mock_conexion), lista_de_clientes)
        self.mock_conexion.close.assert_called_once()

    # -------------------------
    # Test 2: Desconexión controlada (/exit)
    # -------------------------
    @patch('sys.exit')  # Parcheamos sys.exit para que no termine el test
    def test_desconexion_controlada(self, mock_exit):
        # =========================
        # Arrange
        # Cliente envía su nombre y luego comando /exit
        self.mock_conexion.recv = MagicMock(side_effect=[b'ClienteExit', b'/exit'])
        
        # =========================
        # Act
        manejar_cliente(self.mock_server_socket, lista_de_clientes, self.mock_conexion, self.addr)
        
        # =========================
        # Assert
        # Cliente removido de la lista
        self.assertNotIn(('ClienteExit', self.mock_conexion), lista_de_clientes)
        # Conexión cerrada
        self.mock_conexion.close.assert_called_once()
        # sys.exit NO debe llamarse en el test
        mock_exit.assert_not_called()

    # -------------------------
    # Test 3: Envío de mensaje normal
    # -------------------------
    @patch('utils.enviar_a_todos')  # Parcheamos enviar_a_todos para no necesitar otros clientes
    def test_envio_mensaje_normal(self, mock_enviar_a_todos):
        # =========================
        # Arrange
        # Cliente envía su nombre y un mensaje normal
        mensaje_cliente = b'Hola a todos'
        # Luego se desconecta con /exit
        self.mock_conexion.recv = MagicMock(side_effect=[b'Cliente1', mensaje_cliente, b'/exit'])
        
        # =========================
        # Act
        with patch('sys.exit'):  # Evitar que sys.exit cierre el test al final
            manejar_cliente(self.mock_server_socket, lista_de_clientes, self.mock_conexion, self.addr)
        
        # =========================
        # Assert
        # Verificar que enviar_a_todos se llamó con el mensaje completo
        mensaje_completo = 'Cliente1: Hola a todos'
        mock_enviar_a_todos.assert_called_with(mensaje_completo, self.mock_conexion)
        # Verificar que se envió confirmación al cliente
        self.mock_conexion.send.assert_any_call(b'Mensaje recibido...')
        # Cliente removido de la lista al final
        self.assertNotIn(('Cliente1', self.mock_conexion), lista_de_clientes)
        # Conexión cerrada
        self.mock_conexion.close.assert_called_once()

# Ejecutar los tests
if __name__ == "__main__":
    unittest.main()
