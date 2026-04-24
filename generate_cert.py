import os
import datetime
import ipaddress  # Importación necesaria para manejar la IP
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa

# Configuración de rutas
base_dir = os.path.dirname(os.path.abspath(__file__))
cert_path = os.path.join(base_dir, "sample_cert.pem")
key_path = os.path.join(base_dir, "private_key.pem")

def generate_full_cert():
    print("Generating 2048-bit RSA key...")
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )

    # Configurar Identidad
    subject = issuer = x509.Name([
        x509.NameAttribute(NameOID.COUNTRY_NAME, u"CL"),
        x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"Santiago"),
        x509.NameAttribute(NameOID.LOCALITY_NAME, u"Santiago"),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"Cyber Lab"),
        x509.NameAttribute(NameOID.COMMON_NAME, u"localhost"),
    ])

    # Construir el Certificado
    now = datetime.datetime.now(datetime.UTC)
    cert_builder = (
        x509.CertificateBuilder()
        .subject_name(subject)
        .issuer_name(issuer)
        .public_key(private_key.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(now)
        .not_valid_after(now + datetime.timedelta(days=365))
        .add_extension(
            x509.SubjectAlternativeName([
                x509.DNSName(u"localhost"),
                x509.IPAddress(ipaddress.ip_address("127.0.0.1")), # Corregido aquí
            ]),
            critical=False,
        )
        .add_extension(
            x509.BasicConstraints(ca=False, path_length=None),
            critical=True,
        )
    )

    certificate = cert_builder.sign(private_key, hashes.SHA256())

    # Guardar Archivos
    with open(cert_path, "wb") as f:
        f.write(certificate.public_bytes(serialization.Encoding.PEM))

    with open(key_path, "wb") as f:
        f.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption(),
        ))

    print(f"✅ Éxito: Archivos generados en:\n   {base_dir}")

if __name__ == "__main__":
    generate_full_cert()
