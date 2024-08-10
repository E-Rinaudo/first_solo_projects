#!/usr/bin/env python3

"""This module tests the 'RepositoryPlotter' class to ensure it works as expected."""

import pytest
from github_python_r_julia_repos import RepositoryPlotter as RP


@pytest.fixture(name="repo_plotter")
def repo_plotter_fixture() -> RP:
    """An instance of the class available to all tests."""
    repo_plotter = RP()
    return repo_plotter


def test_api_call_error(repo_plotter):
    """Test if the system exits after a RequestException error."""
    repo_plotter.langs_urls = {
        "Python": "api.foo.foo",
        "Julia": "api.foo2.foo",
        "R": "api.foo3.foo",
    }
    with pytest.raises(SystemExit):
        repo_plotter.main()


def test_status_code_is_200(repo_plotter, capsys):
    """Test if the status code of 200 is printed."""
    repo_plotter.main()
    out, err = capsys.readouterr()
    assert "Status code (Python): 200" in out
    assert "Status code (Julia): 200" in out
    assert "Status code (R): 200" in out


def test_pull_20_repositories(repo_plotter):
    """Test if the top 20 repositories are extracted for each language."""
    repo_plotter.main()

    total_repos = sum(len(repos) for repos in repo_plotter.repositories.values())
    assert total_repos == 60


def test_pull_repo_names_stars(repo_plotter):
    """Test if names links and stars of the three languages are stored correctly."""
    repo_plotter.main()

    # Assert the keys in repo_data are 6 ((Lang Repos Names + Lang Stars) * 3).
    total_keys = len(repo_plotter.repo_data.keys())
    assert total_keys == 6

    # Assert the total number of repo links and stars is 120 (40 per each language).
    total_names_stars = sum(
        len(names_stars) for names_stars in repo_plotter.repo_data.values()
    )
    assert total_names_stars == 120
