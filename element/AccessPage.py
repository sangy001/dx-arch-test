# SSO接入页面
sso = '//*[@id="sso"]'        # SSO接入
sso_create = '//*[@id="sso-create"]'  # 新增sso接入
sso_setting = '//*[@id="sso-setting"]'  # 设置
delete = '//*[@id="delete"]'    # 删除

# 创建sso页面
sso_client_id = '//*[@id="sso-client-id"]'  # 客户端id
confirm = '//*[@id="confirm"]'  # 确定
cancel = '//*[@id="cancel"]'    # 取消

# sso详情页面
guide = '//*[@id="guide"]'      # 接入指南
sso_info = '//*[@id="sso-info"]'  # 基本信息
webhook_info = '//*[@id="webhook-info"]'  # webhook
webhook_create = '//button[@class="dao-btn dao-btn--color-blue dao-btn--type-default dao-btn--size-md dao-btn--text-icon"]'  # 创建webhhok
more = '//*[@id="more"]'    # 更多操作

# 创建webhook页面
webhook_name = '//*[@id="webhook-name"]'  # 名称
webhook_obj = '//*[@id="webhook-obj"]'    # 对象
webhook_action = '//*[@id="webhook-action"]'    # 行为
webhook_url = '//*[@id="webhook-url"]'     # URL
webhook_method = '//*[@id="webhook-method"]'   # method

webhook_setting = '//td[@class="operation"]/div'  # 选择设置
webhook_del = '//li/span[contains(text(),"删除")]'  # 删除webhook
del_confrm = '//div[@class="delete-confirm-input"]//input'  # 删除输入框
del_button = '//div[@class="delete-confirm-btn-group"]//button[contains(text(),"删除")]'  # 删除确认按钮


