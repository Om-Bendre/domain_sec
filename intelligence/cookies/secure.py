from core.models.fact import Fact


class SecureAnalyzer:

    def analyze(
        self,
        cookie: dict,
    ) -> list[Fact]:


        return [

            Fact(

                category="Cookies",

                entity=cookie["name"],

                name="secure",

                value="secure" in cookie["attributes"],

            )

        ]