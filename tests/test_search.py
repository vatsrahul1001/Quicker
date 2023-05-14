import time

import pytest


from TestData.SearchData import SearchData


from pageObjects.Google import GooglePage
from utilities.BaseClass import BaseClass


class TestSearch(BaseClass):

    """This test make a google search and validate the first link result with a test data specified in SearchData.py
    It  takes a fixture get_search_data as a param which gets the test data as list from SearchData.py

    We can specify multiple test data in searchData.py and multiple test will run as per provided test data

        test_search_data = [{"search_data": "fiserv","expected_url":"https://www.fiserv.com/"},
                    {"search_data": "Testing","expected_url":"https://www.ibm.com/topics/software-testing"}]

    """

    @pytest.mark.run(order=1)
    def test_google_search(self, get_search_data):
        google_search = GooglePage(self.driver)
        google_search.perform_google_search(get_search_data)
        first_result_link = google_search.get_first_result_href()
        assert get_search_data["expected_url"] == first_result_link

    @pytest.fixture(params=SearchData.test_search_data)
    def get_search_data(self, request):
        return request.param
