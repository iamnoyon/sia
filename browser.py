# -*- coding: utf-8 -*-

# Copyright(C) 2018 Sasha Bouloudnine

from monseigneur.core.browser import PagesBrowser, URL
from .pages import MemberListPage, MemberPage, OfficeListPage, OfficePage
import pandas as pd

__all__ = ['SiaBrowser']


class SiaBrowser(PagesBrowser):

    BASEURL = 'https://www.sia.ch/'

    memberlist_page= URL("https://www.sia.ch/fr/affiliation/liste-des-membres/membres-individuels/nc/1/\?tx_updsiafeuseradmin_pi1%5BdisplaySearchResult%5D=1&tx_updsiafeuseradmin_pi1%5Bpointer%5D=(?P<memberlist_page_no>\d+)", MemberListPage)

    member_page = URL("https://www.sia.ch/(?P<lang>\.+)/affiliation/liste-des-membres/membres-individuels/m/(?P<member_id>\d+)", MemberPage)

    office_list_page = URL("https://www.sia.ch/fr/affiliation/liste-des-membres/membres-bureaux/nc/1/?tx_updsiafeuseradmin_pi1%5BdisplaySearchResult%5D=1&tx_updsiafeuseradmin_pi1%5Bpointer%5D=(?P<office_list_page_no>\d+)", OfficeListPage)

    office_page = URL("https://www.sia.ch/(?P<lang>\.+)/affiliation/liste-des-membres/membres-bureaux/m/(?P<office_id>\d+)", OfficePage)

    def __init__(self, *args, **kwargs):
        zip_lang = 'zip_language.xlsx'
        self.df = pd.read_excel(zip_lang)
        super(SiaBrowser, self).__init__(*args, **kwargs)

    def iter_members(self, memberlist_page_no):
        self.memberlist_page.go(memberlist_page_no=memberlist_page_no)
        assert self.memberlist_page.is_here()
        return self.page.iter_members()

    def iter_members_details(self, lang, member_id):
        zip = self.page.get_zip()
        lang= self.page.get_lang(zip)
        self.member_page.go(lang=lang, member_id = member_id)
        assert self.member_page.is_here()
        return self.page.iter_members()

    def iter_offices(self, office_list_page_no):
        self.office_list_page.go(office_list_page_no=office_list_page_no)
        assert self.office_list_page.is_here()
        return self.page.iter_members()

    def iter_offices_details(self, office_id):
        zip = self.page.get_zip()
        lang= self.page.get_lang(zip)
        self.office_page.go(lang=lang, office_id=office_id)
        assert self.office_page.is_here()
        return self.page.iter_members()
