# Suite de QA Automation E2E: Autenticación y Flujo de Compra con Playwright y Pytest

Este proyecto implementa pruebas automatizadas de interfaz de usuario (**UI End-to-End Testing**) sobre la plataforma de comercio electrónico **SauceDemo**, utilizando localizadores modernos accesibles y generación automática de evidencias visuales.

## Escenarios Automatizados (5/5 Aprobados)

1. **Login Exitoso (Happy Path):** Validación de acceso con credenciales autorizadas y redirección al catálogo de inventario.
2. **Login con Contraseña Incorrecta:** Verificación del bloqueo de seguridad y mensaje de alerta ante clave inválida.
3. **Login con Usuario Inexistente:** Prueba negativa de control de acceso para cuentas no registradas en el sistema.
4. **Validación de Campos Obligatorios:** Control de envío de formulario vacío para asegurar la exigencia de datos requeridos.
5. **Flujo Completo de Compra (E2E):** Recorrido integral desde el inicio de sesión, selección de producto, verificación de inventario en carrito, formulario de envío (*Checkout*) y confirmación final de orden.

## Evidencias Generadas

Cada ejecución genera automáticamente capturas de pantalla (`.png`) de respaldo para auditoría de calidad en cada escenario evaluado.

## Tecnologías Utilizadas

* **Lenguaje:** Python 3
* **Automatización Web:** Playwright (Chromium)
* **Framework de Pruebas:** Pytest