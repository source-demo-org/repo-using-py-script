import requests
from config import GITHUB_USERNAME, GITHUB_TOKEN
 
def create_github_repo(repo_name, description="", private=True, auto_init=True, org_name=None):
    if org_name:
        url = f"https://api.github.com/orgs/{org_name}/repos"
    else:
        url = "https://api.github.com/user/repos"

    headers = {
        "Accept": "application/vnd.github+json"
    }
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": auto_init
    }
 
    response = requests.post(url, json=data, auth=(GITHUB_USERNAME, GITHUB_TOKEN))
 
    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully!")
        return response.json()
    else:
        print(f"Failed to create repository: {response.status_code} !!!")
        print("Error:", response.json())
        return None
 
if __name__ == "__main__":
    repo_name = "public-repo-created-via-script-in-org"
    description = "This repo was created using a Python script and GitHub API."
    create_github_repo(repo_name, description, private=False,org_name="source-demo-org")
 