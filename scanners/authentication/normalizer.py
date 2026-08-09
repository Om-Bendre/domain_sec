from bs4 import BeautifulSoup


class AuthenticationNormalizer:
    """
    Converts raw HTTP data into a normalized structure.

    """

    def normalize(
        self,
        raw_data: dict,
    ) -> dict:

        html = raw_data.get("html", "")

        soup = BeautifulSoup(
            html,
            "lxml",
        )

        forms = []

        for form in soup.find_all("form"):

            forms.append(
                self._parse_form(form)
            )

        return {

            "page_url": raw_data.get("url"),

            "headers": raw_data.get(
                "headers",
                {},
            ),

            "cookies": raw_data.get(
                "cookie_headers",
                [],
            ),

            "forms": forms,

            "html": html,

        }

    def _parse_form(
        self,
        form,
    ) -> dict:

        return {

            "action": form.get(
                "action",
                "",
            ),

            "method": form.get(
                "method",
                "GET",
            ).upper(),

            "autocomplete": form.get(
                "autocomplete",
                "",
            ),

            "id": form.get(
                "id",
                "",
            ),

            "name": form.get(
                "name",
                "",
            ),

            "inputs": [

                self._parse_input(inp)

                for inp in form.find_all("input")

            ],

        }

    def _parse_input(
        self,
        inp,
    ) -> dict:

        return {

            "type": inp.get(
                "type",
                "text",
            ).lower(),

            "name": inp.get(
                "name",
                "",
            ),

            "id": inp.get(
                "id",
                "",
            ),

            "value": inp.get(
                "value",
                "",
            ),

            "placeholder": inp.get(
                "placeholder",
                "",
            ),

            "autocomplete": inp.get(
                "autocomplete",
                "",
            ),

            "required": inp.has_attr(
                "required",
            ),

             "minlength": inp.get(
            "minlength",
            ),

            "maxlength": inp.get(
                "maxlength",
            ),


        }