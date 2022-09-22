from typing_extensions import Self
from monseigneur.core.browser.pages import HTMLPage, JsonPage, pagination, Page
from monseigneur.core.browser.elements import ItemElement, ListElement, method, DictElement
from monseigneur.core.browser.filters.html import Link, AbsoluteLink
from monseigneur.core.browser.filters.json import Dict
from monseigneur.core.browser.filters.standard import CleanText, Regexp, CleanDecimal, Currency, DateTime, Env, Field, Currency as CleanCurrency, CleanDate
from alchemy.tables import Members

import json

@method
class MemberListPage(HTMLPage):
    item_xpath = "//table//tr"
    class iter_members(DictElement):
        def get_zip(self):
            print(self.doc.xpath('/td[4]'))
            return CleanText(self.doc.xpath('/td[4]'))

        class get_members(ItemElement):
            klass = Members

class MemberPage(HTMLPage):
    class iter_members_details(DictElement):
        item_xpath = "data/ads"

        class get_members_details(ItemElement):
            klass = Members

class OfficeListPage(HTMLPage):
    class iter_offices(DictElement):
        item_xpath = "data/ads"

        class get_offices(ItemElement):
            klass = Members

class OfficePage(HTMLPage):
    class iter_offices_details(DictElement):
        item_xpath = "data/ads"

        class get_offices_details(ItemElement):
            klass = Members

