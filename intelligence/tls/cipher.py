from core.models.fact import Fact


class CipherAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Fact]:

        facts = []

        cipher = normalized_data.get(
            "cipher_suite",
        )

        bits = normalized_data.get(
            "cipher_bits",
        )

        if cipher:

            facts.append(

                Fact(

                    category="TLS",

                    entity="Cipher",

                    name="cipher_suite",

                    value=cipher,

                )

            )

        if bits:

            facts.append(

                Fact(

                    category="TLS",

                    entity="Cipher",

                    name="cipher_bits",

                    value=bits,

                )

            )

        return facts