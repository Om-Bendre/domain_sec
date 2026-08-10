from core.models.fact import Fact


class PasswordAnalyzer:

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

                if field.get(
                    "type",
                    "",
                ) != "password":

                    continue

                facts.append(

                    Fact(

                        category="Authentication",

                        entity="Password",

                        name="password_field",

                        value=True,

                        description="Password field detected",

                    )

                )

                facts.append(

                    Fact(

                        category="Authentication",

                        entity="Password",

                        name="autocomplete",

                        value=field.get(
                            "autocomplete",
                        ),

                    )

                )

                facts.append(

                    Fact(

                        category="Authentication",

                        entity="Password",

                        name="required",

                        value=field.get(
                            "required",
                        ),

                    )

                )

                if field.get("minlength") is not None:

                    facts.append(

                        Fact(

                            category="Authentication",

                            entity="Password",

                            name="minlength",

                            value=field["minlength"],
                        )

                    )

                if field.get("maxlength") is not None:

                    facts.append(

                        Fact(

                            category="Authentication",

                            entity="Password",

                            name="maxlength",

                            value=field["maxlength"],

                        )
                    )

        return facts
    