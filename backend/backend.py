from mbackend.core.fetcher import Fetcher
from mbackend.core.application import Application
from monseigneur.modules.public.sia.alchemy.dao_manager import DaoManager
from monseigneur.modules.public.sia.alchemy.tables import Members
import time


class SiaBackend(Application):

    APPNAME = "Application Sia"
    VERSION = '1.0'
    COPYRIGHT = 'Copyright(C) 2012-YEAR LOBSTR'
    DESCRIPTION = "Scraping Backend for Sia.ch"
    SHORT_DESCRIPTION = "Sia Scraping"

    def __init__(self):
        super(SiaBackend, self).__init__(self.APPNAME)
        self.setup_logging()
        self.fetcher = Fetcher()
        self.module = self.fetcher.build_backend("sia", params={})

        self.dao = DaoManager("sia")
        self.session, self.scoped_session = self.dao.get_shared_session()

    def main(self):
        members = self.module.iter_members(page=1)
        for member in members:
            print(member.__dict__)


if __name__ == '__main__':
    my = SiaBackend()
    my.main()
