import os
import pytest

from config.logger import setup_logging
from driver.webdriver_factory import WebDriverFactory


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="")

@pytest.fixture(scope='function', autouse=True)
def init_setup(request):
    setup_logging()
    if request.path.parts[-2] == 'ui':
        driver = WebDriverFactory().get_webdriver(request)
        pytest.driver = driver
        yield driver
        driver.quit()
    else:
        pass


# ------------------------------------------------HTML REPORT----------------------------------------------

def pytest_html_report_title(report):
    report.title = "TITLE!"

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            dir = os.path.dirname(__file__)+'\\reports\\'
            file_name = report.nodeid.split('::')[1] + ".png"
            file = os.path.join(dir,file_name)
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