from core.models.fact import Fact


class RegistrarAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Fact]:

        facts = []

        registrar = normalized_data.get(
            "registrar",
        )

        if registrar:

            facts.append(

                Fact(

                    category="WHOIS",

                    entity="Registrar",

                    name="registrar",

                    value=registrar,

                )

            )

       
        registrar_id = normalized_data.get(
            "registrar_iana_id",
        )

        if registrar_id:

            facts.append(

                Fact(

                    category="WHOIS",

                    entity="Registrar",

                    name="registrar_iana_id",

                    value=registrar_id,

                )

            )

        return facts