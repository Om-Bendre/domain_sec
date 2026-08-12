from core.models.fact import Fact


class CMSAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Fact]:

        facts = []

        html = normalized_data.get(
            "html",
            "",
        ).lower()

        generator = (
            normalized_data.get(
                "generator"
            ) or ""
        ).lower()

        detections = set()

        if (
            "wordpress" in generator
            or "/wp-content/" in html
            or "/wp-includes/" in html
        ):
            detections.add("WordPress")

        if (
            "drupal" in generator
            or "drupal-settings-json" in html
        ):
            detections.add("Drupal")

        if (
            "joomla" in generator
            or "/media/system/" in html
        ):
            detections.add("Joomla")

        if "ghost" in generator:
            detections.add("Ghost")

        if "strapi" in generator:
            detections.add("Strapi")

        for cms in sorted(detections):

            facts.append(
                Fact(
                    category="Technology",
                    entity="CMS",
                    name="cms",
                    value=cms,
                )
            )

        return facts