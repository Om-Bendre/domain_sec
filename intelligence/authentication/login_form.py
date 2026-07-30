LOGIN_FIELD_NAMES = {

    "username",
    "user",
    "email",
    "login",
    "identifier",
    "userid",

}

PASSWORD_FIELD_NAMES = {

    "password",
    "passwd",
    "pass",

}


class LoginFormAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> dict:

        forms = normalized_data.get(
            "forms",
            [],
        )

        for form in forms:

            username = None
            password = None

            for field in form["inputs"]:

                field_type = field["type"]
                field_name = field["name"].lower()

                #
                # Password field
                #

                if field_type == "password":

                    password = field

                #
                # Username / Email field
                #

                if (
                    field_type in (
                        "text",
                        "email",
                    )
                    or field_name in LOGIN_FIELD_NAMES
                ):

                    username = field

            if username and password:

                return {

                    "login_form_detected": True,

                    "username_field": username,

                    "password_field": password,

                    "method": form["method"],

                    "action": form["action"],

                }

        return {

            "login_form_detected": False,

            "username_field": None,

            "password_field": None,

            "method": None,

            "action": None,

        }