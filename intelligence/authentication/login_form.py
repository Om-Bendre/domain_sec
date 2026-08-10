from core.models.fact import Fact


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
    ) -> list[Fact]:

        facts = []

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

                if field_name in LOGIN_FIELD_NAMES:
                    username_field = field

                elif field_type == "email":
                    username_field = field

            if not (

                username_field

                and

                password_field

            ):

                continue

            facts.append(

                Fact(

                    category="Authentication",

                    name="login_form",

                    value=True,

                    description="Login form detected",

                )

            )

            facts.append(

                Fact(

                    category="Authentication",

                    name="form_method",

                    value=form["method"],

                )

            )

            facts.append(

                Fact(

                    category="Authentication",

                    name="form_action",

                    value=form["action"],

                )

            )

            facts.append(

                Fact(

                    category="Authentication",

                    name="username_field",

                    value=username_field["name"],

                )

            )

            facts.append(

                Fact(

                    category="Authentication",

                    name="password_field",

                    value=password_field["name"],

                )

            )

            return facts

        return facts