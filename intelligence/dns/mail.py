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

        findings.append(

            Finding(

                category="DNS",

                entity="Mail",

                name="mx_present",

                value=bool(mx_records),

            )

        )

        for record in mx_records:

            findings.append(

                Finding(

                    category="DNS",

                    entity="Mail",

                    name="mx_record",

                    value=record,

                )

            )

            text = str(record).lower()

            for key, provider in self.PROVIDERS.items():

                if key in text:

                    findings.append(

                        Finding(

                            category="DNS",

                            entity="Mail",

                            name="mail_provider",

                            value=provider,

                        )

                    )

                    break

        #
        # SPF
        #

        for txt in txt_records:

            txt = str(txt)

            if txt.lower().startswith("v=spf1"):

                findings.append(

                    Finding(

                        category="DNS",

                        entity="Mail",

                        name="spf_present",

                        value=True,

                    )

                )

                findings.append(

                    Finding(

                        category="DNS",

                        entity="Mail",

                        name="spf_record",

                        value=txt,

                    )

                )

            if txt.lower().startswith("v=dmarc1"):

                findings.append(

                    Finding(

                        category="DNS",

                        entity="Mail",

                        name="dmarc_present",

                        value=True,

                    )

                )

                findings.append(

                    Finding(

                        category="DNS",

                        entity="Mail",

                        name="dmarc_record",

                        value=txt,

                    )

                )

        return findings