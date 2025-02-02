import os
import pytest
from selenium import webdriver



def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="")

@pytest.fixture(scope='function')
def init_driver(request):
    # global driver
    browser = request.config.getoption("browser")
    if browser == 'chrome': 
            options = webdriver.ChromeOptions()
            # options.add_argument("--incognito")
            options.add_experimental_option('detach', True)
            driver = webdriver.Chrome(options=options)
    elif browser == 'ie':
        driver = webdriver.Firefox()
    else:
        raise Exception(f'Browser {browser} is not supported.')
    driver.maximize_window()
    pytest.driver = driver
    yield driver
    # driver.quit


# ------------------------------------------------HTML REPORT----------------------------------------------

def pytest_html_report_title(report):
    report.title = "TITLE!"


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.get_plugin('html')
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])

    if report.when == "call" or report.when == "setup":
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = '../reports/' + str(report.start) + '.jpeg'
            pytest.driver.get_screenshot_as_file(file_name)
            html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                   'onclick="window.open(this.src)" align="right"/></div>' % file_name
            extras.append(pytest_html.extras.html(html))
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