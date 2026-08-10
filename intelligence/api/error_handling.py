from core.models.fact import Fact


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
    ) -> list[Fact]:

        facts = []

        body = normalized_data.get(
            "body",
            "",
        ).lower()

        for pattern, name in ERROR_PATTERNS.items():

            if pattern in body:

                facts.append(

                    Fact(

                        category="API Security",

                        entity="Error Handling",

                        name="error_information",

                        value=name,

                    )

                )

        return facts