from pprint import pprint

from core.models.configuration import Configuration

from core.orchestrator.orchestrator import Orchestrator


orchestrator = Orchestrator()

inp = input("enter url after https://")

result = orchestrator.scan(

    f"https://{inp}",

    Configuration(),

)

print()

print("=" * 80)

print("ORCHESTRATOR")

print("=" * 80)

print()

pprint(

    result.model_dump(),

)