from core.models.finding import Finding


ERROR_PATTERNS = {

    "stack trace": "Stack Trace",

    "traceback": "Python Traceback",

    "exception": "Exception",

    "nullpointerexception": "Java Exception",

    "sql syntax": "SQL Error",

    "fatal error": "Fatal Error",

    "debug": "Debug Information",

    "internal server error": "Internal Error",

}


class ErrorHandlingAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Finding]:

        findings = []

        body = normalized_data.get(
            "body",
            "",
        ).lower()

        for pattern, name in ERROR_PATTERNS.items():

            if pattern in body:

                findings.append(

                    Finding(

                        category="API Security",

                        entity="Error Handling",

                        name="error_information",

                        value=name,

                    )

                )

        return findings