class LoginFormAnalyzer:

    USERNAME_FIELDS = {

        "username",
        "user",
        "email",
        "login",

    }

    CSRF_FIELDS = {

        "csrf",
        "_csrf",
        "csrf_token",
        "_token",

    }

    def analyze(
        self,
        normalized_data: dict,
    ) -> dict:

        forms = normalized_data.get(
            "forms",
            [],
        )

        login_form = None

        for form in forms:

            has_password = False
            has_username = False

            for field in form["inputs"]:

                field_type = field.get(
                    "type",
                    "",
                ).lower()

                field_name = (
                    field.get(
                        "name",
                        "",
                    ).lower()
                )

                if field_type == "password":

                    has_password = True

                if field_name in self.USERNAME_FIELDS:

                    has_username = True

            if has_password and has_username:

                login_form = form

                break

        if login_form is None:

            return {

                "login_form_detected": False,

            }

        csrf = False

        username_autocomplete = None

        password_autocomplete = None

        for field in login_form["inputs"]:

            field_name = (
                field.get(
                    "name",
                    "",
                ).lower()
            )

            field_type = (
                field.get(
                    "type",
                    "",
                ).lower()
            )

            if field_name in self.CSRF_FIELDS:

                csrf = True

            if field_name in self.USERNAME_FIELDS:

                username_autocomplete = field.get(
                    "autocomplete"
                )

            if field_type == "password":

                password_autocomplete = field.get(
                    "autocomplete"
                )

        return {

            "login_form_detected": True,

            "method": login_form.get(
                "method"
            ),

            "action": login_form.get(
                "action"
            ),

            "csrf_token": csrf,

            "username_autocomplete":
                username_autocomplete,

            "password_autocomplete":
                password_autocomplete,

        }