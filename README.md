# 项目介绍
项目采用python3.12.7开发.
## 项目目的
本项目主要配合皇室战争部落管理及相关数据查询之用.
## 依赖项
项目主要依赖于[RoyaleAPI](https://royaleapi.com/ "RoyaleAPI")

此外,请确保已安装依赖的所有第三库.所有自定义模板均有相关功能实现的注释.
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
├───data
│   ├───input
│   │       clansInformation.xlsx
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
## 请求头
为防止过多次请求，可以将请求头修改.
## 使用
确保所有依赖项正常且目录结构完整后运行`main.py`文件或者直接使用发行版.

## 可能存在的问题
一些可能出错的地方在于：
### 驱动拒绝访问
可能是因为C盘权限不足，请将权限升级
### 请求被拒
可能是请求过于频繁导致，可以尝试修改请求头
### 无法访问
部分功能默认使用了edge浏览器配置的驱动访问动态网页，可能需要作适当修改
### 无法访问到有效内容
可能是动态网页出错，可以尝试修改驱动项
## 输入
所有选项均有相关说明,此外，查询依据是`data/input/clansInformation.xlsx`，请确保目录结构完整、正确，若需要进一步的修改，请按已有格式修改.

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
# 关于更新
当前该项目处于个人开发阶段，如果你有任何好的想法或者想要加入开发，欢迎联系我！
# 联系我
QQ:640006128 或 3842004484

email:8956230x@gmail.com
# 我们的部落QQ群
939160021