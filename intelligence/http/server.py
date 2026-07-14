from core.contracts.intelligence import BaseIntelligence


class ServerAnalyzer(BaseIntelligence):

    KNOWN_SERVERS = {

        "nginx": "NGINX",

        "apache": "Apache",

        "iis": "Microsoft IIS",

        "caddy": "Caddy",

        "gws": "Google Web Server",

        "cloudflare": "Cloudflare",

    }

    def analyze(
        self,
        normalized,
    ):

        server = (
            normalized.get("server")
            or ""
        ).lower()

        detected = "Unknown"

        for key, value in self.KNOWN_SERVERS.items():

            if key in server:

                detected = value

                break

        return {

            "server_software": detected,

        }