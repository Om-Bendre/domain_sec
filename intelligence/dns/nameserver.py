from core.models.fact import Fact


class NameServerAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Fact]:

        facts = []

        nameservers = normalized_data.get(
            "nameservers",
            [],
        )

        facts.append(

            Fact(

                category="DNS",

                entity="Name Servers",

                name="count",

                value=len(nameservers),

            )

        )

        # for ns in nameservers:

        #     facts.append(

        #         Fact(

        #             category="DNS",

        #             entity="Name Servers",

        #             name="nameserver",

        #             value=ns,

        #         )

        #     )

        return facts