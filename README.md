# 🤖 WhatsApp Bot - Repartidor de TAREAS

Este bot envía automáticamente un mensaje a un grupo de WhatsApp con un número aleatorio diario (0-7) asignado a cada participante 😄.

## 🚀 Requisitos

- Python 3.8+
- Google Chrome instalado
- ChromeDriver compatible con tu versión de Chrome

## 📦 Instalación

1. Clona o descarga el proyecto

2. Instala dependencias:

 '' pip install -r requirements.txt ''


3. Descarga ChromeDriver:
https://chromedriver.chromium.org/

Y colócalo en el mismo directorio o en tu PATH.

---

## ⚙️ Configuración

Edita el archivo `config.py`:

- Nombre del grupo de WhatsApp
- Lista de participantes
- Rango de números

---

## ▶️ Uso

Ejecuta:

'' python bot.py ''


1. Se abrirá WhatsApp Web
2. Escanea el QR
3. Pulsa ENTER en la terminal
4. El bot enviará el mensaje automáticamente

---

## 🔁 Automatización diaria

Puedes programarlo con:

### Windows (Task Scheduler)
### Linux / Mac (cron)

Ejemplo cron (todos los días a las 10:00):

'' 0 10 * * * /usr/bin/python3 /ruta/bot.py ''


---

## ⚠️ Advertencias

- Este método usa automatización de navegador (no oficial)
- WhatsApp podría bloquear tu cuenta si abusas
- No enviar spam

---

## 😎 Mejoras posibles

- Añadir IA para respuestas automáticas
- Logs históricos
- Mensajes personalizados
- Base de datos

---

## 🧠 Disclaimer

Este bot es solo para fines educativos.
