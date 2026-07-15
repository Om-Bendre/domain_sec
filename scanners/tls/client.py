import socket
import ssl


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

                return {

                    "tls_version": tls.version(),

                    "cipher": tls.cipher(),

                    "certificate": certificate,

                }