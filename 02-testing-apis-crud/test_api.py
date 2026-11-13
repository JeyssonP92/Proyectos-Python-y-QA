import requests 

#Bsae URL del servidor de pruebas de la API
BASE_URL = "https://jsonplaceholder.typicode.com"

def test_obtener_post_exitoso():
    """ [Test1] prueba exitosa.
    verfica que la API devuelve un código de estado 200 y que el contenido
    del post es correcto."""
    print("\n Iniciando prueba de obtener post exitoso")
    
    respuesta = requests.get(f"{BASE_URL}/posts/1")
    #(verificacion del QA)
    assert respuesta.status_code == 200, f"Error: se esperaba un código de estado 200, pero se obtuvo {respuesta.status_code}"
    datos = respuesta.json()
    #se asegura que el campo 'title' esté presente en la respuesta
    assert "title" in datos, "Error: la respuesta no contiene el campo 'title'"
    print("Test1 exitoso")


def test_obtener_post_no_existente():
    """ [Test2] prueba de obtener un post que no existe.
    verfica que la API devuelve un código de estado 404."""
    print("\n Iniciando prueba de obtener post no existente")
    
    respuesta = requests.get(f"{BASE_URL}/posts/9999")
    #(verificacion del QA)
    assert respuesta.status_code == 404, f"Error: se esperaba un código de estado 404, pero se obtuvo {respuesta.status_code}"
    print("Test2 exitoso")

#ejecucion de las pruebas
print("1. Iniciando pruebas de la API")
test_obtener_post_exitoso()
test_obtener_post_no_existente()
print("\n Todas las pruebas de la API se ejecutaron correctamente")

