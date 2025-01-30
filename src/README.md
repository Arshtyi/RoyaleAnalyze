# 目录结构
```
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
# 项目实现说明
## 全局化
为了避免模块的循环导入，`externs.py`文件用于做一些全局化工作.`path.py`负责路径拼接.
## 输入
`data/input/clansInformation.xlsx`为存入的部落信息,若需要修改则按已有格式修改.

`urls.py`文件存放需要用到的url与请求头.

`main.py`文件为程序入口,`menu.py`文件实现选择菜单,`operations.py`定义和获取操作.`gettime.py`实现时间信息输入.
## 抓取
抓取的主体在`fetch.py`文件.
## 输出与格式化
文件的写入由`fetch.py`完成,输出与相关格式化由`formal.py`完成.
# 其他事项
## 速度
部分功能需要访问动态网页，不可避免地会慢上许多.