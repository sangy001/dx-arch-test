#
# from common import ArchAPI
# from functools import wraps
# from config.Config import Config
#
#
# obj = ArchAPI.ArchAPI()
# config = Config()
#
#
# # 判断参数是否存在
# """
# 保证config文件中的sso参数存在
# :return:
# """
#
#
# def confirm_client_info(func):
#     @wraps(func)
#     def confirm_client(*args, **kwargs):
#         if obj.judge_sso_exist(config.arch_test_client_uuid) is True:
#             return True
#         else:
#             obj.create_sso()
#         return func(*args, **kwargs)
#     return confirm_client
#
#
# def confirm_webhook_id(func):
#     @wraps(func)
#     def confirm_webhook(*args, **kwargs):
#         if obj.judge_webhook_exist(config.arch_test_webhook_id):
#             return True
#         else:
#             obj.create_webhook()
#         return func(*args, **kwargs)
#     return confirm_webhook
#
#
# def confirm_user_id(func):
#     @wraps(func)
#     def confirm_user(*args, **kwargs):
#         if obj.judge_user_exist(config.arch_test_user_id):
#             return True
#         else:
#             obj.create_user()
#             obj.set_password(config.arch_test_user_id)
#         return func(*args, **kwargs)
#     return confirm_user
#
#
# def confirm_ldap_id(func):
#     @wraps(func)
#     def confirm_ldap(*args, **kwargs):
#         if obj.judge_ldap_exist(config.arch_test_ldap_id):
#             return True
#         else:
#             obj.create_ldap()
#         return func(*args, **kwargs)
#     return confirm_ldap()
#
