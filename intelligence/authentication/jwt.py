import base64
import json


class JWTAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> dict:

        headers = normalized_data.get(
            "headers",
            {},
        )

        cookies = normalized_data.get(
            "cookies",
            [],
        )

        token = self._find_jwt(
            headers,
            cookies,
        )

        if token is None:

            return {

                "jwt_detected": False,

            }

        try:

            header, payload = self._decode_jwt(
                token,
            )

        except Exception:

            return {

                "jwt_detected": True,

                "jwt_valid": False,

            }

        return {

            "jwt_detected": True,

            "jwt_valid": True,

            "algorithm": header.get(
                "alg"
            ),

            "type": header.get(
                "typ"
            ),

            "issuer": payload.get(
                "iss"
            ),

            "subject": payload.get(
                "sub"
            ),

            "audience": payload.get(
                "aud"
            ),

            "expiration": payload.get(
                "exp"
            ),

        }

    def _find_jwt(
        self,
        headers: dict,
        cookies: list,
    ):

        authorization = headers.get(
            "Authorization"
        )

        if authorization and authorization.startswith(
            "Bearer "
        ):

            return authorization.replace(
                "Bearer ",
                "",
            )

        for cookie in cookies:

            value = cookie.get(
                "value",
                "",
            )

            if value.count(".") == 2:

                return value

        return None

    def _decode_jwt(
        self,
        token: str,
    ):

        header, payload, _ = token.split(
            "."
        )

        header = json.loads(

            base64.urlsafe_b64decode(

                self._pad(
                    header
                )

            )

        )

        payload = json.loads(

            base64.urlsafe_b64decode(

                self._pad(
                    payload
                )

            )

        )

        return header, payload

    def _pad(
        self,
        value: str,
    ) -> str:

        return value + "=" * (
            -len(value) % 4
        )