from core.models.finding import Finding


LOGIN_FIELD_NAMES = {

    "username",
    "user",
    "userid",
    "email",
    "login",
    "identifier",

}


class LoginFormAnalyzer:

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

            username_field = None
            password_field = None

            for field in form["inputs"]:

                field_type = field.get(
                    "type",
                    "",
                )

                field_name = field.get(
                    "name",
                    "",
                ).lower()

                if field_type == "password":

                    password_field = field

                if (

                    field_type in {

                        "text",

                        "email",

                    }

                    or

                    field_name in LOGIN_FIELD_NAMES

                ):

                    username_field = field

            if not (

                username_field

                and

                password_field

            ):

                continue

            findings.append(

                Finding(

                    category="Authentication",

                    name="login_form",

                    value=True,

                    description="Login form detected",

                )

            )

            findings.append(

                Finding(

                    category="Authentication",

                    name="form_method",

                    value=form["method"],

                )

            )

            findings.append(

                Finding(

                    category="Authentication",

                    name="form_action",

                    value=form["action"],

                )

            )

            findings.append(

                Finding(

                    category="Authentication",

                    name="username_field",

                    value=username_field["name"],

                )

            )

            findings.append(

                Finding(

                    category="Authentication",

                    name="password_field",

                    value=password_field["name"],

                )

            )

            return findings

        return findings