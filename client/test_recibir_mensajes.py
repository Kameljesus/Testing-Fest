# client/test_integration_client_8000.py
import unittest
import subprocess
import socket
import threading
import time
import sys

HOST = 'localhost'
PORT = 8000 

# =========================
# Servidor de prueba que simula mensajes
# =========================
def servidor_simulado(mensajes):
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.bind((HOST, PORT))
    server_sock.listen(1)
    
    # Aceptar conexión del cliente
    conn, addr = server_sock.accept()
    
    # Recibir el nombre del cliente (primer mensaje)
    conn.recv(1024)
    
    # Enviar los mensajes al cliente
    for msg in mensajes:
        conn.send(msg.encode('utf-8'))
        time.sleep(0.1)
    
    # Cerrar conexión
    conn.close()
    server_sock.close()


# =========================
# Test de integración
# =========================
class TestClienteIntegration(unittest.TestCase):
    
    def test_recibir_mensajes(self):
        # =========================
        # Arrange
        # =========================
        mensajes = ["Hola, test!", "Segundo mensaje", ""]  # Mensajes que enviará el servidor
        hilo_servidor = threading.Thread(target=servidor_simulado, args=(mensajes,))
        hilo_servidor.start()
        
        # Lanzamos el cliente como subproceso
        cliente_proc = subprocess.Popen(
            [sys.executable, "client.py"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        # =========================
        # Act
        # =========================
        # Enviar el nombre del cliente
        cliente_proc.stdin.write("Tester\n")
        cliente_proc.stdin.flush()
        
        # Esperamos un momento para que el cliente reciba los mensajes
        time.sleep(1)
        
        # Enviar comando para cerrar cliente
        cliente_proc.stdin.write("/exit\n")
        cliente_proc.stdin.flush()
        
        # Esperamos a que el cliente termine
        cliente_proc.wait(timeout=5)
        
        # Capturamos la salida completa del cliente
        salida = cliente_proc.stdout.read()
        
        # =========================
        # Assert
        # =========================
        self.assertIn("Hola, test!", salida)
        self.assertIn("Segundo mensaje", salida)
        
        # Aseguramos que el servidor termine
        hilo_servidor.join()


# =========================
# Ejecutar los tests
# =========================
if __name__ == "__main__":
    unittest.main()
