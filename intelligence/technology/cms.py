from core.models.finding import Finding


CMS = {

    "wordpress": "WordPress",

    "drupal": "Drupal",

    "joomla": "Joomla",

    "ghost": "Ghost",

    "strapi": "Strapi",

}


class CMSAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Finding]:

        findings = []

        html = normalized_data.get(

            "html",

            "",

        ).lower()

        meta = str(

            normalized_data.get(

                "meta",

                {},

            )

        ).lower()

        searchable = html + meta

        for key, value in CMS.items():

            if key in searchable:

                findings.append(

                    Finding(

                        category="Technology",

                        entity="CMS",

                        name="cms",

                        value=value,

                    )

                )

        return findings