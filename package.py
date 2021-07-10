from pycman.utils.common import datetime_format

package = {
    'name': 'Pycman',
    'version': '1.1.1',
    'author': 'singein',
    'email': 'singein@outlook.com',
    "scripts": {
        'commit': 'git add . && cz commit',
        'build': 'python setup.py bdist_wheel',
        'default': 'echo 请输入明确的命令名称',
        'tests': f'pytest tests -n=auto --html=test_reports/test-report-{datetime_format()}.html --self-contained-html'
    }
}
