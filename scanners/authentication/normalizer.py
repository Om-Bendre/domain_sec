from bs4 import BeautifulSoup

from scanners.cookies.normalizer import CookieNormalizer


class AuthenticationNormalizer:

    def __init__(self):

        self.cookie_normalizer = CookieNormalizer()

    def normalize(
        self,
        raw_data: dict,
    ) -> dict:

        html = raw_data.get(
            "html",
            ""
        )

        soup = BeautifulSoup(
            html,
            "lxml",
        )

        forms = []

        for form in soup.find_all("form"):

            forms.append(

                self._parse_form(
                    form,
                )

            )

        return {

            "forms": forms,

            "cookies": self.cookie_normalizer.normalize(
                raw_data
            ),

            "headers": raw_data.get(
                "headers",
                {}
            ),

            "page_url": raw_data.get(
                "url"
            ),

            "html": html,

        }

    def _parse_form(
        self,
        form,
    ) -> dict:

        inputs = []

        for field in form.find_all("input"):

            inputs.append(

                self._parse_input(
                    field,
                )

            )

        return {

            "method": (
                form.get(
                    "method",
                    "GET",
                ).upper()
            ),

            "action": form.get(
                "action"
            ),

            "id": form.get(
                "id"
            ),

            "name": form.get(
                "name"
            ),

            "inputs": inputs,

        }

    def _parse_input(
        self,
        field,
    ) -> dict:

        return {

            "type": field.get(
                "type",
                "text",
            ),

            "name": field.get(
                "name"
            ),

            "id": field.get(
                "id"
            ),

            "value": field.get(
                "value"
            ),

            "placeholder": field.get(
                "placeholder"
            ),

            "autocomplete": field.get(
                "autocomplete"
            ),

            "required": field.has_attr(
                "required"
            ),

            "attributes": dict(
                field.attrs
            ),

        }