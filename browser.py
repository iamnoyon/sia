# -*- coding: utf-8 -*-

# Copyright(C) 2018 Sasha Bouloudnine

from monseigneur.core.browser import PagesBrowser, URL
from .pages import MemberListPage, MemberPage, OfficeListPage, OfficePage
import pandas as pd
import re

__all__ = ['SiaBrowser']


class SiaBrowser(PagesBrowser):

    BASEURL = 'https://www.sia.ch/'

    memberlist_page= URL("https://www.sia.ch/fr/affiliation/liste-des-membres/membres-individuels/nc/1/\?tx_updsiafeuseradmin_pi1%5BdisplaySearchResult%5D=1&tx_updsiafeuseradmin_pi1%5Bpointer%5D=(?P<memberlist_page_no>\d+)", MemberListPage)

    member_details_page = URL("https://www.sia.ch/(?P<language>.+)/affiliation/liste-des-membres/membres-individuels/m/(?P<member_id>\d+)/", MemberPage)

    office_list_page = URL("https://www.sia.ch/fr/affiliation/liste-des-membres/membres-bureaux/nc/1/?tx_updsiafeuseradmin_pi1%5BdisplaySearchResult%5D=1&tx_updsiafeuseradmin_pi1%5Bpointer%5D=(?P<offices_list_page_no>\d+)", OfficeListPage)

    office_details_page = URL("https://www.sia.ch/(?P<language>.+)/affiliation/liste-des-membres/membres-bureaux/m/(?P<office_id>\d+)/", OfficePage)

    def __init__(self, *args, **kwargs):
        zip_lang = 'zip_language.xlsx'
        self.df = pd.read_excel(zip_lang)
        super(SiaBrowser, self).__init__(*args, **kwargs)

    def iter_members(self, memberlist_page_no):
        self.memberlist_page.go(memberlist_page_no=memberlist_page_no)
        assert self.memberlist_page.is_here()
        return self.page.iter_members()

    def members_details(self, language, url):
        #zip = self.page.get_zip()
        #lang= self.page.get_lang(zip)
        member_id = re.findall(r'(\d+)', url)[0]
        language = language.lower()
        self.member_details_page.go(language=language, member_id = member_id)
        #print('Hello:', self.member_details_page)
        assert self.member_details_page.is_here()
        return self.page.get_members_details(self.page)

    def iter_offices(self, offices_list_page_no):
        self.office_list_page.go(offices_list_page_no=offices_list_page_no)
        assert self.office_list_page.is_here()
        return self.page.iter_offices()

    def offices_details(self, language, url):
        office_id = re.findall(r'(\d+)', url)[0]
        language = language.lower()
        self.office_details_page.go(language=language, office_id = office_id)
        #print('Hello:', self.office_details_page)
        assert self.office_details_page.is_here()
        return self.page.get_offices_details(self.page)
