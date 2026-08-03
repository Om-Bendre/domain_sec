from core.models.finding import Finding


class PrefixAnalyzer:

    def analyze(
        self,
        cookie: dict,
    ) -> list[Finding]:

        findings = []

        name = cookie["name"]

        if name.startswith("__Host-"):

            findings.append(

                Finding(

                    category="Cookies",

                    entity=name,

                    name="prefix",

                    value="__Host-",

                )

            )

        elif name.startswith("__Secure-"):

            findings.append(

                Finding(

                    category="Cookies",

                    entity=name,

                    name="prefix",

                    value="__Secure-",

                )

            )

        return findings