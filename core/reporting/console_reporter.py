from core.models.scan_result import ScanResult


class ConsoleReporter:
    """
    Displays ScanResult objects in the terminal.
    """

    def report(self, result: ScanResult):

        print("\n====================================")
        print(f"Scanner : {result.scanner}")
        print(f"Status  : {result.status.value}")
        print("====================================\n")

        print("Context")

        print(f" Target      : {result.context.target}")
        print(f" Type        : {result.context.target_type.value}")
        print(f" Scan Type   : {result.context.scan_type.value}")
        print(f" Duration    : {result.context.duration_ms:.2f} ms")

        print("\nFindings")

        if not result.findings:
            print(" None")

        else:
            for finding in result.findings:

                print(f"\n{finding.name}")

                print(f"  Category : {finding.category}")

                print(f"  Value    : {finding.value}")

                if finding.description:
                    print(f"  Description : {finding.description}")

                if finding.metadata:
                    print(f"  Metadata : {finding.metadata}")

        if result.errors:

            print("\nErrors")

            for error in result.errors:

                print(f"\n{error.error_type}")

                print(f"  Message : {error.message}")