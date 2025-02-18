"""
该模块定义了用于网络请求的头信息、代理设置以及项目相关的URL地址。
HEADERS:
    包含了用于HTTP请求的头信息,包括User-Agent和Content-Type。
proxies:
    定义了HTTP和HTTPS请求的代理设置,指向本地代理服务器。
url_0:
    RoyaleAPI的初始URL,用于构建其他相关URL。
url_repository:
    项目的GitHub仓库地址。
url_clan:
    部落信息的URL,基于初始URL构建。
url_player:
    玩家信息的URL,基于初始URL构建。
url_readme:
    项目README文件的URL,指向GitHub仓库中的README.md文件。
url_releases:
    项目发布版本的URL,指向GitHub仓库中的releases页面。
url_changelog:
    项目变更日志的URL,指向GitHub仓库中的CHANGELOG.md文件。
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
url_repository_2 = "https://github.com/Arshtyi/RoyaleAnalyze-2.0" #项目地址
"""
token urls
"""
url_clan = url_0 + "clan/" #部落url
url_player = url_0 + "player/" #玩家url
url_readme = url_repository + "/blob/main/assets/README.md" #readme地址
url_releases = url_repository + "/releases" #releases地址
url_changelog = url_repository + "/blob/main/CHANGELOG.md" #changelog地址