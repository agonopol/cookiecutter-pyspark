{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
{% for _ in cookiecutter.project %}={% endfor %}
{{ cookiecutter.project }}
{% for _ in cookiecutter.project %}={% endfor %}

{% if is_open_source %}
.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.job }}.svg
        :target: https://pypi.python.org/pypi/{{ cookiecutter.job }}

.. image:: https://img.shields.io/travis/{{ cookiecutter.github_username }}/{{ cookiecutter.job }}.svg
        :target: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.job }}

.. image:: https://readthedocs.org/projects/{{ cookiecutter.job | replace("_", "-") }}/badge/?version=latest
        :target: https://{{ cookiecutter.job | replace("_", "-") }}.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status
{%- endif %}


{{ cookiecutter.description }}

{% if is_open_source %}
* Free software: {{ cookiecutter.open_source_license }}
* Documentation: https://{{ cookiecutter.job | replace("_", "-") }}.readthedocs.io.
{% endif %}

Features
--------

* TODO

Credits
-------

This package was created with Cookiecutter_ and the `agonopol/cookiecutter-pyspark`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`agonopol/cookiecutter-pyspark`: https://github.com/agonopol/cookiecutter-pyspark
