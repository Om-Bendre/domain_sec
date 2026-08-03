from core.models.finding import Finding


class RegistrarAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Finding]:

        findings = []

        registrar = normalized_data.get(
            "registrar",
        )

        if registrar:

            findings.append(

                Finding(

                    category="WHOIS",

                    entity="Registrar",

                    name="registrar",

                    value=registrar,

                )

            )

        registrar_url = normalized_data.get(
            "registrar_url",
        )

        if registrar_url:

            findings.append(

                Finding(

                    category="WHOIS",

                    entity="Registrar",

                    name="registrar_url",

                    value=registrar_url,

                )

            )

        registrar_id = normalized_data.get(
            "registrar_iana_id",
        )

        if registrar_id:

            findings.append(

                Finding(

                    category="WHOIS",

                    entity="Registrar",

                    name="registrar_iana_id",

                    value=registrar_id,

                )

            )

        return findings