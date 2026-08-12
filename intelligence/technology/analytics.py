from core.models.fact import Fact


class AnalyticsAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Fact]:

        facts = []

        html = normalized_data.get(
            "html",
            "",
        ).lower()

        scripts = " ".join(
            normalized_data.get(
                "scripts",
                [],
            )
        ).lower()

        inline_scripts = " ".join(
            normalized_data.get(
                "inline_scripts",
                [],
            )
        ).lower()

        searchable = (
            html
            + scripts
            + inline_scripts
        )

        detections = set()

        if (
            "google-analytics.com" in searchable
            or "googletagmanager.com" in searchable
            or "gtag(" in searchable
        ):
            detections.add(
                "Google Analytics"
            )

        if "googletagmanager.com" in searchable:
            detections.add(
                "Google Tag Manager"
            )

        if "plausible.io" in searchable:
            detections.add("Plausible")

        if "matomo" in searchable:
            detections.add("Matomo")

        if "mixpanel" in searchable:
            detections.add("Mixpanel")

        if "segment.com" in searchable:
            detections.add("Segment")

        if "hotjar" in searchable:
            detections.add("Hotjar")

        if "clarity.ms" in searchable:
            detections.add(
                "Microsoft Clarity"
            )

        for provider in sorted(detections):

            facts.append(
                Fact(
                    category="Technology",
                    entity="Analytics",
                    name="provider",
                    value=provider,
                )
            )

        return facts