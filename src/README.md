# 项目实现说明
## 输入
ClansInfor.py文件内为实现存入的部落标签,若需要修改则按格式修改字典original_clans.

urls.py文件存放需要用到的url.

main.py文件为程序入口,menu.py文件实现选择菜单,ops_defines.py通过constant定义操作类型,再由ops.py实现.
## 抓取
抓取的主体在fetch.py文件.
## 输出与格式化
文件的写入由fetch.py完成,输出与相关格式化由formal.py完成.