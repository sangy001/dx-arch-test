# ldap界面
ldap = '//span[contains(text(),"用户目录")]'  # LDAP 用户目录
ldap_add = '//*[@id="ldap-add"]'           # 接入用户目录
more = '//*[@id="more"]'                   # 更多操作
ldap_sync = '//*[@id="ldap-sync"]'         # 手动同步
ldap_edit = '//*[@id="ldap-edit"]'         # 编辑

# 接入ldap界面
ldap_address = '//*[@id="ldap-address"]'   # 服务器主机地址
ldap_username = '//*[@id="ldap-username"]'  # 用户名
ldap_password = '//*[@id="ldap-password"]'  # 密码
ldap_dn = '//*[@id="ldap-dn"]'             # 基准dn
ldap_filter = '//*[@id="ldap-filter"]'     # 对象过滤器

confirm = '//*[@id="confirm"]'   # 确定并连接
cancel = '//*[@id="cancel"]'               # 取消

no_ldap = '//div[contains(text(),"暂未接入")]'  # ldap暂未接入









