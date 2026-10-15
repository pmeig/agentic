---
name: sonar-python
description: Only when asked (qa, front, back): SonarQube setup, coverage and exclusions of a Python module. Never load on your own.
---

# Sonar for Python (on request only)

Python runs in WSL through the `python` alias (see the `python` skill).

## Properties

- `sonar.projectKey`, `sonar.sourceEncoding=UTF-8`, `sonar.sources=src` (or the package folder), `sonar.tests=tests`,
  `sonar.test.inclusions=**/test_*.py,**/*_test.py`, `sonar.python.version=3.13`.
- Coverage: `pytest --cov=<package> --cov-report=xml:coverage.xml` (pytest-cov, `branch = true` in `pyproject.toml`) and
  `sonar.python.coverage.reportPaths=coverage.xml`; test report optional with `sonar.python.xunit.reportPath`.

## Out of the analysis

- Tests: `tests/**`, `**/conftest.py` in `sonar.coverage.exclusions` and `sonar.cpd.exclusions`.
- Without behavior (`sonar.coverage.exclusions`): `**/__init__.py`, `**/settings.py`, `**/config.py`, pydantic / dataclass models
  without validators, `**/migrations/**` (Alembic, Django), `**/schemas/**`, `**/main.py` bootstrap, generated clients.

## Monthly refresh

Last refreshed: 2026-10. At first use in a later month: re-check the sources, update only internet-derived guidance, keep user/project rules, update this date, report changes.
Sources: https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/languages/python/ ,
https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/test-coverage/python-test-coverage/ , https://pytest-cov.readthedocs.io/
