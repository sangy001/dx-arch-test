# 导航栏
user = '//*[@id="user"]'
# header_gear = '//*[@id="header-gear"]'
header_gear = '//div[@class="___dx-arch-header-toolbar-item-container"]'

user_manage = '//*[@id="user-manage"]'
portal_manage = '//*[@id="portal-manage"]'

# 创建用户界面
create_user = '//*[@id="user-create"]'  # 创建用户
username = '//*[@id="username"]'
lastname = '//*[@id="lastname"]'        # 姓
firstname = '//*[@id="firstname"]'      # 名
email = '//*[@id="email"]'              # 邮箱
password = '//*[@id="password"]'        # 密码
confirm_password = '//*[@id="confirm-password"]'   # 确认密码
confirm = '//*[@id="confirm"]'          # 确定
cancel = '//*[@id="cancel"]'            # 取消

# 用户详情界面
more = '//*[@id="more"]'         # 更多操作

delete = '//li[contains(text(),"删除")]'  # 删除操作
del_confirm = '//div[@class="delete-confirm-input"]//input'  # 删除确认框
del_button = '//div[@class="delete-confirm-btn-group"]//button[contains(text(),"删除")]'  # 删除确认按钮

disable = '//li[contains(text(),"禁用")]'   # 禁用
enable = '//*[@id="enable"]'     # 启用
# delete = '//*[@id="delete"]'     # 删除
userinfo_edit = '//*[@id="userinfo-edit"]'   # 用户信息编辑
password_edit = '//*[@id="password-edit"]'   # 密码编辑
roles_edit ='//*[@id="roles_edit"]'          # 角色编辑

# 角色编辑界面
roles_select = '//*[@id="roles-select"]'     # 角色
# 确定	confirm
# 取消	cancel

# 基本信息编辑界面
status = '//*[@id="status"]'       # 状态
# 姓	lastname
# 名	firstname
# 邮箱	email
# 确定	confirm
# 取消	cancel


# 安全界面
# 密码	password
# 确认密码	confirm-password
# 确定	confirm
# 取消	cancel
