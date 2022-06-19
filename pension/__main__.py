import logging
from datetime import datetime

from .config import Config
from .journey import PensionJourney
from .web import get_driver
from .output import output

logging.basicConfig(level=logging.INFO)


if __name__ == "__main__":
    try:
        driver = get_driver()
        journey = PensionJourney(driver, Config())
        valuations = list(journey.run())
    except Exception as error:
        with open(f"/error/{datetime.now()}.html", "w") as f:
            f.write(driver.page_source)
        raise RuntimeError(f"Error at {driver.current_url}") from error

    # Present results
    print(output(valuations))
