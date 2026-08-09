from core.models.finding import Finding


class SecureAnalyzer:

    def analyze(
        self,
        cookie: dict,
    ) -> list[Finding]:


        return [

            Finding(

                category="Cookies",

                entity=cookie["name"],

                name="secure",

                value="secure" in cookie["attributes"],

            )

        ]