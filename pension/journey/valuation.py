import dataclasses


@dataclasses.dataclass(init=False)
class Valuation:
    fund: str
    units_held: float
    unit_price: float
    value: float

    def __init__(self, fund, units_held, unit_price, value):
        def floatify(v):
            return float(v.replace(",", "")) if isinstance(v, str) else v

        self.fund = fund
        self.units_held = floatify(units_held)
        self.unit_price = floatify(unit_price)
        self.value = floatify(value)
