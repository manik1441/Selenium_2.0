class ENV:
    run_env = 'DEMO'
    browser = 'chrome'


class URL:
    DEMO = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'

    def url(self):
        return eval("URL." + ENV.run_env)


DEBUG_LOG = False