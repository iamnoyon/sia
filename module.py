# -*- coding: utf-8 -*-

# Copyright(C) 2018 Sasha Bouloudnine

from monseigneur.core.tools.backend import Module
from .browser import SiaBrowser

__all__ = ['SiaModule']


class SiaModule(Module):
    NAME = 'sia'
    MAINTAINER = u'Jamal'
    EMAIL = '{first}.{last}@lobstr.io'
    BROWSER = SiaBrowser

    def iter_members(self, memberlist_page_no):
        return self.browser.iter_members(memberlist_page_no)
    def iter_members_details(self, lang, member_id):
        return self.browser.iter_members(lang, member_id)
