# 目录结构
```
│   clansInformation.py
│   externs.py
│   fetch.py
│   formal.py
│   gettime.py
│   list.txt
│   main.py
│   main.spec
│   menu.py
│   operations.py
│   path.py
│   README.md
│   urls.py
```
# 项目实现说明
## 全局化
为了避免模块的循环导入，externs.py文件用于做一些全局化工作.path.py负责路径拼接
## 输入
input文件夹下为存入的部落信息,若需要修改则按已有格式修改字典.

urls.py文件存放需要用到的url.

main.py文件为程序入口,menu.py文件实现选择菜单,operations.py通过constant定义操作类型.gettime.py实现时间信息输入.
## 抓取
抓取的主体在fetch.py文件.
## 输出与格式化
文件的写入由fetch.py完成,输出与相关格式化由formal.py完成.