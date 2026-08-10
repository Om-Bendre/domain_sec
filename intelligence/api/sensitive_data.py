import re

from core.models.fact import Fact


PATTERNS = {

    "Bearer Token":

        r"Bearer\s+[A-Za-z0-9\-._~+/]+=*",

    "API Key":

        r"api[_-]?key",

    "Secret":

        r"secret",

    "Password":

        r"password",

    "Access Token":

        r"access[_-]?token",

    "Refresh Token":

        r"refresh[_-]?token",

    "Internal ID":

        r"internal[_-]?id",

}


class SensitiveDataAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Fact]:

        facts = []

        body = normalized_data.get(
            "body",
            "",
        )

        for name, pattern in PATTERNS.items():

            if re.search(

                pattern,

                body,

                re.IGNORECASE,

            ):

                facts.append(

                    Fact(

                        category="API Security",

                        entity="Sensitive Data",

                        name="indicator",

                        value=name,

                    )

                )

        return facts