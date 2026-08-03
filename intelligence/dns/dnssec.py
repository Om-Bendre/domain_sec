from core.models.finding import Finding


class DNSSECAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Finding]:

        findings = []

        dnssec = normalized_data.get(
            "dnssec",
            {},
        )

        enabled = dnssec.get(
            "enabled",
            False,
        )

        findings.append(

            Finding(

                category="DNS",

                entity="DNSSEC",

                name="dnssec_enabled",

                value=enabled,

            )

        )

        if dnssec.get(
            "dnskey",
        ):

            findings.append(

                Finding(

                    category="DNS",

                    entity="DNSSEC",

                    name="dnskey_present",

                    value=True,

                )

            )

        if dnssec.get(
            "ds",
        ):

            findings.append(

                Finding(

                    category="DNS",

                    entity="DNSSEC",

                    name="ds_record_present",

                    value=True,

                )

            )

        return findings