import socket
import ssl

from cryptography import x509
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import (
    ec,
    ed25519,
    ed448,
    rsa,
)


class TLSClient:

    def query(
        self,
        target: str,
    ):

        context = ssl.create_default_context()

        with socket.create_connection(
            (target, 443),
            timeout=10,
        ) as sock:

            with context.wrap_socket(
                sock,
                server_hostname=target,
            ) as tls:

                certificate = tls.getpeercert()

                der_certificate = tls.getpeercert(
                    binary_form=True
                )

                parsed_certificate = (
                    x509.load_der_x509_certificate(
                        der_certificate
                    )
                )

                public_key = parsed_certificate.public_key()

                public_key_algorithm = "Unknown"
                public_key_size = None

                if isinstance(
                    public_key,
                    rsa.RSAPublicKey,
                ):
                    public_key_algorithm = "RSA"
                    public_key_size = public_key.key_size

                elif isinstance(
                    public_key,
                    ec.EllipticCurvePublicKey,
                ):
                    public_key_algorithm = "ECDSA"
                    public_key_size = public_key.key_size

                elif isinstance(
                    public_key,
                    ed25519.Ed25519PublicKey,
                ):
                    public_key_algorithm = "Ed25519"

                elif isinstance(
                    public_key,
                    ed448.Ed448PublicKey,
                ):
                    public_key_algorithm = "Ed448"

                signature_algorithm = (
                    parsed_certificate.signature_hash_algorithm.name
                    if parsed_certificate.signature_hash_algorithm
                    else "Unknown"
                )

                fingerprint = (
                    parsed_certificate
                    .fingerprint(hashes.SHA256())
                    .hex()
                    .upper()
                )

                return {

                    "tls_version": tls.version(),

                    "cipher": tls.cipher(),

                    "certificate": certificate,

                    "public_key_algorithm": public_key_algorithm,

                    "public_key_size": public_key_size,

                    "signature_algorithm": signature_algorithm,

                    "certificate_fingerprint": fingerprint,

                }