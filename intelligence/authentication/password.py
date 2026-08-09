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

                if field.get("minlength") is not None:

                    findings.append(

                        Finding(

                            category="Authentication",

                            entity="Password",

                            name="minlength",

                            value=field["minlength"],
                        )

                    )

                if field.get("maxlength") is not None:

                    findings.append(

                        Finding(

                            category="Authentication",

                            entity="Password",

                            name="maxlength",

                            value=field["maxlength"],

                        )
                    )
                    
        return findings
    