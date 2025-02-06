# 本项目主体已于2025-02-05正式完成所有开发,最后版本V1.1.2：[releases](https://github.com/Arshtyi/RoyaleAnalyze/releases "releases")
# 项目介绍
项目采用python3.12.7开发.
## 项目目的
本项目主要配合皇室战争部落管理及相关数据查询之用.
## 依赖项
项目主要依赖于[RoyaleAPI](https://royaleapi.com/ "RoyaleAPI")
# 功能实现
见[CHANGELOG.md](https://github.com/Arshtyi/RoyaleAnalyze/blob/main/CHANGELOG.md "更新日志")
# 关于项目
## 目录结构
```
│   .gitattributes
│   .gitignore
│   CHANGELOG.md
│   LICENSE
│   list.txt
│   README.md
│   走遍万罪星空.yml
│       
├───data
│   ├───input
│   │       clansInformation.xlsx
│   │       groupInformation.xlsx
│   │       
│   └───output
│           Information.xlsx
│           
├───logs
│       brower.log
│       
└───src
    │   clansInformation.py
    │   externs.py
    │   fetch.py
    │   formal.py
    │   gettime.py
    │   main.py
    │   menu.py
    │   operations.py
    │   path.py
    │   README.md
    │   urls.py
```
## 使用
确保所有依赖项正常且目录结构完整后运行`main.py`或者直接使用[releases](https://github.com/Arshtyi/RoyaleAnalyze/releases "releases")
## 输入
查询依据是`data/input/clansInformation.xlsx`，请确保目录结构完整、正确，若需要进一步的修改，请按已有格式修改.

特别地，格式化处理在输入退出选项后执行，请注意输入此指令，否则将导致格式化异常.
## 输出
文件默认输出为`data/output/Information.xlsx`，请注意执行退出指令以完成格式化.
# 家庭信息
[走遍万罪星空](https://github.com/Arshtyi/RoyaleAnalyze/blob/main/%E8%B5%B0%E9%81%8D%E4%B8%87%E7%BD%AA%E6%98%9F%E7%A9%BA.yml "家庭信息")
```yml
name: 走遍万罪星空
key: 走遍万罪星空
color: blue
emblem: Arrow_01
info:
  description: >
    中国人为主的部落，欢迎各方朋友加入，主要交流频道为QQ群：939160021
    A clan mainly composed of Chinese people, welcoming friends from all sides to join. The main communication channel is QQ group: 939160021
clans:
  - name: 零度轩辕
    tag: QRL0PYQL
  - name: 勾指起誓
    tag: R8RJYCCU
  - name: 啟明星之夢
    tag: GQPV9Y2R
```
# 联系我
QQ:640006128 或 3842004484

email:8956230x@gmail.com
# 我们的部落QQ群
939160021
# 截至2025-02-05,本项目主体已经完成全部开发工作,本项目也暂停新功能开发,日后仅会做一些BUG的修复工作