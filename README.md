# 🔐 generate_cert — Automated SSL/TLS Certificate Generator

**generate_cert** es una herramienta en Python orientada a automatizar la generación de certificados X.509 autofirmados junto con claves privadas RSA.  
Está pensada para **entornos de desarrollo, laboratorios de ciberseguridad y testing**, donde se requiere levantar rápidamente servicios seguros sin depender de una CA externa.

---

## ✨ Value Proposition

Este proyecto demuestra:

- Automatización de tareas de seguridad en entornos DevSecOps  
- Implementación práctica de criptografía aplicada (PKI básica)  
- Buenas prácticas modernas (uso de SAN obligatorio)  
- Integración con herramientas reales  

---

## 🚀 Features

- 🔑 **RSA 2048-bit Key Generation**
- 🔐 **SHA-256 Certificate Signing**
- 🌐 **SAN Support (`localhost`, `127.0.0.1`)**
- 📦 **PEM Output compatible con Nginx, Apache, Docker, Wazuh, Zabbix**
- 📁 **Dynamic Path Handling**

---

## 🧱 Tech Stack

- `Python 3.12+`
- `cryptography`
- X.509 / PKI / RSA / SHA-256

---

## ⚙️ Installation

``bash
pip install cryptography ``

## 📂 Output

El script genera automáticamente:

- `sample_cert.pem → Certificado público`
- `private_key.pem → Clave privada`

Ambos listos para integrarse en servidores o entornos locales.

- 🧪 Use Cases
- 🔧 Configuración rápida de HTTPS en entornos locales
- 🧑‍💻 Laboratorios de ciberseguridad / pentesting
- 🐳 Contenedores Docker con TLS
- 📡 Simulación de infraestructura segura
- 📚 Aprendizaje práctico de certificados digitales

## ⚠️ Security Notice

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
