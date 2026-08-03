from core.models.finding import Finding


class NameServersAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Finding]:

        findings = []

        nameservers = normalized_data.get(
            "name_servers",
            [],
        )

        findings.append(

            Finding(

                category="WHOIS",

                entity="Name Servers",

                name="count",

                value=len(nameservers),

            )

        )

        for ns in nameservers:

            findings.append(

                Finding(

                    category="WHOIS",

                    entity="Name Servers",

                    name="name_server",

                    value=ns,

                )

            )

        return findings