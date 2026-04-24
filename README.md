# SSL-TLS-Certificate-Generator
Este proyecto es una herramienta de automatización para generar certificados **X.509 autofirmados** y claves privadas RSA de 2048 bits. Está diseñado para laboratorios de pruebas, entornos de desarrollo local y prácticas de criptografía aplicada.

## Características Técnicas
* **Algoritmo:** RSA con exponente público 65537.
* **Seguridad:** Firma mediante SHA-256.
* **Compatibilidad:** Incluye extensiones **SAN (Subject Alternative Name)** para soporte en navegadores modernos (localhost/127.0.0.1).
* **Portabilidad:** Genera archivos en formato PEM compatibles con Nginx, Apache y herramientas de monitoreo.

## Uso
1. Instalar dependencias:
   pip install cryptography
2. Ejecutar el script:
   python generate_cert.py
