你是一名资深前端原型工程师。你的任务是：在“原型工程（/specs/prototypes/）”中补齐 Web 端的账号体系（非 SSO）相关页面与交互闭环，用于演示登录与账号管理能力（可使用 mock，无需真实鉴权）。

适用条件（命中则必须执行）：
- 需求未采用 SSO/OIDC/LDAP 等统一身份接入，且属于“本系统独立登录”形态

路由（必须稳定可访问）：
- 登录：`/login`
- 创建账号：`/signup`
- 忘记密码：`/forgot-password`
- 重置密码：`/reset-password`
- 修改密码：`/change-password`（从 `/profile` 或 Header 用户菜单进入；禁止挂左侧菜单）

页面与闭环（必须可演示）：
1. `/login`
   - 账号选择（Select 或 List，至少 3 个 mock 账号）
   - 密码输入（可 mock 校验）
   - 登录按钮
   - 链接：去创建账号、忘记密码
   - 登录成功后：建立 session mock，跳转到 `/` 或 `/landing`
2. `/signup`
   - 字段：账号/手机号/邮箱（按需求命中裁剪）、密码、确认密码
   - 校验：必填、密码复杂度、两次密码一致
   - 创建成功后：写入 mock 用户数据源，并可回到 `/login` 选择新账号登录
3. `/forgot-password`
   - 字段：手机号/邮箱其一（按需求命中裁剪）
   - 行为：发送验证码（mock）并进入下一步
4. `/reset-password`
   - 字段：验证码、新密码、确认密码
   - 校验：验证码格式、密码复杂度、两次一致
   - 成功后：提示“密码已重置”，跳转 `/login`
5. `/change-password`
   - 必须为“已登录可访问”的页面（未登录访问必须引导到 `/login`）
   - 字段：旧密码、新密码、确认密码
   - 成功后：强制退出（清空 session mock）并引导重新登录

会话与路由拦截（必须）：
- 必须实现 session mock（例如 `src/store/session` 或等价位置）
- 未登录访问任意业务页（除 auth 页面与允许公开的 `/landing` 以外）：必须跳转 `/login`
- Header Avatar 下拉必须提供：
  - 切换账号/切换角色（用于演示权限差异）
  - 修改密码入口（跳转 `/change-password`）
  - 退出登录（清空 session，跳转 `/login`）

Mock 数据要求（必须）：
- 用户数据结构至少包含：
  - `user_id`、`user_name`、`role_id/role_name`、`org_id/org_name`
  - `login_account`（用户名/手机号/邮箱之一或多项）
- 创建账号、重置密码、修改密码都必须写回 mock 数据源并可在 UI 上验证结果

体验与文案（必须）：
- 错误提示必须可见且可解释（中文文案）
- 登录/重置/修改密码等关键操作必须有成功提示（message/notification）
- 表单提交必须有 loading 状态与防重复提交
