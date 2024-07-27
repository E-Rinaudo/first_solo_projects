import pytest
from github_python_r_julia_repos import RepositoryPlotter as RP


@pytest.fixture
def repo_plotter() -> RP:
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
        repo_plotter._make_api_call()


def test_status_code_is_200(repo_plotter, capsys):
    """Test if the status code of 200 is printed."""
    repo_plotter._make_api_call()
    out, err = capsys.readouterr()
    assert "Status code (Python): 200" in out
    assert "Status code (Julia): 200" in out
    assert "Status code (R): 200" in out


def test_pull_20_repositories(repo_plotter):
    """Test if the top 20 repositories are extracted for each language."""
    repo_plotter._make_api_call()
    total_repos = 0
    for lists in repo_plotter.repositories.values():
        for repo in lists:
            total_repos += 1

    assert total_repos == 60


def test__pull_repo_names_stars(repo_plotter):
    """Test if names links and stars of the three languages are stored correctly."""
    repo_plotter._make_api_call()

    # Assert the keys in repo_data are 6 ((Lang Repos Names + Lang Stars) * 3).
    total_keys = 0
    for key in repo_plotter.repo_data:
        total_keys += 1

    assert total_keys == 6

    # Assert the total number of repo links and stars is 120 (40 per each language).
    total_names_stars = 0
    for lists in repo_plotter.repo_data.values():
        for data in lists:
            total_names_stars += 1

    assert total_names_stars == 120
