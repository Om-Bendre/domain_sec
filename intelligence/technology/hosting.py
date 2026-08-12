from core.models.fact import Fact


class HostingAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Fact]:

        facts = []

        headers = normalized_data.get(
            "headers",
            {},
        )

        server = headers.get(
            "server",
            "",
        ).lower()

        powered_by = headers.get(
            "x-powered-by",
            "",
        ).lower()

        detections = set()

        if "vercel" in server:
            detections.add("Vercel")

        if "netlify" in server:
            detections.add("Netlify")

        if "render" in server:
            detections.add("Render")

        if "railway" in server:
            detections.add("Railway")

        if "heroku" in server:
            detections.add("Heroku")

        if "fly.io" in server:
            detections.add("Fly.io")

        if "firebase" in server:
            detections.add("Firebase")

        if "github" in server:
            detections.add("GitHub Pages")

        if "azure" in server:
            detections.add("Azure")

        if "aws" in server:
            detections.add("AWS")

        for provider in sorted(detections):

            facts.append(
                Fact(
                    category="Technology",
                    entity="Hosting",
                    name="provider",
                    value=provider,
                )
            )

        return facts