from core.models.fact import Fact


class CDNAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Fact]:

        facts = []

        headers = normalized_data.get(
            "headers",
            {},
        )

        scripts = " ".join(
            normalized_data.get(
                "scripts",
                [],
            )
        ).lower()

        server = headers.get(
            "server",
            "",
        ).lower()

        via = headers.get(
            "via",
            "",
        ).lower()

        detections = set()

        if (
            "cloudflare" in server
            or headers.get("cf-ray")
        ):
            detections.add("Cloudflare")

        if "cloudfront" in via:
            detections.add(
                "Amazon CloudFront"
            )

        if "fastly" in via:
            detections.add("Fastly")

        if "akamai" in via:
            detections.add("Akamai")

        if "cdn77.com" in scripts:
            detections.add("CDN77")

        if "cdn.jsdelivr.net" in scripts:
            detections.add("jsDelivr")

        if "unpkg.com" in scripts:
            detections.add("UNPKG")

        for provider in sorted(detections):

            facts.append(
                Fact(
                    category="Technology",
                    entity="CDN",
                    name="provider",
                    value=provider,
                )
            )

        return facts