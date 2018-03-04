# -*- coding: utf-8 -*-
# @Time     : 2018/2/2 0:56
# @Author   : ice
# @File     : __init__.py.py
# @Software : PyCharm
# coding: utf-8
# 主从配置
SQLALCHEMY_DATABASE_SLAVE_URI = {
    'master': 'mysql://mersea_w:LXn1O3niDl78whtN_W8Y1eA0GAGA4Pui@10.6.19.29:3482/mersea?charset=utf8mb4'
}

SQLALCHEMY_BINDS = {
    'ad_stats_bi': 'mysql://ad_stats_bi_r:DVVMp4ajRzcXRUZ_EHQBuocKrzThY2hF@10.8.52.137:3611/ad_stats_bi?charset=utf8mb4',
    'ad_data_r': 'mysql://addata_r:ARreBOEhw9MijIEN_eP6BYKOxkTikUnl@10.3.20.251:3417/ad_data?charset=utf8mb4',
    'qcc_data_r_05': 'mysql://qcc_data_r:dYabq1dy46q2p5NW_e3IArqv9viPyITy@10.3.20.201:3553/qcc_data?charset=utf8mb4',
    'qcc_data_r': 'mysql://cg_clue_u:smcNz6fF7uYCiGfU_t3Phfpr5izUZBGP@10.6.19.35:3310/cg_clue?charset=utf8mb4',
    'clue_crawler': 'mysql://clue_crawler_r:ZOugK0Flfw7lrmVE_Cj0bZPGxNfcFtOz@10.3.20.204:3553/clue_crawler?charset=utf8mb4',
    'ad_billing_r': 'mysql://adbilling_r:pBw5YGZggKpFbssn_fbCQlb8wEWdKqbk@10.6.16.187:3415/ad_billing?charset=utf8mb4',
}
MERSEA_REDIS_HOST = '10.3.23.27'
MERSEA_REDIS_PORT = 3702
MERSEA_REDIS_DB = 0

# mersea redis服务psm(测试环境不需要配置)
MERSEA_REDIS_PSM = 'toutiao.redis.mersea'


# CG_RD redis集群
# redis_conf.get_values(CG_REDIS_PROXY_CONFIG)
CG_REDIS_HOST = '10.3.32.82'
CG_REDIS_PORT = 3701
CG_REDIS_DB = 0

# Opportunity Order
OPPORTUNITY_ORDER_REDIS_PREFIX = 'mersea'

BPM_BASE_URL = 'https://bpm.bytedance.com'

# sms_service
SMS_SERVICE_URL = 'https://choiseul.bytedance.net/api/v1/callcenter/sms'
SMS_TOKEN = '4751094f4a083cdaef9d879256b8ad5a'

# Log
LOG_LEVEL = 'INFO'
log_format = "[%(category)s]-[%(server_ip)s]-[%(request_id)s-%(thread)d]-[%(asctime)s]-%(levelname)s-[%(pathname)s.%(funcName)s] %(message)s"


def generate_log_config(category='site'):
    category = 'mersea_' + category
    return {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'default': {
                'format': log_format
            },
        },
        'handlers': {
            'graylog2': {
                'level': LOG_LEVEL,
                'formatter': 'default',
                'class': 'graypy.GELFHandler',
                'host': '10.6.26.234',
                'debugging_fields': False,
                'facility': category,
                'filters': ['context_filter']
            },
            'time': {
                'level': LOG_LEVEL,
                'formatter': 'default',
                'class': 'cgutil.logging.handlers.CGTimedRotatingFileHandler',
                'when': 'MIDNIGHT',
                'backupCount': 7,
                'filename': '/var/log/tiger/%s.log' % category,
                'filters': ['context_filter']
            },
            'databus': {
                'level': LOG_LEVEL,
                'class': 'pyutil.databus.DatabusLogHandler',
                'channel': 'cg_app_log',
                'formatter': 'default',
                'filters': ['context_filter']
            },
            'event': {
                'level': LOG_LEVEL,
                'class': 'cgutil.logging.handlers.EventLogHandler',
                'app_id': 1258,
                'psm': 'cg.mersea.web',
                'formatter': 'json'
            }
        },
        'loggers': {
            'sqlalchemy.engine.base.Engine': {
                'handlers': []
            }
        },
        'root': {
            'handlers': ['sentry', 'graylog2', 'time', 'databus', 'event'],
            'level': LOG_LEVEL
        }
    }


LOG_CONFIG = generate_log_config()
PERFORMANCE_LOG_CONFIG = generate_log_config("performance")
CELERY_BEAT_LOG_CONFIG = generate_log_config('celery_beat')
SCRIPT_LOG_CONFIG = generate_log_config('script')
CELERY_LOG_CONFIG = generate_log_config('celery')
HANGUP_LOG_CONFIG = generate_log_config('hangup')

MAIL_AND_MSG_SEND = True

MAILS_SET = {'zhangruochen@bytedance.com', 'liumingliang@bytedance.com', 'adgrowth@bytedance.com',
             'wangyunhua@bytedance.com',
             'dingwei@bytedance.com', 'mashenglei@bytedance.com', 'licongxing@bytedance.com',
             'wangxu.02@bytedance.com', 'hongdeqiang@bytedance.com', 'wangmeng.02@bytedance.com',
             'huangting@bytedance.com', 'zhanghuishu@bytedance.com', 'lihui@bytedance.com',
             'wangyan.05@bytedance.com', 'lijie@bytedance.com', 'longguangyuan@bytedance.com',
             'renjixiang@bytedance.com', 'wangxiaoqin@bytedance.com', 'huangkai@bytedance.com'}

SQLALCHEMY_DATABASE_URI_R = 'mysql://mersea_r:TDuj0EGNH2sCx83G_VcySJnSJmOPvSgf@10.6.19.29:3483/mersea?charset=utf8mb4'

# 大权限系统
BSM_SERVICE_CLIENT_ID = 1
BSM_SERVICE_CLIENT_PWD = 'F668A0B53F1CCC0DAD5CCF2109A73A0476ABB275C3BE5C73'
BSM_SERVICE_DEBUG = False
BSM_SERVICE_PARAM = None

CALL_CENTER_SERVICE_NAME = 'cg.callcenter.rpc'
LOCAL_DEBUG = False

TOS_BUCKET = 'cg.mersea.storage'
TOS_ACCESS_TOKEN = '07QGWR4G3KOEK8HUUPX3'

ONLINE_ENV = True
# 添加redis key时请勿与此同名，或使用该名称为前缀
REDIS_SET_NAME = 'mersea_sales_active_analytics_today'

# 临时解决统计SQL超时问题
SQLALCHEMY_POOL_TIMEOUT = 30

APPS_BASE_DOMAIN = 'wings.bytedance.net'
APPS_BASE_URI = 'https://' + APPS_BASE_DOMAIN

ERROR_LOG_FREQUENCY = 5 * 60

# 商机公海认领 AB test online 开关
OPP_AB_TEST_TEST_ENV = False

# 站内信
PIGEON_BASE_URL = 'https://upstream-pigeon.bytedance.net'
