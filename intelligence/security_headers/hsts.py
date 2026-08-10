from core.models.fact import Fact


class HSTSAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Fact]:

        facts = []

        hsts = normalized_data.get(
            "hsts",
        )

        #
        # HSTS Missing
        #

        if not hsts:

            facts.append(

                Fact(

                    category="Security Headers",

                    entity="HSTS",

                    name="present",

                    value=False,

                )

            )

            return facts

        #
        # HSTS Present
        #

        facts.append(

            Fact(

                category="Security Headers",

                entity="HSTS",

                name="present",

                value=True,

            )

        )

        #
        # Parse directives
        #

        max_age = None

        include_subdomains = False

        preload = False

        directives = [

            directive.strip()

            for directive in hsts.split(";")

            if directive.strip()

        ]

        for directive in directives:

            lower = directive.lower()

            if lower.startswith("max-age="):

                try:

                    max_age = int(

                        directive.split("=")[1]

                    )

                except ValueError:

                    pass

            elif lower == "includesubdomains":

                include_subdomains = True

            elif lower == "preload":

                preload = True

        #
        # Fact
        #

        facts.append(

            Fact(

                category="Security Headers",

                entity="HSTS",

                name="max_age",

                value=max_age,

            )

        )

        facts.append(

            Fact(

                category="Security Headers",

                entity="HSTS",

                name="include_subdomains",

                value=include_subdomains,

            )

        )

        facts.append(

            Fact(

                category="Security Headers",

                entity="HSTS",

                name="preload",

                value=preload,

            )

        )

        return facts