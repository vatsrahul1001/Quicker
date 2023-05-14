import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from TestData import EnvironmentDetails
from utilities.log import get_logger
from pytest_html_reporter import attach

logger = get_logger()

driver = None

"""This function enables this framework to take command line argument 
    example:
    we can specify --browser in below command line to provide browser as chrome,firefox or edge
    poetry run pytest  --html-report=./report/report.html  --capture sys --browser=firefox

    Parameters:
    browser 

    Returns:
    None

"""


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")


"""This is a pytest fixture this very intial point of execution, this can be called to prerform browser launch and return the
    driver method, also we can perform teardown in this with yield method
    
    example:
    We can all this fixture using like  this < @pytest.mark.usefixtures("setup")>
"""


@pytest.fixture()
def setup(request):
    global driver
    browser_name = request.config.getoption("browser")
    if browser_name == "chrome":
        chrome_options = Options()
        chrome_options.add_argument("--ignore-certificate-errors")
        driver = webdriver.Chrome(
            ChromeDriverManager().install(), options=chrome_options
        )
    elif browser_name.lower() == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browser_name.lower() == "edge":
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    logger.info(f"Starting Execution with {browser_name} browser")
    driver.get(EnvironmentDetails.BASE_URL)
    logger.info(f"opening {EnvironmentDetails.BASE_URL} webpage")
    driver.maximize_window()
    driver.implicitly_wait(5)
    request.cls.driver = driver
    yield
    attach(data=driver.get_screenshot_as_png())
    driver.close()
    driver.quit()
