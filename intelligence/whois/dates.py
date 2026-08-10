from datetime import datetime, timezone

from core.models.fact import Fact


class DatesAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Fact]:

        facts = []

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

            facts.append(

                Fact(

                    category="WHOIS",

                    entity="Dates",

                    name="creation_date",

                    value=created,

                )

            )

        if updated:

            facts.append(

                Fact(

                    category="WHOIS",

                    entity="Dates",

                    name="updated_date",

                    value=updated,

                )

            )

        if expires:

            facts.append(

                Fact(

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

            if created.tzinfo is not None:

                created = created.astimezone(
                    timezone.utc,
                )

                now = datetime.now(
                    timezone.utc,
                )

            else:

                now = datetime.now()

            age = (

                now -

                created

            ).days
            
            facts.append(

                Fact(

                    category="WHOIS",

                    entity="Dates",

                    name="domain_age_days",

                    value=age,

                )

            )

        return facts