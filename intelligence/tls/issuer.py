from core.contracts.intelligence import BaseIntelligence


class IssuerAnalyzer(BaseIntelligence):

    TRUSTED = [

        "Google",

        "DigiCert",

        "Let's Encrypt",

        "GlobalSign",

        "Sectigo",

        "Cloudflare",

    ]

    def analyze(
        self,
        normalized,
    ):

        issuer = (

            normalized.get(

                "issuer_common_name"

            )

            or ""

        )

        trusted = any(

            ca.lower() in issuer.lower()

            for ca in self.TRUSTED

        )

        return {

            "trusted_ca": trusted,

        }