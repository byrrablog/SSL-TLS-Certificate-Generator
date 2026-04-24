🔐 generate_cert — Automated SSL/TLS Certificate Generator

generate_cert es una herramienta en Python orientada a automatizar la generación de certificados X.509 autofirmados junto con claves privadas RSA.
Está pensada para entornos de desarrollo, laboratorios de ciberseguridad y testing, donde se requiere levantar rápidamente servicios seguros sin depender de una CA externa.

✨ Value Proposition

Este proyecto demuestra:

Automatización de tareas de seguridad comunes en entornos DevSecOps
Implementación práctica de criptografía aplicada (PKI básica)
Buenas prácticas en generación de certificados modernos (SAN obligatorio)
Integración directa con herramientas reales del ecosistema
🚀 Features
🔑 RSA 2048-bit Key Generation
Generación de claves seguras con exponente público 65537 (estándar de la industria)
🔐 SHA-256 Certificate Signing
Firma criptográfica robusta para garantizar integridad
🌐 SAN Support (Subject Alternative Name)
Incluye automáticamente:
localhost
127.0.0.1
Compatible con navegadores modernos (Chrome, Edge, Firefox)
📦 PEM Output (Industry Standard)
Listo para usar en:
Nginx / Apache
Docker containers
Herramientas SIEM como Wazuh
Monitoreo con Zabbix
📁 Dynamic Path Handling
Guarda automáticamente los archivos en la ruta del proyecto
🧱 Tech Stack
Python 3.12+
Cryptography (hazmat layer)
Conceptos aplicados:
X.509 Certificates
Public Key Infrastructure (PKI)
RSA Encryption
Hashing (SHA-256)
⚙️ Installation
pip install cryptography
▶️ Usage
python generate_cert.py
📂 Output

El script genera automáticamente:

sample_cert.pem → Certificado público
private_key.pem → Clave privada

Ambos listos para integrarse en servidores o entornos locales.

🧪 Use Cases
🔧 Configuración rápida de HTTPS en entornos locales
🧑‍💻 Laboratorios de ciberseguridad / pentesting
🐳 Contenedores Docker con TLS
📡 Simulación de infraestructura segura
📚 Aprendizaje práctico de certificados digitales
⚠️ Security Notice

Este proyecto genera certificados autofirmados.
No es adecuado para producción donde se requiera confianza pública mediante una Autoridad Certificadora (CA).

📈 Possible Improvements
Soporte para certificados firmados por CA interna
CLI con argumentos personalizados (CN, expiración, SAN dinámico)
Exportación a formatos adicionales (DER, PFX)
Integración con pipelines CI/CD
Rotación automática de certificados

👤 Author
   Bayron Cares. 
