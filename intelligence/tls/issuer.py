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

        organization = (
            normalized.get(
                "issuer_organization"
            )
            or ""
        )

        trusted = any(

            ca.lower() in organization.lower()

            for ca in self.TRUSTED

        )

        return {

            "trusted_ca": trusted,

        }