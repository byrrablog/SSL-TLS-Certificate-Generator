# 🛡️ PyCert-Gen: SSL/TLS Certificate Automator

PyCert-Gen es un script robusto de Python diseñado para la generación automatizada de certificados **X.509 autofirmados** y claves privadas RSA. Es una herramienta ideal para desarrolladores, expertos en ciberseguridad y administradores de sistemas que necesitan asegurar entornos de prueba o laboratorios locales de manera rápida y segura.

## 🚀 Características

* **Criptografía Robusta:** Genera claves RSA de **2048 bits** con exponente público 65537.
* **Seguridad:** Firmado digitalmente mediante el algoritmo **SHA-256**.
* **Soporte SAN (Subject Alternative Name):** Incluye extensiones para `localhost` y `127.0.0.1`, evitando alertas de seguridad en navegadores modernos (Chrome, Edge, Firefox).
* **Estandarización:** Exporta archivos en formato **PEM**, compatibles con Nginx, Apache, Docker y herramientas de monitoreo como Zabbix o Wazuh.
* **Gestión Dinámica:** Detecta automáticamente el directorio del script para organizar los archivos generados.

## 🛠️ Requisitos

* Python 3.12+
* Librería `cryptography`

## 📦 Instalación y Uso

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/TU_USUARIO/NOMBRE_DEL_REPO.git](https://github.com/TU_USUARIO/NOMBRE_DEL_REPO.git)
   cd NOMBRE_DEL_REPO
