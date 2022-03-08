class ScreenShotExtension:

    @staticmethod
    def take_screenshot(driver, file_name):
        driver.save_screenshot(file_name, False)


