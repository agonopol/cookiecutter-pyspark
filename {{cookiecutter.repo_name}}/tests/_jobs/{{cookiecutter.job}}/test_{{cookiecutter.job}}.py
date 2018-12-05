from mock import patch
from pysparkling import Context
from jobs.{{cookiecutter.job}} import analyze

@patch('jobs.{{cookiecutter.job}}.{% cookiecutter.job.capitalize() %}Context.initalize_counter')
@patch('jobs.{{cookiecutter.job}}.{% cookiecutter.job.capitalize() %}JobContext.inc_counter')
def test_{{cookiecutter.job}}_analyze(_, __):
    result = analyze(Context())
    assert len(result) == 327
    assert result[:6] == [('ut', 17), ('eu', 16), ('vel', 14), ('nec', 14), ('quis', 12), ('vitae', 12)]
