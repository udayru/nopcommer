import pytest
from selenium import webdriver


@pytest.fixture()
def setup(brower):
    if brower == "firefox":
        driver = webdriver.Firefox(executable_path="/home/uk/browers/firefox/geckodriver")
        print("\n lunching firefox brower")
    elif brower == "chrom":
        driver = webdriver.chrom(executable_path="/home/uk/browers/firefox/geckodriver")
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def brower(request):
    return request.config.getoption("--browser")


def pytest_configure(config):
    config._metadata["project name"] = 'nop ecommers'
    config._metadata["module name"] = 'login'
    config._metadata["tester "] = 'uday'


@pytest.mark.optionlhook
def pytest_metadata(metadata):
    metadata.pop("Plugins", None)
