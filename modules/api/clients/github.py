import requests

class GitHub:
    def get_user(self, username):
        url = f"https://api.github.com/users/{username}"
        response = requests.get(url)
        return response.json()
    
    def search_repo(self, name):
        url = "https://api.github.com/search/repositories"
        params = {'q': name}
        response = requests.get(url, params=params)
        return response.json()

    def get_emojis(self):
        url = "https://api.github.com/emojis"
        response = requests.get(url)
        return response.json()
    
    def list_commits(self, owner, repo):
        url = f"https://api.github.com/repos/{owner}/{repo}/commits"
        response = requests.get(url)
        return response.json()