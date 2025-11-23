## Conceptos:

# Prueba Unitaria:

    Es un bloque de código que verifica la precisión de un componente pequeño y aislado del software, como una función o método. El objetivo es asegurar que cada unidad funcione como se espera, identificando errores en las primeras etapas del desarrollo y facilitando la depuración. Estas pruebas son ejecutadas por los desarrolladores y se clasifican como de caja blanca porque se centran en el código interno. 

# Framework de pruebas (pytest o unittest):

    Un framework de pruebas es una estructura o conjunto de herramientas, directrices y prácticas que proporcionan un entorno estandarizado para la automatización de pruebas de software.

# Aserciones (assert):

    Las aserciones (assert) son sentencias de programación que afirman que una condición debe ser verdadera en un punto específico del código.

    Ejemplo: La función hace una suma entre dos números:

    primer_numero = 1.

    segundo_numero = 2.

    Assert de la función: primer_numero + segundo_numero (3).

# Mocking:

    El mocking es una técnica de desarrollo de software que utiliza simulaciones o mocks para aislar y probar una unidad de código. Se reemplazan los componentes externos reales (como bases de datos o APIs) por objetos simulados para poder ejecutar pruebas de forma controlada y predecible, sin depender de recursos externos que podrían no estar listos o ser inestables. 

    Ejemplo: Probar la función que elimina a un cliente de la base de datos sin usar la verdadera base de datos.

# Test de funciones puras:

    Un "Test de funciones puras" se refiere a las pruebas realizadas en funciones que siempre producen la misma salida para la misma entrada y no tienen efectos secundarios (no modifican variables externas ni estados). Estas pruebas son sencillas porque se centran en verificar la relación directa entre la entrada y la salida, asegurando que el resultado sea siempre predecible. 

    Funciones puras → fáciles de testear. No modifican nada externos a estas mismas.

# Funciones con efectos secundarios:

    Las funciones con efectos secundarios son aquellas que, además de devolver un valor, realizan cambios observables en su entorno. Estos efectos pueden incluir la modificación de variables globales, la escritura en un archivo o la consola, o la interacción con el sistema de base de datos. A diferencia de las funciones puras, las funciones con efectos secundarios pueden tener comportamientos impredecibles, lo que dificulta su depuración. 

    Funciones que hacen cosas reales (leer archivos, enviar datos, sockets) → necesitan mocks.

# Caja Negra:

    En programación, una "caja negra" se refiere a un sistema o método cuyo funcionamiento interno está oculto para el usuario o probador, que solo conoce las entradas y salidas esperadas.

    Ejemplo: Ejecutar la función sumar para ver si esta suma dos números correctamente, verificando esta última por medio del resultado.

# Caja Blanca:

    En programación, la caja blanca es un tipo de prueba de software que examina el funcionamiento interno del código, la estructura y la lógica del programa. A diferencia de las pruebas de caja negra, que no requieren conocimiento del código, el probador de caja blanca tiene acceso al código fuente para verificar su correcto funcionamiento, descubrir vulnerabilidades y asegurar que todas las rutas de ejecución, condiciones y bucles se comporten según lo esperado. 

    Ejemplo: Ver cómo la función sumar lee los dos números y qué hace con ellos en realidad para ver si se suman correctamente.

# Pruebas de errores (tests que esperan fallos):

    Concepto:
    Verificar que una función maneje mal uso, errores o datos inválidos.

    Analogía:
    Ver si un paracaídas tiene un plan B cuando el primero no abre.

# Cobertura de Código (Code Coverage):

    La cobertura de código es una métrica de pruebas de software que mide qué porcentaje del código fuente de un programa se ejecuta cuando se ejecutan un conjunto de pruebas. Su objetivo principal es ayudar a los desarrolladores a identificar qué partes del código no han sido probadas y, de este modo, mejorar la calidad del software al detectar brechas en las pruebas. 

# Testeo de concurrencia / hilos:

    El testeo de concurrencia y hilos es el proceso de verificar que una aplicación pueda manejar múltiples tareas ejecutándose simultáneamente (concurrencia) sin errores, especialmente cuando esas tareas (hilos) comparten recursos como la memoria.

# Testeo de sockets:

    Un testeo de sockets en programación es el proceso de verificar que la comunicación entre dos puntos finales (sockets) de una red funcione correctamente, asegurando que los datos se envíen y reciban de manera fiable entre clientes y servidores.