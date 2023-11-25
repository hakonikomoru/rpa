from collections import OrderedDict


class BasePage:
    
    def __init__(self, driver=None, url=None):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def close(self):
        self.driver.quit()

    @staticmethod
    def write_to_file(path, output_arr, mode='w'):
        with open(path, mode=mode) as f:
            for text in output_arr:
                f.write(str(text) + "\n")

    @staticmethod
    def deduplicate_array(arr):
        return list(OrderedDict.fromkeys(arr))

    def append_to_file(self, path, merge_arr):
        self.write_to_file(path, merge_arr, mode='a')
