from core.models.fact import Fact


class BackendAnalyzer:

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

        if (
            "php" in server
            or "php" in powered_by
        ):
            detections.add("PHP")

        if powered_by == "express":
            detections.add("Node.js")

        if any(
            value in server
            for value in (
                "gunicorn",
                "uvicorn",
                "werkzeug",
            )
        ):
            detections.add("Python")

        if (
            "asp.net" in powered_by
            or "kestrel" in server
        ):
            detections.add(".NET")

        if any(
            value in server
            for value in (
                "tomcat",
                "jetty",
            )
        ):
            detections.add("Java")

        if server == "go":
            detections.add("Go")

        for backend in sorted(detections):

            facts.append(
                Fact(
                    category="Technology",
                    entity="Backend",
                    name="technology",
                    value=backend,
                )
            )

        return facts