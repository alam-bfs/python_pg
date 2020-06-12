from oop.util.string_processor import *
from oop.page.login import Login
from oop.helper.api import get_status_code, get_resp_data


if __name__ == "__main__":
    StringProcessor = StringProcessor("car")
    Login = Login("Kaiser")
    print(StringProcessor.rev_string())
    print(Login.get_name())
    get_status_code()
    print(get_resp_data())

