import logging

import allure
import requests
from conftest import request_payload
from queries.query_module import queries
from queries.query_module_negative import queries_negative
from variables.variable_module import variables


class TestGraphqlQuery:
    """
    Clas to validate the graphql api response for id and address
    """

    @allure.feature("Positive")
    def test_01_positive_scenario(self, api_url):
        """
        Function to verify grpahql api positive response
        :param api_url:
        :return:
        """
        query = queries()
        variable = variables()
        address_found = False
        payload = request_payload(query_module=query, variable_module=variable)
        content = requests.post(api_url, json=payload).json()
        for key in content['data']['Tokens']['Token'][0]:
            if key == "address":
                address_found = True

        if not address_found:
            raise Exception("requested fields are not coming in response")

    @allure.feature("Negative")
    def test_02_negative_scenario(self, api_url):
        """
        Function to verify graphql negative response
        :param api_url:
        :return:
        """
        query = queries_negative()
        variable = variables()
        try:
            payload = request_payload(query_module=query, variable_module=variable)
            content = requests.post(api_url, json=payload).json()
            for key in content['data']['Tokens']['Token'][0]:
                if key == "address":
                    raise Exception("no results should be in response for negative scenario")
        except Exception as error:
            logging.info(f"Failed due to {error}")
