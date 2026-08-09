import ipaddress
import re
import socket

from urllib.parse import urlparse

from core.enums.scan import TargetType
from core.models.resolved_target import ResolvedTarget


class TargetResolver:

    DOMAIN_REGEX = re.compile(
        r"^(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$"
    )

    def resolve(
        self,
        target: str,
    ) -> ResolvedTarget:

        target = target.strip()


        # IP

        try:

            ipaddress.ip_address(target)

            return ResolvedTarget(

                original=target,

                target_type=TargetType.IP,

                ip=target,

                url=f"https://{target}",

                domain=None,

            )

        except ValueError:

            pass

        # URL

        parsed = urlparse(target)

        if parsed.scheme and parsed.netloc:

            domain = parsed.hostname

            ip = None

            try:

                ip = socket.gethostbyname(
                    domain,
                )

            except Exception:

                pass

            return ResolvedTarget(

                original=target,

                target_type=TargetType.URL,

                url=target,

                domain=domain,

                ip=ip,

            )

        # Domain

        if self.DOMAIN_REGEX.fullmatch(target):

            ip = None

            try:

                ip = socket.gethostbyname(
                    target,
                )

            except Exception:

                pass

            return ResolvedTarget(

                original=target,

                target_type=TargetType.DOMAIN,

                domain=target,

                url=f"https://{target}",

                ip=ip,

            )

        # Invalid

        return ResolvedTarget(

            original=target,

            target_type=TargetType.INVALID,

        )