import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests against (chrome, firefox, edge)")
# This adds a custom command-line option --browser to pytest.
# action="store" tells pytest to store the value passed via --browser.
# default="chrome" means if no --browser is passed, it defaults to "chrome".
# help describes what the option does when using pytest --help.

@pytest.fixture()
def driver(request):
    browser = request.config.getoption("--browser").lower()
    
# request is a special object that gives access to command-line options.
# .getoption("--browser") fetches the value passed using --browser.
# .lower() ensures the value is lowercase for comparison.

    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        service = ChromeService()
        driver = webdriver.Chrome(service=service, options=options)
    
#If --browser=chrome, this block runs.
# ChromeOptions() lets you configure Chrome (like adding arguments).
# --start-maximized opens the window in full screen.
# ChromeService() initializes the service needed to start ChromeDriver.
# webdriver.Chrome() launches Chrome with the given options and service.

    elif browser == "firefox":
        options = FirefoxOptions()
        options.add_argument("--start-maximized")
        service = FirefoxService()
        driver = webdriver.Firefox(service=service, options=options)

    elif browser == "edge":
        options = EdgeOptions()
        options.add_argument("--start-maximized")
        service = EdgeService()
        driver = webdriver.Edge(service=service, options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    yield driver
    driver.quit()

"""As of Selenium v4.6.0, Selenium Manager was introduced — a built-in feature that:

🔍 Automatically downloads the correct browser driver (like ChromeDriver, EdgeDriver, GeckoDriver) for your browser version at runtime."""

"""When you write this:
driver = webdriver.Chrome(service=service, options=options)
You did not specify a path to chromedriver.exe.

Selenium internally detects:

The installed Chrome version

Downloads the matching chromedriver binary (usually to a temporary cache folder)

Launches the browser using that driver"""