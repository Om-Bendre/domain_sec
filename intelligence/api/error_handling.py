from core.models.fact import Fact


class ErrorHandlingAnalyzer:

    ERROR_MARKERS = (
        "traceback (most recent call last)",
        "stack trace",
        "java.lang.",
        "exception in thread",
        "fatal error",
        "syntaxerror:",
        "referenceerror:",
        "typeerror:",
        "filenotfounderror:",
    )

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Fact]:

        facts = []

        body = normalized_data.get(
            "body",
            "",
        )

        if not body:
            return facts

        body_lower = body.lower()

        matched_terms = []

        for marker in self.ERROR_MARKERS:

            if marker in body_lower:

                matched_terms.append(
                    marker
                )

        if not matched_terms:
            return facts

        facts.append(
            Fact(
                category="API Security",
                entity="Error",
                name="error_information",
                value=True,
                metadata={
                    "matched_terms": matched_terms,
                },
            )
        )

        return facts