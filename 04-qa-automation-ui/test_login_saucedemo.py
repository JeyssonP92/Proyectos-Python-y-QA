from playwright.sync_api import sync_playwright

URL_LOGIN = "https://saucedemo.com"

def test_login_exitoso():
    """Escenario 1: Verifica acceso correcto usando localizadores accesibles."""
    with sync_playwright() as p: #Inicia la sesión de Playwright de forma segura y garantiza que los recursos de memoria se liberen al terminar
        navegador = p.chromium.launch(headless=False, slow_mo=1000) #headless=False para ver la ejecución, slow_mo=1000 para ralentizar la acción
        pagina = navegador.new_page()
        pagina.goto(URL_LOGIN)
        
        # Localizamos las cajas por el texto de ayuda visible (Placeholder)
        pagina.get_by_placeholder("Username").fill("standard_user") #get_by_placeholder busca el campo de entrada por su texto de ayuda y lo llena con el valor proporcionado
        pagina.get_by_placeholder("Password").fill("secret_sauce") #.fill() simula al usuario escribiendo las credenciales dentro del campo 
        # Localizamos el botón por su rol web y nombre visible
        pagina.get_by_role("button", name="Login").click() #get_by_role busca el botón por su rol y nombre visible, y .click() simula un clic en él
        
        assert "inventory.html" in pagina.url, "Error QA: No ingresó al inventario."
        pagina.screenshot(path="evidencia_login_exitoso.png") #pagina.screenshot() toma una captura de pantalla de la página actual y la guarda en el archivo especificado para documentar la evidencia del test
        navegador.close() #Cierra el navegador y libera los recursos de memoria utilizados por Playwright

def test_login_fallido():
    """Escenario 2: Verifica bloqueo de seguridad ante contraseña incorrecta."""
    with sync_playwright() as p:
        navegador = p.chromium.launch(headless=False, slow_mo=1000)
        pagina = navegador.new_page()
        pagina.goto(URL_LOGIN)
        
        pagina.get_by_placeholder("Username").fill("standard_user")
        pagina.get_by_placeholder("Password").fill("wrong_password")
        pagina.get_by_role("button", name="Login").click()
        
        mensaje_error = pagina.locator("[data-test='error']").inner_text()
        assert "Username and password do not match" in mensaje_error, f"Error QA: Mensaje inesperado '{mensaje_error}'"
        
        pagina.screenshot(path="evidencia_login_fallido.png")
        navegador.close()

def test_login_campos_vacios():
    """Escenario 3: Verifica obligatoriedad de campos al enviar el formulario vacío."""
    with sync_playwright() as p:
        navegador = p.chromium.launch(headless=False, slow_mo=1000)
        pagina = navegador.new_page()
        pagina.goto(URL_LOGIN)
        
        pagina.get_by_role("button", name="Login").click()
        
        mensaje_error = pagina.locator("[data-test='error']").inner_text()
        assert "Username is required" in mensaje_error, f"Error QA: No exigió usuario '{mensaje_error}'"
        
        pagina.screenshot(path="evidencia_campos_vacios.png")
        navegador.close()   
        
def test_login_usuario_inexistente():
    """Escenario 4: Verifica bloqueo de seguridad ante usuario inexistente."""
    with sync_playwright() as p:
        navegador = p.chromium.launch(headless=False, slow_mo=1000)
        pagina = navegador.new_page()
        pagina.goto(URL_LOGIN)
        
        pagina.get_by_placeholder("Username").fill("nonexistent_user")
        pagina.get_by_placeholder("Password").fill("secret_sauce")
        pagina.get_by_role("button", name="Login").click()
        
        mensaje_error = pagina.locator("[data-test='error']").inner_text()
        assert "Username and password do not match" in mensaje_error, f"Error QA: Mensaje inesperado '{mensaje_error}'"
        
        pagina.screenshot(path="evidencia_usuario_inexistente.png")
        navegador.close()

def test_flujo_compra_completo():
    """Escenario 5: Verifica flujo completo de compra desde login, agregar producto, carrito, checkout y confirmación."""
    with sync_playwright() as p:
        navegador = p.chromium.launch(headless=False, slow_mo=1000)
        pagina = navegador.new_page()
        pagina.goto(URL_LOGIN)
        
        # Login exitoso
        pagina.get_by_placeholder("Username").fill("standard_user")
        pagina.get_by_placeholder("Password").fill("secret_sauce")
        pagina.get_by_role("button", name="Login").click()
        
        assert "inventory.html" in pagina.url, "Error QA: No ingresó al inventario."
        
        # Agregar un producto al carrito
        pagina.locator("[data-test='add-to-cart-sauce-labs-backpack']").click()
        
        # Verificar que el carrito tenga 1 producto
        carrito_cantidad = pagina.locator(".shopping_cart_badge").inner_text()
        assert carrito_cantidad == "1", f"Error QA: Se esperaba 1 producto en el carrito, tiene '{carrito_cantidad}'"
        
        # Entrar al carrito para verificar el producto agregado
        pagina.locator(".shopping_cart_link").click()
        producto_en_carrito = pagina.locator(".inventory_item_name").inner_text()
        assert "Sauce Labs Backpack" in producto_en_carrito, f"Error QA: el producto no está en el carrito"
        
        # Iniciar checkout
        pagina.get_by_role("button", name="Checkout").click()
        
        # Completar información de checkout
        pagina.get_by_placeholder("First Name").fill("Jeysson")
        pagina.get_by_placeholder("Last Name").fill("Peña")
        pagina.get_by_placeholder("Zip/Postal Code").fill("12345")
        pagina.get_by_role("button", name="Continue").click()
        
        # Confirmar orden en el resumen final (Overview)
        assert "checkout-step-two.html" in pagina.url, "Error QA: No cargó el resumen de pago."
        pagina.get_by_role("button", name="Finish").click()
        
        # Verificar mensaje de finalización de compra
        mensaje_finalizacion = pagina.locator(".complete-header").inner_text()
        assert "Thank you for your order" in mensaje_finalizacion, f"Error QA: Compra no finalizada correctamente '{mensaje_finalizacion}'"
        
        pagina.screenshot(path="evidencia_de_compra_exitosa.png")
        navegador.close()        