# 🛡️ generate_cert: SSL/TLS Certificate Automator

`generate_cert` es un script de Python diseñado para la generación automatizada de certificados **X.509 autofirmados** y claves privadas RSA. Es una herramienta ideal para asegurar entornos de prueba, laboratorios locales y flujos de trabajo de desarrollo de manera rápida.

## 🚀 Características

* **Criptografía Robusta:** Genera claves RSA de **2048 bits** con exponente público 65537.
* **Seguridad de Firma:** Utiliza el algoritmo **SHA-256** para la integridad del certificado.
* **Soporte SAN (Subject Alternative Name):** Configurado para `localhost` y `127.0.0.1`, eliminando alertas de seguridad en navegadores modernos.
* **Portabilidad:** Exporta archivos en formato **PEM**, estándar de la industria compatible con Nginx, Apache, Docker y herramientas de seguridad.
* **Gestión de Rutas:** El script detecta su propia ubicación para guardar los resultados en la carpeta del proyecto.

## 🛠️ Requisitos

* Python 3.12+
* Librería `cryptography`

## 📦 Instalación y Uso

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/TU_USUARIO/NOMBRE_DEL_REPO.git](https://github.com/TU_USUARIO/NOMBRE_DEL_REPO.git)
   cd NOMBRE_DEL_REPO
Ejecutar el script:
Lanza el generador desde tu terminal:

   Bash
  `python generate_cert.py`

📂 Archivos Generados
Al finalizar la ejecución, el script creará automáticamente en la misma carpeta:

`sample_cert.pem: Tu certificado público listo para ser cargado en tus servicios.
private_key.pem: La clave privada RSA vinculada al certificado.`

⚠️ Advertencia de Seguridad
Entornos de Desarrollo: Este script genera certificados autofirmados. No deben utilizarse en entornos de producción críticos donde se requiera la validación de una Entidad Certificadora (CA) pública.

👤 Author
Bayron Cares
