from core.contracts.intelligence import BaseIntelligence

class ProviderDetector(BaseIntelligence):

    PROVIDERS = {

        "15169": {
            "provider": "Google LLC",
            "infrastructure": "Cloud Provider",
            "hosting": "Google Cloud",
        },

        "16509": {
            "provider": "Amazon",
            "infrastructure": "Cloud Provider",
            "hosting": "AWS",
        },

        "8075": {
            "provider": "Microsoft",
            "infrastructure": "Cloud Provider",
            "hosting": "Azure",
        },

        "13335": {
            "provider": "Cloudflare",
            "infrastructure": "CDN / Security",
            "hosting": "Cloudflare",
        },

        "20940": {
            "provider": "Akamai",
            "infrastructure": "CDN",
            "hosting": "Akamai",
        },

        "14061": {
            "provider": "DigitalOcean",
            "infrastructure": "Cloud Provider",
            "hosting": "DigitalOcean",
        },

        "24940": {
            "provider": "Hetzner",
            "infrastructure": "Cloud Provider",
            "hosting": "Hetzner",
        },

        "16276": {
            "provider": "OVHcloud",
            "infrastructure": "Cloud Provider",
            "hosting": "OVHcloud",
        },

        "31898": {
            "provider": "Oracle",
            "infrastructure": "Cloud Provider",
            "hosting": "Oracle Cloud",
        },

        "63949": {
            "provider": "Linode",
            "infrastructure": "Cloud Provider",
            "hosting": "Linode",
        },

    }

    def analyze(
        self,
        normalized,
    ):

        asn = str(
            normalized.get("asn")
        )

        if asn in self.PROVIDERS:

            provider = self.PROVIDERS[asn]

            return {

                "provider": provider["provider"],

                "hosting_provider": provider["hosting"],

                "infrastructure_type": provider["infrastructure"],

                "confidence": "High",

            }

        return {

            "provider": "Unknown",

            "hosting_provider": "Unknown",

            "infrastructure_type": "Unknown",

            "confidence": "Low",

        }