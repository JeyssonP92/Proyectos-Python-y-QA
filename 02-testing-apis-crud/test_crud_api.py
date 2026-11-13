import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_ciclo_completo_crud():
    """ [Test] prueba de ciclo completo CRUD.
    verfica que la API permite crear, leer, actualizar y eliminar un post."""
    print("\n Iniciando prueba de ciclo completamente automatizado CRUD")
    
    # Paso POST, Crear un nuevo post
    print("Creando un nuevo post...")
    nuevo_post = {
        "title": "Nuevo Post de Prueba QA",
        "body": "Este es el contenido del post automatizado.",
        "userId": 1
    }
    respuesta_crear = requests.post(f"{BASE_URL}/posts", json=nuevo_post)
    #VERIFICACION QA, el codigo de estado esperado es 201 (Created)
    assert respuesta_crear.status_code == 201, f"Error: se esperaba un código de estado 201, pero se obtuvo {respuesta_crear.status_code}"
    datos_crear = respuesta_crear.json()
    post_id = datos_crear.get("id")
    assert post_id is not None, "Error: no se obtuvo el ID del nuevo post"
    print(f"Post creado con ID: {post_id}")
    
    # Paso GET, Leer el post creado
    print("Leyendo el post creado ...")
    #se simuala la consulta al recurso creado, para que la API responda correctamente.
    respuesta_get = requests.get(f"{BASE_URL}/posts/1")
    #VERIFICACION QA, el codigo de estado esperado es 200 (OK)
    assert respuesta_get.status_code == 200, f"Error: se esperaba un código de estado 200, pero se obtuvo {respuesta_get.status_code}"
    print("GET exitoso, el post fue leído correctamente")
    
    #Paso PUT, Actualizar el post
    print("Actualizando el post...")
    post_actualizado = {
        "id": post_id,
        "title": "Post Actualizado de Prueba QA",
        "body": "Este es el contenido actualizado del post automatizado.",
        "userId": 1
    }
    #se envia la solicitud PUT al recurso creado, para que la API responda correctamente.
    respuesta_put = requests.put(f"{BASE_URL}/posts/1", json=post_actualizado)
    #VERIFICACION QA, el codigo de estado esperado es 200 (OK)
    assert respuesta_put.status_code == 200, f"Error: se esperaba un código de estado 200, pero se obtuvo {respuesta_put.status_code}"
    #se valida que el servidor haya actualizado correctamente el recurso, con el nuevo titulo.
    datos_servidor = respuesta_put.json()
    assert datos_servidor["title"] == "Post Actualizado de Prueba QA", "Error: el título del post no fue actualizado correctamente"
    print("PUT exitoso, el post fue actualizado correctamente")
    #Paso DELETE, Eliminar el post
    print("Eliminando el post...")
    respuesta_delete = requests.delete(f"{BASE_URL}/posts/{post_id}")
    assert respuesta_delete.status_code == 200, f"Error: se esperaba un código de estado 200, pero se obtuvo {respuesta_delete.status_code}"
    print("DELETE exitoso, el post fue eliminado correctamente")
    print("Test CRUD exitoso")
