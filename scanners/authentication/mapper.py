from core.models.finding import Finding


class AuthenticationMapper:

    def map(
        self,
        authentication_data: dict,
    ) -> list[Finding]:

        findings = []

        for key, value in authentication_data.items():

            findings.append(

                Finding(

                    category="Authentication",

                    name=key,

                    value=value,

                )

            )

        return findings