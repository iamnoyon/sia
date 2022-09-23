from typing_extensions import Self
from monseigneur.core.browser.pages import HTMLPage, JsonPage, pagination, Page
from monseigneur.core.browser.elements import ItemElement, ListElement, method, DictElement
from monseigneur.core.browser.filters.html import Link, AbsoluteLink
from monseigneur.core.browser.filters.json import Dict
from monseigneur.core.browser.filters.standard import CleanText, Regexp, CleanDecimal, Currency, DateTime, Env, Field, Currency as CleanCurrency, CleanDate
from alchemy.tables import Members

import json

class ListPage(HTMLPage):

    ENCODING = 'UTF8'

    def build_doc(self, content):

        self.html_doc = HTMLPage.build_doc(self, content)

        add_content = CleanText('//script[contains(text(), "__REDIAL_PROPS__")]')(self.html_doc)

        add_content = add_content.replace('window.__REDIAL_PROPS__ =', '')
        add_content = json.loads(add_content)

        for content in add_content:
            if content != None:
                self.doc = content
                return self.doc

@method
class MemberListPage(HTMLPage):
    item_xpath = "//table//tr"
    class iter_members(ListElement):
        klass = Members
        def obj_zipcode(self):
            return self.el.xpath('/td[4]')

class MemberPage(HTMLPage):
    class iter_members_details(ItemElement):
        klass = Members
        def obj_url(self):
            pass
        def obj_language(self):
            pass
        def obj_full_address(self):
            return self.el.xpath('//table//tr[2]/td/text()')
        def obj_gender(self):
            return self.el.xpath('//table//tr[2]/td/font[1]/font/text()')[0]
        def obj_name(self):
            return self.el.xpath('//table//tr[2]/td/font[2]/font/text()')[0]
        def obj_education(self):
            return self.el.xpath('//table//tr[2]/td/font[3]/font/text()')
        def obj_address(self):
            return self.el.xpath('//table//tr[2]/td/font[4]/font/text()')[0]
        def obj_city(self):
             return self.el.xpath('//table//tr[2]/td/font[5]/font/text()')[0]
        def obj_email(self):
            #decreption
            pass
        def obj_tel(self):
            #decreption
            pass
        def obj_fax(self):
            #decreption
            pass
        def obj_website(self):
            #decreption
            pass
        def obj_job(self):
            return self.el.xpath('//table//tr[6]/td[2]//text()')[0]
        def obj_sector(self):
            return self.el.xpath('//table//tr[7]/td[2]//text()')[0]
        def obj_group(self):
            return self.el.xpath('//table//tr[8]/td[2]//text()')[0]
        def obj_section(self):
            return self.el.xpath('//table//tr[9]/td[2]//text()')[0]
        


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

