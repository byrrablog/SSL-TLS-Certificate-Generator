# 🛡️ generate_cert: SSL/TLS Certificate Automator

`generate_cert` es un script de Python diseñado para la generación automatizada de certificados **X.509 autofirmados** y claves privadas RSA. Es una herramienta ideal para asegurar entornos de prueba, laboratorios locales y flujos de trabajo de desarrollo de manera rápida y sencilla.

## 🚀 Características

* **Criptografía Robusta:** Genera claves RSA de **2048 bits** con exponente público 65537.
* **Seguridad de Firma:** Utiliza el algoritmo **SHA-256** para garantizar la integridad del certificado.
* **Soporte SAN (Subject Alternative Name):** Configurado automáticamente para `localhost` y `127.0.0.1`, eliminando las alertas de seguridad en navegadores modernos como Chrome, Edge y Firefox.
* **Portabilidad:** Exporta archivos en formato **PEM**, el estándar de la industria compatible con Nginx, Apache, Docker y herramientas de seguridad como Wazuh o Zabbix.
* **Gestión de Rutas:** El script detecta dinámicamente su propia ubicación para guardar los archivos generados directamente en la carpeta del proyecto.

## 🛠️ Requisitos

* **Python 3.12+**
* **Librería Cryptography:** Es la única dependencia externa necesaria.

## 📦 Instalación y Uso

1. **Instalar dependencias:**
   Asegúrate de tener instalada la librería necesaria ejecutando:
   ```bash
   pip install cryptography
Ejecutar el script:
Lanza el generador desde tu terminal:

Bash
python generate_cert.py
📂 Archivos Generados
Al finalizar la ejecución, el script creará automáticamente en la misma carpeta:

sample_cert.pem: Tu certificado público listo para ser cargado en tus servicios.

private_key.pem: La clave privada RSA vinculada al certificado.

⚠️ Advertencia de Seguridad
Entornos de Desarrollo: Este script genera certificados autofirmados. No deben utilizarse en entornos de producción críticos donde se requiera la validación de una Entidad Certificadora (CA) pública.

👤 Author
Bayron Cares -
