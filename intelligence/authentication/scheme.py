from core.models.fact import Fact


class AuthenticationSchemeAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Fact]:

        facts = []

        authentication = normalized_data.get(
            "authentication",
            {},
        )

        headers = normalized_data.get(
            "headers",
            {},
        )

        #
        # WWW-Authenticate
        #

        challenge = authentication.get(
            "www_authenticate"
        )

        if challenge:

            challenge = str(
                challenge
            ).strip()

            facts.append(
                Fact(
                    category="API Security",
                    entity="Authentication",
                    name="authentication_required",
                    value=True,
                )
            )

            #
            # Extract actual scheme
            #
            scheme = challenge.split(
                None,
                1,
            )[0].strip()

            if scheme:

                facts.append(
                    Fact(
                        category="API Security",
                        entity="Authentication",
                        name="authentication_scheme",
                        value=scheme,
                    )
                )

            facts.append(
                Fact(
                    category="API Security",
                    entity="Authentication",
                    name="www_authenticate",
                    value=challenge,
                )
            )

        #
        # Authorization header advertised
        #

        cors = normalized_data.get(
            "cors",
            {},
        )

        allow_headers = cors.get(
            "headers",
            "",
        )

        if isinstance(
            allow_headers,
            str,
        ):

            allowed_headers = {
                item.strip().lower()
                for item in allow_headers.split(",")
            }

            if "authorization" in allowed_headers:

                facts.append(
                    Fact(
                        category="API Security",
                        entity="Authentication",
                        name="authorization_header_supported",
                        value=True,
                    )
                )

     

        return facts

