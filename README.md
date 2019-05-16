1. 完成彩票竞猜系统

目录结构：
Lottery
- bin

start.py
- conf

settings.py
- core

src.py
- db
- lib

common.py
- log

功能分析：
1. 入口在start.py中
2. 主要的业务逻辑在src.py中
3. 配置信息在settings.py中
4. db下用shevle模块来存放中奖记录
5. 在common.py中完成共有功能
6. 在log下记录所有竞猜记录
	
细节点：
1. start.py中配置环境变量，并调用src中的入口run方法启动重新
2. settings.py中配置
- 配置环境变量BASE_DIR
- 配置日志文件路径LOG_PATH
- 配置中奖文件路径SHEVLE_PATH
- 配置Logging配置信息字典
3. common.py中实现
- 从settings.py中获取所需路径
- save_record功能：用log往log文件夹下的record.log记录竞猜记录
- get_logger功能：根据name提供logger
- save_win功能：用shevle模块存放中奖信息到db下的win.shv文件
4. src.py中实现
- 从settings.py中获取所需路径
- 从common.py中获取公用方法
- 提示用户选择玩法：0退出 1猜大小 2匹配三 3匹配五 其他输入错误，重输
- 猜大小：用户选择大或小，然后开奖，中奖与否都记录竞猜记录，中奖则记录中奖记录
- 匹配三：三个数字匹配，不要求顺序匹配，全对一等奖，对二二等奖，对一三等奖，记录规则同时
- 匹配五：三个数字匹配，设置五个奖项，规则同上
