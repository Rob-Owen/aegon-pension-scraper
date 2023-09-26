import time
import re

from .selectors import *
from .valuation import Valuation
from pension.web import element_by_css, element_by_id


class PensionJourney:
    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def _login(self):
        self.driver.get(self.config.start_url)
        # element_by_css(self.driver, CSS_LOGIN_PAGE).click()
        element_by_id(self.driver, ID_USERNAME_FIELD).send_keys(self.config.login)
        element_by_id(self.driver, ID_PASSWORD_FIELD).send_keys(self.config.password)
        self.driver.find_element_by_xpath(XPATH_LOGIN_BUTTON).click()

    def _enter_plan(self):
        # Enter the first tabulated pension plan
        element_by_css(self.driver, CSS_FIRST_PLAN).click()

    def _parse_valuations(self):
        time.sleep(5)
        page = self.driver.page_source
        matches = re.findall(
            r'"\$FundName\$pyButtonLabel":"(?P<fund>[\s\w]*)","\$TotalUnits\$pyCaption":"(?P<units>[\d\.]*)","\$BidPrice\$pyCaption":"(?P<unit_price>[\d\.]*)","\$TotalValue\$pyCaption":"(?P<total>[\d\.]*)"',
            page,
        )
        return [Valuation(*m) for m in matches]

    def run(self):
        self._login()
        self._enter_plan()
        return self._parse_valuations()
