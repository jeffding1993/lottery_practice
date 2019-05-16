from conf import settings
import logging.config
import shelve


# - save_record功能：用log往log文件夹下的record.log记录竞猜记录
def save_record(name, msg):
    logger = get_logger(name)
    logger.info(msg)


# - get_logger功能：根据name提供logger
def get_logger(name):
    logging.config.dictConfig(settings.LOGGING_DIC)
    return logging.getLogger(name)


# - save_win功能：用shevle模块存放中奖信息到db下的win.shv文件
def save_win(name, msg):
    with shelve.open(settings.SHELVE_PATH, writeback=True) as shv_tool:
        res = []
        try:
            res = shv_tool[name]
        except KeyError:
            shv_tool[name] = [msg]
        res.append(msg)
