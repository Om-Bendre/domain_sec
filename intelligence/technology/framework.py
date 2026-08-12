from core.models.fact import Fact


class FrameworkAnalyzer:

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

        headers = normalized_data.get(
            "headers",
            {},
        )

        detections = set()

        # Next.js
        if (
            "__next_data__" in html
            or "/_next/" in html
            or "/_next/" in scripts
            or "next.js" in headers.get(
                "x-powered-by",
                "",
            ).lower()
        ):
            detections.add("Next.js")

        # Nuxt
        if (
            "__nuxt__" in html
            or "/_nuxt/" in html
            or "nuxt" in scripts
        ):
            detections.add("Nuxt")

        # Django
        if (
            "csrftoken" in str(
                normalized_data.get(
                    "cookies",
                    [],
                )
            ).lower()
            or "django" in headers.get(
                "server",
                "",
            ).lower()
        ):
            detections.add("Django")

        # Flask
        if "werkzeug" in headers.get(
            "server",
            "",
        ).lower():
            detections.add("Flask")

        # Express
        if headers.get(
            "x-powered-by",
            "",
        ).lower() == "express":
            detections.add("Express")

        # Laravel
        if (
            "laravel_session" in str(
                normalized_data.get(
                    "cookies",
                    [],
                )
            ).lower()
            or "laravel" in headers.get(
                "x-powered-by",
                "",
            ).lower()
        ):
            detections.add("Laravel")

        # ASP.NET
        if (
            "asp.net" in headers.get(
                "x-powered-by",
                "",
            ).lower()
            or "asp.net_sessionid" in str(
                normalized_data.get(
                    "cookies",
                    [],
                )
            ).lower()
        ):
            detections.add("ASP.NET")

        # Spring
        if headers.get(
            "x-application-context",
        ):
            detections.add("Spring")

        # FastAPI
        if headers.get(
            "server",
            "",
        ).lower() == "uvicorn":
            detections.add("FastAPI")

        # Ruby on Rails
        if "rails" in headers.get(
            "x-powered-by",
            "",
        ).lower():
            detections.add("Ruby on Rails")

        for framework in sorted(detections):

            facts.append(
                Fact(
                    category="Technology",
                    entity="Framework",
                    name="framework",
                    value=framework,
                )
            )

        return facts