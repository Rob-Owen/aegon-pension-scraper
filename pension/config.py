import os


class Config:
    def __init__(self):
        self.login = os.environ["PENSION_USERNAME"]
        self.password = os.environ["PENSION_PASSWORD"]
        self.start_url = "https://extranet.secure.aegon.co.uk/"
