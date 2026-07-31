from core.models.finding import Finding


class PasswordAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Finding]:

        findings = []

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

                findings.append(

                    Finding(

                        category="Authentication",

                        entity="Password",

                        name="password_field",

                        value=True,

                        description="Password field detected",

                    )

                )

                findings.append(

                    Finding(

                        category="Authentication",

                        entity="Password",

                        name="autocomplete",

                        value=field.get(
                            "autocomplete",
                        ),

                    )

                )

                findings.append(

                    Finding(

                        category="Authentication",

                        entity="Password",

                        name="required",

                        value=field.get(
                            "required",
                        ),

                    )

                )

                attributes = field.get(
                    "attributes",
                    {},
                )

                if "minlength" in attributes:

                    findings.append(

                        Finding(

                            category="Authentication",

                            entity="Password",

                            name="minlength",

                            value=attributes[
                                "minlength"
                            ],

                        )

                    )

                if "maxlength" in attributes:

                    findings.append(

                        Finding(

                            category="Authentication",

                            entity="Password",

                            name="maxlength",

                            value=attributes[
                                "maxlength"
                            ],

                        )

                    )

        return findings