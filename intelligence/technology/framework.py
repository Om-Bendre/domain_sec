from core.models.finding import Finding


FRAMEWORKS = {

    "django": "Django",

    "flask": "Flask",

    "express": "Express",

    "laravel": "Laravel",

    "spring": "Spring",

    "fastapi": "FastAPI",

    "rails": "Ruby on Rails",

    "asp.net": "ASP.NET",

    "next": "Next.js",

    "nuxt": "Nuxt",

}


class FrameworkAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Finding]:

        findings = []

        html = normalized_data.get(

            "html",

            "",

        ).lower()

        headers = str(

            normalized_data.get(

                "headers",

                {},

            )

        ).lower()

        meta = str(

            normalized_data.get(

                "meta",

                {},

            )

        ).lower()

        searchable = html + headers + meta

        for key, value in FRAMEWORKS.items():

            if key in searchable:

                findings.append(

                    Finding(

                        category="Technology",

                        entity="Framework",

                        name="framework",

                        value=value,

                    )

                )

        return findings