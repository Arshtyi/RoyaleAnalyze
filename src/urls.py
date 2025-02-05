"""
This module contains URL configurations and HTTP request settings for the RoyaleAnalyze project.
Constants:
    HEADERS (dict): HTTP headers used for making requests.
    proxies (dict): Proxy settings for HTTP and HTTPS requests.
    url_0 (str): Base URL for RoyaleAPI.
    url_repository (str): GitHub repository URL for the project.
    url_clan (str): URL for accessing clan information.
    url_player (str): URL for accessing player information.
    url_readme (str): URL for accessing the project's README file.
    url_releases (str): URL for accessing the project's releases page.

"""
"""
headers
"""
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
}
"""
proxies
"""
proxies = {
    'http': 'http://127.0.0.1:8080',
    'https': 'https://127.0.0.1:8080'
}
"""
original urls
"""
url_0 = "https://royaleapi.com/" #初始依赖url
url_repository = "https://github.com/Arshtyi/RoyaleAnalyze" #项目地址
"""
token urls
"""
url_clan = url_0 + "clan/" #部落url
url_player = url_0 + "player/" #玩家url
url_readme = url_repository + "/blob/main/README.md" #readme地址
url_releases = url_repository + "/releases" #releases地址
url_changelog = url_repository + "/blob/main/CHANGELOG.md" #changelog地址