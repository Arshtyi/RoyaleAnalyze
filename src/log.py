"""
这是一个用于日志记录的模块，提供了灵活的日志记录功能，支持多种日志级别、彩色输出以及可选的日志文件写入功能。
该模块适用于整个项目 RoyaleAnalyze，用于记录和调试程序运行时的信息。
功能说明:
1. 支持的日志级别:
    - TRACE: 追踪信息，通常用于详细的调试信息。
    - INFO: 普通信息，表示程序正常运行的状态。
    - DEBUG: 调试信息，用于开发和调试阶段。
    - WARNING: 警告信息，提示可能的问题。
    - ERROR: 错误信息，表示程序运行中出现的问题。
    - CRITICAL: 严重错误信息，表示程序可能无法继续运行。
2. 彩色输出:
    - 使用 `colorama` 库为不同的日志级别提供不同的颜色，方便在终端中快速区分日志信息。
3. 日志文件写入:
    - 支持将日志信息写入指定的文件，便于后续分析和存档。
参数说明:
- `level` (str): 日志级别，表示当前日志的严重性。
- `module_name` (str): 模块名称，用于标识日志来源。
- `message` (str): 日志内容，描述具体的日志信息。
- `output_path` (str, 可选): 日志文件路径，如果提供，将日志写入该文件。
"""
from datetime import datetime
from colorama import Fore, Style

def log(level, module_name, message, output_path=None):
    # Define log levels and their corresponding colors
    level_colors = {
        'TRACE': Fore.CYAN,
        'INFO': Fore.GREEN,
        'DEBUG': Fore.BLUE,
        'WARNING': Fore.YELLOW,
        'ERROR': Fore.RED,
        'CRITICAL': Fore.MAGENTA
    }
    # Get the current time with milliseconds
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    # Format the log message
    log_message = f"[{current_time}] [{level}] [{module_name}]:  {message}"
    # Print the log message with color
    color = level_colors.get(level.upper(), Fore.WHITE)
    # print(color + log_message + Style.RESET_ALL)
    # Optionally write the log message to a file
    if output_path:
        with open(output_path, 'a', encoding='utf-8') as log_file:
            if output_path.strip():
                log_file.write(log_message + '\n')
    else:
        print(color + log_message + Style.RESET_ALL)