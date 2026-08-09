from time import perf_counter

from core.contracts.scanner import BaseScanner
from core.enums.scan import ScanStatus
from core.enums.scan import ScanType


from core.models.scan_context import ScanContext
from core.models.scan_error import ScanError
from core.models.scan_result import ScanResult

from core.models.requests.technology_request import TechnologyRequest
from core.models.configuration import Configuration

from scanners.technology.client import TechnologyClient
from scanners.technology.normalizer import TechnologyNormalizer
from scanners.technology.mapper import TechnologyMapper

from intelligence.technology.server import ServerAnalyzer
from intelligence.technology.framework import FrameworkAnalyzer
from intelligence.technology.cms import CMSAnalyzer
from intelligence.technology.javascript import JavaScriptAnalyzer
from intelligence.technology.frontend import FrontendAnalyzer
from intelligence.technology.backend import BackendAnalyzer
from intelligence.technology.hosting import HostingAnalyzer
from intelligence.technology.cdn import CDNAnalyzer
from intelligence.technology.analytics import AnalyticsAnalyzer



class TechnologyScanner(BaseScanner):

    NAME = "technology"

    REQUEST_MODEL = TechnologyRequest

    VERSION = "1.0.0"

    def __init__(self):

        self.client = TechnologyClient()

        self.normalizer = TechnologyNormalizer()

        self.mapper = TechnologyMapper()

        self.analyzers = [

            ServerAnalyzer(),

            FrameworkAnalyzer(),

            CMSAnalyzer(),

            JavaScriptAnalyzer(),

            FrontendAnalyzer(),

            BackendAnalyzer(),

            HostingAnalyzer(),

            CDNAnalyzer(),

            AnalyticsAnalyzer(),

    

        ]

    def scan(
        self,
        request: TechnologyRequest,
        configuration: Configuration,
    ) -> ScanResult:

        target_type = request.target.target_type

        start = perf_counter()

        context = ScanContext(

            target=request.target.original,

            target_type=target_type,

            scanner_name="Technology Scanner",

            scanner_version=self.VERSION,

            scan_type=ScanType.PASSIVE,

            duration_ms=0,

            configuration=configuration.model_dump(),

        )

        try:

            raw_data = self.client.query(

                request.target.url,

            )

            normalized_data = self.normalizer.normalize(

                raw_data,

            )

            findings = []

            for analyzer in self.analyzers:

                findings.extend(

                    analyzer.analyze(

                        normalized_data,

                    )

                )

            findings = self.mapper.map(

                findings,

            )

            context.duration_ms = (

                perf_counter() - start

            ) * 1000

            return ScanResult(

                scanner="Technology Scanner",

                status=ScanStatus.SUCCESS,

                context=context,

                findings=findings,

                raw_data= {},

            )

        except Exception as exc:

            context.duration_ms = (

                perf_counter() - start

            ) * 1000

            return ScanResult(

                scanner="Technology Scanner",

                status=ScanStatus.FAILED,

                context=context,

                errors=[

                    ScanError(

                        error_type=type(exc).__name__,

                        message=str(exc),

                    )
                ],

            )