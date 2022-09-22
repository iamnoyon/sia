# -*- coding: utf-8 -*-

# Copyright(C) 2018 Sasha Bouloudnine

from monseigneur.core.browser import PagesBrowser, URL
from .pages import MemberListPage, MemberPage, OfficeListPage, OfficePage

__all__ = ['LequipeBrowser']


class LequipeBrowser(PagesBrowser):

    BASEURL = 'https://www.sia.ch/'

    member_list_page = URL("https://www.sia.ch/fr/affiliation/liste-des-membres/membres-individuels/nc/1/?tx_updsiafeuseradmin_pi1%5BdisplaySearchResult%5D=1&tx_updsiafeuseradmin_pi1%5Bpointer%5D=(?P<memberlist_page>\d+)", MemberListPage)

    member_page = URL("https://www.sia.ch/(?P<lang>\.+)/affiliation/liste-des-membres/membres-individuels/m/(?P<member_id>\d+)", MemberPage)

    office_list_page = URL("https://www.sia.ch/fr/affiliation/liste-des-membres/membres-bureaux/nc/1/?tx_updsiafeuseradmin_pi1%5BdisplaySearchResult%5D=1&tx_updsiafeuseradmin_pi1%5Bpointer%5D=(?P<officelist_page>\d+)", OfficeListPage)

    office_page = URL("https://www.sia.ch/(?P<lang>\.+)/affiliation/liste-des-membres/membres-bureaux/m/(?P<office_id>\d+)", OfficePage)

    def __init__(self, *args, **kwargs):
        super(LequipeBrowser, self).__init__(*args, **kwargs)

    def iter_members(self, memberlist_page):
        self.member_list_page.go(page=memberlist_page)
        assert self.member_list_page.is_here()
        return self.page.iter_members()

    def iter_members_details(self, member_id):
        zip = self.page.get_zip()
        lang= self.page.get_lang(zip)
        self.member_page.go(lang=lang, member_id = member_id)
        assert self.member_page.is_here()
        return self.page.iter_members()

    def iter_offices(self, office_list_page):
        self.office_list_page.go(page=office_list_page)
        assert self.office_list_page.is_here()
        return self.page.iter_members()

    def iter_offices_details(self, office_id):
        zip = self.page.get_zip()
        lang= self.page.get_lang(zip)
        self.office_page.go(lang=lang, office_id=office_id)
        assert self.office_page.is_here()
        return self.page.iter_members()
