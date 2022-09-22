# -*- coding: utf-8 -*-

# Copyright(C) 2018 Sasha Bouloudnine

from monseigneur.core.tools.backend import Module
from .browser import LequipeBrowser

__all__ = ['LequipeModule']


class LequipeModule(Module):
    NAME = 'Lequipe'
    MAINTAINER = u'Jamal'
    EMAIL = '{first}.{last}@lobstr.io'
    BROWSER = LequipeBrowser

    def iter_articles(self, page):
        return self.browser.iter_articles(page)
