from mock import patch
from pysparkling import Context
from jobs.{{cookiecutter.job}} import analyze

@patch('jobs.{{cookiecutter.job}}.{{ cookiecutter.project.replace(' ', '').replace('-', '') }}Context.initalize_counter')
@patch('jobs.{{cookiecutter.job}}.{{ cookiecutter.project.replace(' ', '').replace('-', '') }}Context.inc_counter')
def test_{{cookiecutter.job}}_analyze(_, __):
    result = analyze(Context())
    assert len(result) == 327
