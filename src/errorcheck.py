"""
errorcheck 模块
该模块用于检查和修复项目中所需的各种路径,以确保程序能够正常运行。主要功能包括:
1. 检查部落信息表路径是否存在。
2. 检查玩家信息表路径是否存在。
3. 检查输出路径是否存在,并在不存在时尝试创建。
4. 检查 Contributions 日志路径是否存在,并在不存在时尝试创建。
5. 检查 Donations 日志路径是否存在,并在不存在时尝试创建。
6. 检查 Faults 日志路径是否存在,并在不存在时尝试创建。
7. 删除旧的 Faults 日志文件。
函数:
    pathCheckAndFix(): 检查并修复上述所有路径,确保程序能够正常运行。
异常处理:
    在尝试创建路径时,如果发生异常,将打印错误信息并终止程序运行。

"""
import src.path as path
import os
import src.log as log
import src.externs as externs
def pathCheckAndFix():
    flag = True
    if os.path.exists(path.log_path()):
        log.log("INFO", "ERRORCHECK", "程序日志路径检查正确...", )
        os.remove(path.log_path())
        log.log("INFO", "ERRORCHECK", "程序日志文件删除成功...", )
    else:
        log.log("ERROR", "ERRORCHECK", f"程序日志路径检查失败,路径应为:'{path.log_path()}'", )
        log.log("INFO", "ERRORCHECK", "尝试创建程序日志路径...", )
        try:
            os.makedirs(path.log_dir_path())
            with open(path.log_path(), 'w') as f:
                pass
            log.log("INFO", "ERRORCHECK", f"程序日志路径:'{path.log_path()}'创建成功...", externs.log_path)
        except Exception as e:
            log.log("CRITICAL", "ERRORCHECK", f"创建程序日志路径失败,这将导致程序无法正常运行", )
            log.log("CRITICAL", "ERRORCHECK", "基于上述错误,准备终止程序...", )
            log.log("CRITICAL", "ERRORCHECK", f"请在终止程序后尝试手动创建路径:'{path.log_path()}'", )
            flag = False
            return flag
    if os.path.exists(path.pathConcatenationForClansInformationTable()):
        log.log("INFO", "ERRORCHECK", "部落信息检查正确...", externs.log_path)
    else:
        log.log("CRITICAL", "ERRORCHECK", f"部落信息检查失败,路径应为:'{path.pathConcatenationForClansInformationTable()}',这将导致程序无法正常运行...", externs.log_path)
        log.log("CRITICAL", "ERRORCHECK", f"部落信息检查失败,路径应为:'{path.pathConcatenationForClansInformationTable()}',这将导致程序无法正常运行...", )
        log.log("CRITICAL", "ERRORCHECK", "基于上述错误,准备终止程序...", externs.log_path)
        log.log("CRITICAL", "ERRORCHECK", "基于上述错误,准备终止程序...", )
        flag = False
        return flag
    if os.path.exists(path.pathConcatenationForGroupPlayerInformationTable()):
        log.log("INFO", "ERRORCHECK", "玩家信息检查正确...", externs.log_path)
    else:
        log.log("WARNING", "ERRORCHECK", f"玩家信息检查失败,路径应为:'{path.pathConcatenationForGroupPlayerInformationTable()}',尽管这不会使得程序无法正常运行,但你将无法对玩家进行筛选", externs.log_path)
        log.log("WARNING", "ERRORCHECK", f"玩家信息检查失败,路径应为:'{path.pathConcatenationForGroupPlayerInformationTable()}',尽管这不会使得程序无法正常运行,但你将无法对玩家进行筛选", )
    if os.path.exists(path.pathConcatenationForOutputTableDir()):
        log.log("INFO", "ERRORCHECK", "输出路径检查正确...", externs.log_path)
    else:
        log.log("WARNING", "ERRORCHECK", f"输出路径检查失败,路径应为:'{path.pathConcatenationForOutputTableDir()}',尝试创建输出路径...", externs.log_path)
        try:
            os.makedirs(path.pathConcatenationForOutputTableDir())
            log.log("INFO", "ERRORCHECK", f"输出路径:'{path.pathConcatenationForOutputTableDir()}'创建成功...", externs.log_path)
        except Exception as e:
            log.log("CRITICAL", "ERRORCHECK", f"创建输出路径失败,这将导致程序无法正常运行", externs.log_path)
            log.log("CRITICAL", "ERRORCHECK", f"创建输出路径失败,这将导致程序无法正常运行", )
            log.log("CRITICAL", "ERRORCHECK", "基于上述错误,准备终止程序...", externs.log_path)
            log.log("CRITICAL", "ERRORCHECK", "基于上述错误,准备终止程序...", )
            log.log("CRITICAL", "ERRORCHECK", f"请在终止程序后尝试手动创建路径'{path.pathConcatenationForOutputTableDir()}'", externs.log_path)
            log.log("CRITICAL", "ERRORCHECK", f"请在终止程序后尝试手动创建路径'{path.pathConcatenationForOutputTableDir()}'", )
            flag = False
            return flag

    if os.path.exists(path.Contributionslog_path()):
        log.log("INFO", "ERRORCHECK", "Contributions日志路径检查正确...", externs.log_path)
    else:
        log.log("ERROR", "ERRORCHECK", f"Contributions日志路径检查失败,路径应为:'{path.Contributionslog_path()}'", externs.log_path)
        log.log("INFO", "ERRORCHECK", "尝试创建Contributions日志路径...", externs.log_path)
        try:
            os.makedirs(path.Contributionslog_path())
            log.log("INFO", "ERRORCHECK", f"Contributions日志路径:'{path.Contributionslog_path()}'创建成功...", externs.log_path)
        except Exception as e:
            log.log("CRITICAL", "ERRORCHECK", f"创建Contributions日志路径失败,这将导致程序无法正常运行", externs.log_path)
            log.log("CRITICAL", "ERRORCHECK", f"创建Contributions日志路径失败,这将导致程序无法正常运行", )
            log.log("CRITICAL", "ERRORCHECK", "基于上述错误,准备终止程序...", externs.log_path)
            log.log("CRITICAL", "ERRORCHECK", "基于上述错误,准备终止程序...", )
            log.log("CRITICAL", "ERRORCHECK", f"请在终止程序后尝试手动创建路径:'{path.Contributionslog_path()}'", externs.log_path)
            log.log("CRITICAL", "ERRORCHECK", f"请在终止程序后尝试手动创建路径:'{path.Contributionslog_path()}'", )
            flag = False
            return flag
    if os.path.exists(path.Donationslog_path()):
        log.log("INFO", "ERRORCHECK", "Donations日志路径检查正确...", externs.log_path)
    else:
        log.log("ERROR", "ERRORCHECK", f"Donations日志路径检查失败,路径应为:'{path.Donationslog_path()}'", externs.log_path)
        log.log("INFO", "ERRORCHECK", "尝试创建Donations日志路径...", externs.log_path)
        try:
            os.makedirs(path.Donationslog_path())
            log.log("INFO", "ERRORCHECK", f"Donations日志路径:'{path.Donationslog_path()}'创建成功...", externs.log_path)
        except Exception as e:
            log.log("CRITICAL", "ERRORCHECK", f"创建Donations日志路径失败,这将导致程序无法正常运行", externs.log_path)
            log.log("CRITICAL", "ERRORCHECK", f"创建Donations日志路径失败,这将导致程序无法正常运行", )
            log.log("CRITICAL", "ERRORCHECK", "基于上述错误,准备终止程序...", externs.log_path)
            log.log("CRITICAL", "ERRORCHECK", "基于上述错误,准备终止程序...", )
            log.log("CRITICAL", "ERRORCHECK", f"请在终止程序后尝试手动创建路径:'{path.Donationslog_path()}'", externs.log_path)
            log.log("CRITICAL", "ERRORCHECK", f"请在终止程序后尝试手动创建路径:'{path.Donationslog_path()}'", )
            flag = False
            return flag
    if os.path.exists(path.FaultsLogDir_path()):
        log.log("INFO", "ERRORCHECK", "Faults日志路径检查正确...", externs.log_path)
    else:
        log.log("ERROR", "ERRORCHECK", f"Faults日志路径检查失败,路径应为:'{path.FaultsLogDir_path()}'", externs.log_path)
        log.log("INFO", "ERRORCHECK", "尝试创建Faults日志路径...", externs.log_path)
        try:
            os.makedirs(path.FaultsLogDir_path())
            log.log("INFO", "ERRORCHECK", f"Faults日志路径:'{path.FaultsLogDir_path()}'创建成功...", externs.log_path)
        except Exception as e:
            log.log("CRITICAL", "ERRORCHECK", f"创建Faults日志路径失败,这将导致程序无法正常运行", externs.log_path)
            log.log("CRITICAL", "ERRORCHECK", f"创建Faults日志路径失败,这将导致程序无法正常运行", )
            log.log("CRITICAL", "ERRORCHECK", "基于上述错误,准备终止程序...", externs.log_path)
            log.log("CRITICAL", "ERRORCHECK", "基于上述错误,准备终止程序...", )
            log.log("CRITICAL", "ERRORCHECK", f"请在终止程序后尝试手动创建路径:'{path.FaultsLogDir_path()}'", externs.log_path)
            log.log("CRITICAL", "ERRORCHECK", f"请在终止程序后尝试手动创建路径:'{path.FaultsLogDir_path()}'", )
            flag = False
            return flag
    if os.path.exists(path.FaultsLog_path()):
        log.log("INFO", "ERRORCHECK", "Faults日志文件检查正确,准备删除...", externs.log_path)
        os.remove(path.FaultsLog_path())
        log.log("INFO", "ERRORCHECK", "Faults日志文件删除成功...", externs.log_path)