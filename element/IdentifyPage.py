# idp界面
identity = '//*[@id="identity"]'          # 身份提供商
identity_add = '//*[@id="identity-add"]'  # 接入身份提供商

more = '//*[@id="more"]'    # 更多操作
delete = '//li[contains(text(),"删除")]'  # 删除操作
del_confirm = '//div[@class="delete-confirm-input"]//input'  # 删除确认框
del_button = '//div[@class="delete-confirm-btn-group"]//button[contains(text(),"删除")]'  # 删除确认按钮

# 创建idp界面
identity_name = '//*[@id="identity-name"]'  # 提供商名称
identity_auth = '//*[@id="identity-auth"]'  # 认证方法
identity_client_id = '//*[@id="identity-client-id"]'  # 客户端id
identity_client_secret = '//*[@id="identity-client-secret"]'  # 客户端密钥
quick_get = '//*[@id="quick-get"]'        # 一键获取
login_url = '//*[@id="login-url"]'        # 登录url
token_url = '//*[@id="token-url"]'        # token url
userinfo_url = '//*[@id="userinfo-url"]'  # 获取用户信息 URL
logout_url = '//*[@id="logout-url"]'      # 登出url
autolink = '//*[@id="autolink"]'          # 自动关联
confirm = '//*[@id="confirm"]'            # 确定按钮
cancel = '//*[@id="cancel"]'              # 取消

# wellknown_url界面
wellknown_url = '//*[@id="wellknown-url"]'  # Well_known URL

# get_confirm = '//*[@id="confirm"]'      # 确定
get_confirm = '//div[@class="quick-dialog-button-group"]/button[@id="confirm"]'
get_cancel = '//*[@id="cancel"]'        # 取消

no_idp = '//div[contains(text(),"暂未接入")]'  # idp暂未接入









