from core.models.finding import Finding


ANALYTICS = {

    "google-analytics": "Google Analytics",

    "gtag": "Google Analytics",

    "googletagmanager": "Google Tag Manager",

    "plausible": "Plausible",

    "matomo": "Matomo",

    "mixpanel": "Mixpanel",

    "segment": "Segment",

    "hotjar": "Hotjar",

    "clarity": "Microsoft Clarity",

}


class AnalyticsAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Finding]:

        findings = []

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

        searchable = html + scripts

        for key, provider in ANALYTICS.items():

            if key in searchable:

                findings.append(

                    Finding(

                        category="Technology",

                        entity="Analytics",

                        name="provider",

                        value=provider,

                    )

                )

        return findings