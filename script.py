import requests
from datetime import datetime
import time

def get_captcha():
    captcha_url = "https://www.banxico.org.mx/cep/stickyImg"
    return requests.get(captcha_url, params={'b_capt': int(time.time() * 1000)})

def download_cep():
    # Paso 1: Validar acceso a la descarga
    validate_url = "https://www.banxico.org.mx/cep/valida.do"
    captcha_response = get_captcha()
    
    data = {
        "fecha": "31-12-2024",
        "criterio": "1234567",
        "monto": "999.00",
        "tipoCriterio": "R",
        "emisor": "40099",
        "receptor": "40100",
        "cuenta": "1234567891234567",
        "receptorParticipante": "0",
        "captcha": captcha_response.cookies.get('JSESSIONID', 'c'),
        "tipoConsulta": "1"
    }
    
    session = requests.Session()
    response = session.post(validate_url, data=data, cookies=captcha_response.cookies)
    
    # Paso 2: Descargar el .ZIP
    if response.status_code == 200 and "boton-descarga-zip" in response.text:
        zip_url = "https://www.banxico.org.mx/cep/descarga.do?formato=ZIP"
        zip_response = session.get(zip_url)
        
        if zip_response.status_code == 200:
            # filename = f'CEP_{datetime.now().strftime("%Y%m%d_%H%M%S")}.zip'
            filename = "CEP_descargado.zip"
            with open(filename, 'wb') as f:
                f.write(zip_response.content)
            print(f"CEP descargado exitosamente como: {filename}")
        else:
            print("Error descargando el archivo ZIP:", zip_response.status_code)
    else:
        print("Error en la validación inicial.")
        # print("Error en la validación inicial:", response.text)

if __name__ == "__main__":
    download_cep()