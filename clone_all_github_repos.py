from dotenv import load_dotenv
import os
from github import Github

load_dotenv()

g = Github(os.getenv("GITHUB_ACCESS_TOKEN"))
folder_path = os.getenv("GITHUBREPOFOLDER")

def get_list_of_downloaded_repos():
    return os.listdir(folder_path)

def get_list_of_github_repos():
    list_of_repos = []
    for repo in g.get_user().get_repos():
        list_of_repos.append(repo.name)
    return list_of_repos

def repos_that_need_to_be_cloned():
    repos_to_be_cloned = []
    for repo in get_list_of_github_repos():
        if repo not in get_list_of_downloaded_repos():
            repos_to_be_cloned.append(repo)
    return repos_to_be_cloned

def get_repos_urls():
    list_of_repos = []
    for repo in g.get_user().get_repos():
        if repo.name in repos_that_need_to_be_cloned():
            list_of_repos.append(repo.clone_url)
    return list_of_repos

def clone_needed_repos():
    for url in get_repos_urls():
        command_to_execute = 'cd ' + str(folder_path) + ' && git clone '+ str(url)
        print("\n\n")
        print(command_to_execute)
        os.system(command_to_execute)


def test_functions():
    print(get_list_of_downloaded_repos())
    print("\n")
    print(get_list_of_github_repos())
    print("\n")
    print(repos_that_need_to_be_cloned())
    print("\n")
    print(get_repos_urls()) 

if __name__ == "__main__":
    #test_functions()
    clone_needed_repos()