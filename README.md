Automatización de Pruebas - Urban Routes
Proyecto de pruebas automatizadas E2E (End-to-End) para la plataforma web Urban Routes, desarrollado en Python aplicando el patrón de diseño Page Object Model (POM), Selenium WebDriver y Pytest.

Tecnologías Utilizadas
Lenguaje: Python 3.x

Framework de Pruebas: Pytest

Herramienta de Automatización: Selenium WebDriver

Navegador: Google Chrome (con Chrome DevTools Protocol habilitado)

Patrón de Diseño: Page Object Model (POM)

Descripción del Flujo Automatizado
El test test_set_route ejecuta y valida las siguientes interacciones dentro del flujo de reserva:

Configuración de Ruta: Ingreso de direcciones de origen (from) y destino (to).

Pedir Taxi: Interacción con el botón de solicitud e ingreso a la vista de tarifas.

Selección de Tarifa: Elección de la opción Comfort.

Verificación de Teléfono: Inserción de número de celular y captura dinámica del código SMS a través de logs de rendimiento del navegador (goog:loggingPrefs).

Método de Pago: Apertura del modal de pagos, vinculación de tarjeta de crédito/débito y confirmación.

Comentarios al Conductor: Inserción de instrucciones adicionales en el campo de texto.

Adicionales de Viaje: Activación del interruptor de Manta y pañuelos.

Contadores Adicionales: Incremento a 2 unidades del pedido de Helado.

Búsqueda de Conductor: Confirmación y envío final del pedido.

Aserciones: Validación de coincidencia de direcciones ingresadas con la vista activa.


Estructura del Proyecto

qa-project-Urban-Routes-es/
│
├── data.py          # Configuración de URLs, credenciales y datos de prueba.
├── main.py          # Definición de clases UrbanRoutesPage, TestUrbanRoutes y helper de SMS.
├── README.md        # Documentación general del proyecto.


Requisitos e Instalación

Clonar el repositorio
Bash
git clone Url
cd qa-project-Urban-Routes-es

Instalar dependencias
pip install selenium pytest

Ejecución de Pruebas
pytest main.py