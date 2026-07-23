class CookieNormalizer:
    """
    Normalize Set-Cookie headers into structured cookie objects.
    """

    def normalize(
        self,
        raw_data: dict,
    ) -> list[dict]:

        raw_headers = raw_data.get(
            "raw_headers"
        )

        if raw_headers is None:
            return []

        set_cookies = raw_headers.get_all(
            "Set-Cookie"
        )

        if not set_cookies:
            return []

        cookies = []

        for header in set_cookies:

            cookies.append(
                self._parse_cookie(header)
            )

        return cookies

    def _parse_cookie(
        self,
        header: str,
    ) -> dict:

        parts = [

            part.strip()

            for part in header.split(";")

        ]

        #
        # First element:
        # sessionid=abc123
        #

        name, value = parts[0].split(
            "=",
            1,
        )

        attributes = {}

        for part in parts[1:]:

            if "=" in part:

                key, val = part.split(
                    "=",
                    1,
                )

                attributes[
                    key.lower()
                ] = val

            else:

                attributes[
                    part.lower()
                ] = True

        return {

            "name": name,

            "value": value,

            "attributes": attributes,

        }