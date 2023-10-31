import json
import pytest
from queries.query_module import *
from variables.variable_module import variables
import subprocess
from pathlib import Path


# Fixture for loading configuration
@pytest.fixture
def graphql_config():
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)
    return config


# Fixture for the GraphQL API URL
@pytest.fixture
def api_url(graphql_config):
    """

    :param graphql_config:
    :return:
    """
    return graphql_config["api_url"]


@pytest.fixture
def query_module():
    """
    :return:
    """
    return queries()


@pytest.fixture
def variable_module():
    """

    :return:
    """
    return variables()


def request_payload(query_module, variable_module):
    """
    Create the GraphQL request payload
    :param query_module:
    :param variable_module:
    :return:
    """
    request_load = {
        "query": query_module,
        "variables": variable_module
    }

    return request_load


def generate_allure_report():
    """
    Generate an Allure report from the allure-results directory.
    """
    current_directory = Path.cwd()
    allure_report_dir = current_directory / "allure-report"
    # Ensure the report directory exists
    if not allure_report_dir.exists():
        allure_report_dir.mkdir()

    # Generate the Allure report using the 'allure' command
    try:
        subprocess.check_call(["allure", "generate", "--clean", "allure-results", "-o", allure_report_dir])
    except subprocess.CalledProcessError as e:
        print("Error generating Allure report:", e)


def pytest_sessionfinish(session):
    # Generate Allure report after the test session
    generate_allure_report()
