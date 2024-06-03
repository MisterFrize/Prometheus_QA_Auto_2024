import pytest

@pytest.mark.api
def test_user_exists(github_api):
    user_data = github_api.get_user("defunkt")
    assert user_data['login'] == 'defunkt'

@pytest.mark.api
def test_user_not_exists(github_api):
    user_data = github_api.get_user("butenkosergii")
    assert user_data['message'] == 'Not Found'

@pytest.mark.api
def test_repo_can_be_found(github_api):
    repo_data = github_api.search_repo("become-qa-auto")
    assert repo_data['total_count'] == 57  # Adjust this value as needed

@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    repo_data = github_api.search_repo("sergiibutenko_repo_non_exist")
    assert repo_data['total_count'] == 0

@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    repo_data = github_api.search_repo("s")
    assert repo_data['total_count'] != 0

@pytest.mark.api
def test_emojis(github_api):
    emojis = github_api.get_emojis()
    assert 'thumbsup' in emojis

@pytest.mark.api
def test_list_commits(github_api):
    commits = github_api.list_commits("octocat", "Hello-World")
    assert len(commits) > 0