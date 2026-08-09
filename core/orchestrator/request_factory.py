from core.models.resolved_target import ResolvedTarget


class RequestFactory:

    def create(
        self,
        scanner_class,
        target: ResolvedTarget,
    ):

        request_model = scanner_class.REQUEST_MODEL

        if request_model is None:

            raise ValueError(

                f"{scanner_class.__name__} "
                "does not define REQUEST_MODEL."

            )

        return request_model(

            target=target,

        )