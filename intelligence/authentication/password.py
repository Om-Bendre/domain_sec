class PasswordAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> dict:

        forms = normalized_data.get(
            "forms",
            [],
        )

        password_field = None

        for form in forms:

            for field in form["inputs"]:

                if field.get(
                    "type",
                    "",
                ).lower() == "password":

                    password_field = field

                    break

            if password_field:

                break

        if password_field is None:

            return {

                "password_field_detected": False,

            }

        return {

            "password_field_detected": True,

            "autocomplete":
                password_field.get(
                    "autocomplete"
                ),

            "required":
                password_field.get(
                    "required"
                ),

            "minlength":
                password_field.get(
                    "attributes",
                    {},
                ).get(
                    "minlength"
                ),

            "maxlength":
                password_field.get(
                    "attributes",
                    {},
                ).get(
                    "maxlength"
                ),

            "placeholder":
                password_field.get(
                    "placeholder"
                ),

        }