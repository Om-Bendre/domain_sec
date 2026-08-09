from core.models.finding import Finding


class NameServerAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Finding]:

        findings = []

        nameservers = normalized_data.get(
            "nameservers",
            [],
        )

        findings.append(

            Finding(

                category="DNS",

                entity="Name Servers",

                name="count",

                value=len(nameservers),

            )

        )

        # for ns in nameservers:

        #     findings.append(

        #         Finding(

        #             category="DNS",

        #             entity="Name Servers",

        #             name="nameserver",

        #             value=ns,

        #         )

        #     )

        return findings