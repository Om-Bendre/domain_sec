from core.models.finding import Finding


HOSTING = {

    "vercel": "Vercel",

    "netlify": "Netlify",

    "render": "Render",

    "railway": "Railway",

    "heroku": "Heroku",

    "fly.io": "Fly.io",

    "firebase": "Firebase",

    "github pages": "GitHub Pages",

    "azure": "Azure",

    "aws": "AWS",

}


class HostingAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Finding]:

        findings = []

        headers = str(

            normalized_data.get(

                "headers",

                {},

            )

        ).lower()

        html = normalized_data.get(

            "html",

            "",

        ).lower()

        searchable = headers + html

        for key, provider in HOSTING.items():

            if key in searchable:

                findings.append(

                    Finding(

                        category="Technology",

                        entity="Hosting",

                        name="provider",

                        value=provider,

                    )

                )

        return findings