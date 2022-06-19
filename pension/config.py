import os


class Config:
    def __init__(self):
        self.login = os.environ["PENSION_USERNAME"]
        self.password = os.environ["PENSION_PASSWORD"]
        self.start_url = "https://www.aegon.co.uk/Login.html"
