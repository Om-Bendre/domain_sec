from core.models.finding import Finding


class ContactsAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Finding]:

        findings = []

        fields = {

            "registrant_country": "Registrant Country",

            "registrant_organization": "Registrant Organization",

            "abuse_email": "Abuse Email",

            "registrant_email": "Registrant Email",

        }

        for field, entity in fields.items():

            value = normalized_data.get(
                field,
            )

            if value:

                findings.append(

                    Finding(

                        category="WHOIS",

                        entity=entity,

                        name=field,

                        value=value,

                    )

                )

        return findings