from core.models.fact import Fact


CDNS = {

    "cloudflare": "Cloudflare",

    "cloudfront": "Amazon CloudFront",

    "fastly": "Fastly",

    "akamai": "Akamai",

    "cdn77": "CDN77",

    "jsdelivr": "jsDelivr",

    "unpkg": "UNPKG",

}


class CDNAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Fact]:

        facts = []

        headers = str(

            normalized_data.get(

                "headers",

                {},

            )

        ).lower()

        scripts = " ".join(

            normalized_data.get(

                "scripts",

                [],

            )

        ).lower()

        searchable = headers + scripts

        for key, provider in CDNS.items():

            if key in searchable:

                facts.append(

                    Fact(

                        category="Technology",

                        entity="CDN",

                        name="provider",

                        value=provider,

                    )

                )

        return facts