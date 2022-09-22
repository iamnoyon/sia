from mbackend.core.fetcher import Fetcher
from mbackend.core.application import Application
from monseigneur.modules.public.lequipe.alchemy.dao_manager import DaoManager
from monseigneur.modules.public.lequipe.alchemy.tables import Article
import time


class LequipeBackend(Application):

    APPNAME = "Application Lequipe"
    VERSION = '1.0'
    COPYRIGHT = 'Copyright(C) 2012-YEAR LOBSTR'
    DESCRIPTION = "Scraping Backend for Lequipe"
    SHORT_DESCRIPTION = "Step-by-step Example of Lequipe Scraping"

    def __init__(self):
        super(LequipeBackend, self).__init__(self.APPNAME)
        self.setup_logging()
        self.fetcher = Fetcher()
        self.module = self.fetcher.build_backend("lequipe", params={})

        self.dao = DaoManager("lequipe")
        self.session, self.scoped_session = self.dao.get_shared_session()

    def main(self):
        for page in range(1, 5):
            articles = self.module.iter_articles(page=page)
            for article in articles:
                print(article.__dict__)
                if not self.session.query(Article).filter(Article.internal_id == article.internal_id).count():
                    self.session.add(article)
                    self.session.commit()


if __name__ == '__main__':
    my = LequipeBackend()
    my.main()
