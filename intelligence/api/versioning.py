import re

from core.models.finding import Finding


class VersioningAnalyzer:

    URL_VERSION = re.compile(

        r"/v(\d+)",

        re.IGNORECASE,

    )

    MEDIA_VERSION = re.compile(

        r"vnd\.[\w.-]+\.v(\d+)\+",

        re.IGNORECASE,

    )

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Finding]:

        findings = []

        url = normalized_data.get(
            "url",
            "",
        )

        headers = normalized_data.get(
            "headers",
            {},
        )

        #
        # URL Version
        #

        match = self.URL_VERSION.search(
            url,
        )

        if match:

            findings.append(

                Finding(

                    category="API Security",

                    entity="Versioning",

                    name="url_version",

                    value=f"v{match.group(1)}",

                )

            )

        #
        # Header Version
        #

        for header in (

            "API-Version",

            "X-API-Version",

            "Version",

        ):

            value = headers.get(
                header,
            )

            if value:

                findings.append(

                    Finding(

                        category="API Security",

                        entity="Versioning",

                        name="header_version",

                        value=value,

                    )

                )

        #
        # Media Type Version
        #

        content_type = normalized_data.get(
            "api",
            {},
        ).get(
            "content_type",
            "",
        )

        match = self.MEDIA_VERSION.search(
            content_type,
        )

        if match:

            findings.append(

                Finding(

                    category="API Security",

                    entity="Versioning",

                    name="media_type_version",

                    value=f"v{match.group(1)}",

                )

            )

        return findings