import sys
import pexpect


def get_script_exe_dir_path():
    print(sys.path)


def get_platform():
    print(sys.platform)
    print(sys.version)


def get_list_of_files():
    child = pexpect.spawn('ls -l')
    child.expect(pexpect.EOF)
    output = child.before
    print(output)


if __name__ == '__main__':
    # get_platform()
    # get_script_exe_dir_path()
    get_list_of_files()
