import dataclasses
import json
from datetime import datetime

from .journey import Valuation


class DataclassJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        return super().default(o)


def output(valuations: list[Valuation]) -> str:
    date_key = datetime.today().strftime("%d-%m-%Y")
    data = {
        date_key: {
            'totalValue': sum(v.value for v in valuations),
            'valuations': {v.fund : v for v in valuations}
        }
    }
    return json.dumps(data, cls=DataclassJSONEncoder)
