# Script de Descarga de CEP (Comprobante Electrónico de Pago)

Este script automatiza la descarga de Comprobantes Electrónicos de Pago (CEP) del sistema SPEI de Banxico.

## Requisitos

- Python 3.x
- Biblioteca `requests`

Para instalar las dependencias:
```bash
pip install requests
```

## Funcionalidad

El script realiza las siguientes operaciones:

1. Simula el proceso de validación del formulario web de Banxico
2. Maneja la autenticación y cookies de sesión
3. Descarga el archivo CEP en formato ZIP (que contiene el PDF y XML)

## Configuración

Modifica las siguientes variables en la función `download_cep()`:

```python
data = {
    "fecha": "31-12-2024",           # Fecha del pago (dd-mm-yyyy)
    "criterio": "1234567",           # Número de referencia o clave de rastreo
    "monto": "2509.00",              # Monto de la operación
    "tipoCriterio": "R",             # R = Número de referencia, T = Clave de rastreo
    "emisor": "40099",               # Código del banco emisor
    "receptor": "40098",             # Código del banco receptor
    "cuenta": "1234567891234567",    # CLABE, tarjeta o celular del beneficiario
    "receptorParticipante": "0"      # 0 = Pago a cuenta, 1 = Pago a banco
}
```

## Uso

```bash
python script.py
```

El script generará un archivo `CEP_descargado.zip` que contiene el comprobante en formatos PDF y XML.

## Institución que recibe la transferencia electrónica

```
"40138" = ABC CAPITAL
"40133" = ACTINVER
"40062" = AFIRME
"90706" = ARCUS
"90659" = ASP INTEGRA OPC
"40128" = AUTOFIN
"40127" = AZTECA
"37166" = BaBien
"40030" = BAJIO
"40002" = BANAMEX
"40154" = BANCO COVALTO
"37006" = BANCOMEXT
"40137" = BANCOPPEL
"40160" = BANCO S3
"40152" = BANCREA
"37019" = BANJERCITO
"40147" = BANKAOOL
"40106" = BANK OF AMERICA
"40159" = BANK OF CHINA
"37009" = BANOBRAS
"40072" = BANORTE
"40058" = BANREGIO
"40060" = BANSI
"2001" = BANXICO
"40129" = BARCLAYS
"40145" = BBASE
"40012" = BBVA MEXICO
"40112" = BMONEX
"90677" = CAJA POP MEXICA
"90683" = CAJA TELEFONIST
"90630" = CB INTERCAM
"40124" = CBM BANCO
"40143" = CIBANCO
"90631" = CI BOLSA
"90901" = CLS
"90903" = CoDi Valida
"40130" = COMPARTAMOS
"40140" = CONSUBANCO
"90652" = CREDICAPITAL
"90688" = CREDICLUB
"90680" = CRISTOBAL COLON
"90723" = Cuenca
"40151" = DONDE
"90616" = FINAMEX
"90634" = FINCOMUN
"90689" = FOMPED
"90699" = FONDEADORA
"90685" = FONDO (FIRA)
"90601" = GBM
"37168" = HIPOTECARIA FED
"40021" = HSBC
"40155" = ICBC
"40036" = INBURSA
"90902" = INDEVAL
"40150" = INMOBILIARIO
"40136" = INTERCAM BANCO
"40059" = INVEX
"40110" = JP MORGAN
"90661" = KLAR
"90653" = KUSPIT
"90670" = LIBERTAD
"90602" = MASARI
"90722" = Mercado Pago W
"40042" = MIFEL
"40158" = MIZUHO BANK
"90600" = MONEXCB
"40108" = MUFG
"40132" = MULTIVA BANCO
"37135" = NAFIN
"90638" = NU MEXICO
"90710" = NVIO
"40148" = PAGATODO
"90620" = PROFUTURO
"40156" = SABADELL
"40014" = SANTANDER
"40044" = SCOTIABANK
"40157" = SHINHAN
"90728" = SPIN BY OXXO
"90646" = STP
"90703" = TESORED
"90684" = TRANSFER
"90656" = UNAGRA
"90617" = VALMEX
"90605" = VALUE
"90608" = VECTOR
"40113" = VE POR MAS
"40141" = VOLKSWAGEN
```

## Notas

- El horario de consulta es de 09:30-23:00 hrs de Lunes a Domingo
- Solo funciona para operaciones entre diferentes instituciones financieras
- Requiere datos exactos de la operación para obtener el comprobante