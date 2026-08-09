from core.models.finding import Finding


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
    ) -> list[Finding]:

        findings = []

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

        #
        # MX
        #

        mx_present = bool(mx_records)

        findings.append(

            Finding(

                category="DNS",

                entity="Mail",

                name="mx_present",

                value=mx_present,

            )

        )

        #
        # Mail Provider
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

            findings.append(

                Finding(

                    category="DNS",

                    entity="Mail",

                    name="mail_provider",

                    value=mail_provider,

                )

            )

        #
        # SPF / DMARC
        #

        spf_present = False

        dmarc_present = False

        for record in txt_records:

            text = str(record).strip().lower()

            if text.startswith("v=spf1"):

                spf_present = True

            elif text.startswith("v=dmarc1"):

                dmarc_present = True

        findings.append(

            Finding(

                category="DNS",

                entity="Mail",

                name="spf_present",

                value=spf_present,

            )

        )

        findings.append(

            Finding(

                category="DNS",

                entity="Mail",

                name="dmarc_present",

                value=dmarc_present,

            )

        )

        return findings