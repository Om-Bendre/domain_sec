from core.models.fact import Fact


class DNSSECAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Fact]:

        facts = []

        dnssec = normalized_data.get(
            "dnssec",
            {},
        )

        enabled = dnssec.get(
            "enabled",
            False,
        )

        facts.append(
            Fact(
                category="DNS",
                entity="DNSSEC",
                name="dnssec_enabled",
                value=enabled,
            )
        )

        if dnssec.get("dnskeys"):

            facts.append(
                Fact(
                    category="DNS",
                    entity="DNSSEC",
                    name="dnskey_present",
                    value=True,
                )
            )

        if dnssec.get("ds"):

            facts.append(
                Fact(
                    category="DNS",
                    entity="DNSSEC",
                    name="ds_record_present",
                    value=True,
                )
            )

        return facts