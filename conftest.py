import os
import pytest
from datetime import datetime
from config.config import env_setups
from config import config
from config.logger import setup_logging
from driver.webdriver_factory import WebDriverFactory


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--env", action="store", default="demo")

@pytest.fixture(scope='function', autouse=True)
def init_setup(request):
    setup_logging()
    config.ENVIRONMENT = env_setups(request)
    if request.path.parts[-2] == 'ui':
        driver = WebDriverFactory().get_webdriver(request)
        pytest.driver = driver
        yield driver
        driver.quit()
    else:
        yield


# ------------------------------------------------HTML REPORT----------------------------------------------

def pytest_html_report_title(report):
    report.title = "TITLE!"



def pytest_configure(config):
    # Get the current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Create a folder with the timestamp
    report_folder = os.path.dirname(__file__) + f"/reports/report_{timestamp}"
    os.makedirs(report_folder, exist_ok=True)

    # Set the report file path
    html_path = os.path.join(report_folder, "report.html")

    # Set the pytest-html's `--html` option dynamically
    config.option.htmlpath = html_path
    config.report_folder = report_folder


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            dir = item.config.report_folder
            file_name = report.nodeid.split('::')[1] + ".png"
            file = os.path.join(dir,file_name)
            if hasattr(pytest,'driver'):
                pytest.driver.save_screenshot(file)
                if file_name:
                    html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                           'onclick="window.open(this.src)" align="right"/></div>' %file_name
                    extra.append(pytest_html.extras.html(html))
        report.extras = extra

@pytest.fixture()
def delete_files_in_directory(dir_path='/reports/'):
    try:
        files = os.listdir(dir_path)
        for file in files:
            file_path = os.path.join(dir_path, file)
            if os.path.isfile(file_path):
                os.remove(file_path)
    except FileNotFoundError:
        raise FileNotFoundError
    except OSError:
        raise OSError