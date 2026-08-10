import base64
import json

from core.models.fact import Fact


class JWTAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Fact]:

        facts = []

        cookies = normalized_data.get(
            "cookies",
            [],
        )

        for cookie in cookies:

            try:

                value = cookie.split(
                    "=",
                    1,
                )[1].split(
                    ";",
                    1,
                )[0]

            except Exception:

                continue

            if value.count(".") != 2:

                continue

            try:

                header, payload = self._decode(
                    value,
                )

            except Exception:

                continue

            facts.append(

                Fact(

                    category="Authentication",

                    entity="JWT",

                    name="jwt_detected",

                    value=True,

                )

            )

            facts.append(

                Fact(

                    category="Authentication",

                    entity="JWT",

                    name="algorithm",

                    value=header.get(
                        "alg",
                    ),

                )

            )

            facts.append(

                Fact(

                    category="Authentication",

                    entity="JWT",

                    name="issuer",

                    value=payload.get(
                        "iss",
                    ),

                )

            )

            facts.append(

                Fact(

                    category="Authentication",

                    entity="JWT",

                    name="subject",

                    value=payload.get(
                        "sub",
                    ),

                )

            )

            facts.append(

                Fact(

                    category="Authentication",

                    entity="JWT",

                    name="audience",

                    value=payload.get(
                        "aud",
                    ),

                )

            )

            facts.append(

                Fact(

                    category="Authentication",

                    entity="JWT",

                    name="expiration",

                    value=payload.get(
                        "exp",
                    ),

                )

            )

        return facts

    def _decode(
        self,
        token: str,
    ):

        header, payload, _ = token.split(".")

        header = json.loads(

            base64.urlsafe_b64decode(

                self._pad(header)

            )

        )

        payload = json.loads(

            base64.urlsafe_b64decode(

                self._pad(payload)

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