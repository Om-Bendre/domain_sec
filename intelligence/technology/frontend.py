from core.models.fact import Fact


class FrontendAnalyzer:

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

        stylesheets = " ".join(
            normalized_data.get(
                "stylesheets",
                [],
            )
        ).lower()

        detections = set()

        if "bootstrap" in stylesheets:
            detections.add("Bootstrap")

        if "tailwind" in stylesheets:
            detections.add("Tailwind CSS")

        if "bulma" in stylesheets:
            detections.add("Bulma")

        if "foundation" in stylesheets:
            detections.add("Foundation")

        if (
            "material-ui" in scripts
            or "@mui/" in scripts
            or "mui" in stylesheets
        ):
            detections.add("Material UI")

        if "semantic-ui" in stylesheets:
            detections.add("Semantic UI")

        for library in sorted(detections):

            facts.append(
                Fact(
                    category="Technology",
                    entity="Frontend",
                    name="library",
                    value=library,
                )
            )

        return facts