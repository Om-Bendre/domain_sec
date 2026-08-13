from core.models.fact import Fact


class MailAnalyzer:

    PROVIDERS = {
        "google": "Google Workspace",
        "googlemail": "Google Workspace",
        "outlook": "Microsoft 365",
        "protection.outlook": "Microsoft 365",
        "zoho": "Zoho Mail",
        "yahoodns": "Yahoo",
        "secureserver": "GoDaddy",
    }

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Fact]:

        facts = []

        mail = normalized_data.get(
            "mail",
            {},
        )

        mx_records = mail.get(
            "mx",
            [],
        )

        txt_records = mail.get(
            "txt",
            [],
        )

        dmarc_records = mail.get(
            "dmarc",
            [],
        )

        #
        # Mail provider
        #

        mail_provider = None

        for record in mx_records:

            text = str(record).lower()

            for key, provider in self.PROVIDERS.items():

                if key in text:

                    mail_provider = provider
                    break

            if mail_provider:
                break

        if mail_provider:

            facts.append(
                Fact(
                    category="DNS",
                    entity="Mail",
                    name="mail_provider",
                    value=mail_provider,
                )
            )

        #
        # SPF
        #

        spf_present = any(
            str(record)
            .strip()
            .lower()
            .startswith("v=spf1")
            for record in txt_records
        )

        facts.append(
            Fact(
                category="DNS",
                entity="Mail",
                name="spf_present",
                value=spf_present,
            )
        )

        #
        # DMARC
        #

        dmarc_present = any(
            str(record)
            .strip()
            .lower()
            .startswith("v=dmarc1")
            for record in dmarc_records
        )

        facts.append(
            Fact(
                category="DNS",
                entity="Mail",
                name="dmarc_present",
                value=dmarc_present,
            )
        )

        return facts