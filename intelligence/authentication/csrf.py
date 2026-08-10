from core.models.fact import Fact


COMMON_CSRF_NAMES = {

    "csrf",

    "_csrf",

    "csrftoken",

    "csrfmiddlewaretoken",

    "authenticity_token",

    "__requestverificationtoken",

    "_token",

}


class CSRFAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Fact]:

        facts = []

        forms = normalized_data.get(
            "forms",
            [],
        )

        for form in forms:

            for field in form["inputs"]:

                if field["type"] != "hidden":

                    continue

                field_name = field["name"].lower()

                if field_name in COMMON_CSRF_NAMES:

                    facts.append(

                        Fact(

                            category="Authentication",

                            entity="CSRF",

                            name="csrf_token",

                            value=field_name,

                            description="Hidden CSRF token detected",

                        )

                    )

        return facts