from core.models.fact import Fact


class ProviderAnalyzer:

    PROVIDERS = {

        "amazon": "AWS",

        "aws": "AWS",

        "google": "Google Cloud",

        "cloudflare": "Cloudflare",

        "azure": "Microsoft Azure",

        "digitalocean": "DigitalOcean",

        "linode": "Linode",

        "ovh": "OVH",

    }

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Fact]:

        network = normalized_data.get(
            "network",
            {},
        )

        searchable = str(network).lower()

        for keyword, provider in self.PROVIDERS.items():

            if keyword in searchable:

                return [

                    Fact(

                        category="Infrastructure",

                        entity="Cloud",

                        name="provider",

                        value=provider,

                    )

                ]

        return []