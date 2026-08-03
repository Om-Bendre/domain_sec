from core.models.finding import Finding


class CipherAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Finding]:

        findings = []

        cipher = normalized_data.get(
            "cipher_suite",
        )

        bits = normalized_data.get(
            "cipher_bits",
        )

        if cipher:

            findings.append(

                Finding(

                    category="TLS",

                    entity="Cipher",

                    name="cipher_suite",

                    value=cipher,

                )

            )

        if bits:

            findings.append(

                Finding(

                    category="TLS",

                    entity="Cipher",

                    name="cipher_bits",

                    value=bits,

                )

            )

        return findings