# coding=utf-8
import pytest
from operations.search_page import SearchPage
from tests.base_test import BaseTest

class TestSearch(BaseTest):
    def test_search(self):
        self.page = SearchPage().make_a_search(self.driver, self.wait)
        assert self.page == 'Your password is ncorrect'





