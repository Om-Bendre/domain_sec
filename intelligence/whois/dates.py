from datetime import datetime

from core.models.finding import Finding


class DatesAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Finding]:

        findings = []

        created = normalized_data.get(
            "creation_date",
        )

        updated = normalized_data.get(
            "updated_date",
        )

        expires = normalized_data.get(
            "expiration_date",
        )

        if created:

            findings.append(

                Finding(

                    category="WHOIS",

                    entity="Dates",

                    name="creation_date",

                    value=created,

                )

            )

        if updated:

            findings.append(

                Finding(

                    category="WHOIS",

                    entity="Dates",

                    name="updated_date",

                    value=updated,

                )

            )

        if expires:

            findings.append(

                Finding(

                    category="WHOIS",

                    entity="Dates",

                    name="expiration_date",

                    value=expires,

                )

            )

        if isinstance(
            created,
            datetime,
        ):

            age = (

                datetime.utcnow() -

                created

            ).days

            findings.append(

                Finding(

                    category="WHOIS",

                    entity="Dates",

                    name="domain_age_days",

                    value=age,

                )

            )

        return findings