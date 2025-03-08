import os
import pytest
from config.logger import setup_logging, logging
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
    pytest_html = item.config.pluginmanager.get_plugin('html')
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])
    logger = logging.getLogger(item.nodeid)

    if report.when == "call" or report.when == "setup":
        xfail = hasattr(report, "wasxfail")
        if report.passed:
            logger.info(f"Test {item.nodeid} PASSED")
        elif report.failed and not xfail:
            logger.error(f"Test {item.nodeid} FAILED")
            file_name = '../reports/' + str(report.start) + '.jpeg'
            pytest.driver.get_screenshot_as_file(file_name)
            html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                   'onclick="window.open(this.src)" align="right"/></div>' % file_name
            extras.append(pytest_html.extras.html(html))
        elif report.skipped:
            logger.warning(f"Test {item.nodeid} SKIPPED")
        report.extras = extras


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