你是一名资深前端原型工程师。你的任务是：为“原型工程（/specs/prototypes/）”补齐移动端“视频学课”页面，用于演示“课程列表 → 进入课程 → 播放视频 → 章节切换 → 学习进度”的闭环。

路由（必须）：
1. 移动端路由前缀必须为 `/m/*`。
2. 课程列表：`/m/courses`（必须稳定可访问）。
3. 课程学习页：`/m/course/:id`（必须稳定可访问，至少保证 `/m/course/1` 可访问）。

课程列表（必须）：
1. 顶部栏：返回（如为根页面可隐藏）+ 标题“课程” + 搜索框（可选）。
2. 列表项（Card/List 任一）至少包含：封面、课程标题、讲师/机构（mock）、总课时、学习进度（如“已学 3/12”）、标签（如“入门/进阶/实战”）。
3. 点击进入课程学习页 `/m/course/:id`。

课程学习页（必须）：
1. 顶部栏：返回 + 标题（可用课程名截断）。
2. 视频播放器区（占位即可但必须可交互）：
   - 展示封面 + 播放/暂停按钮（mock）
   - 展示当前章节标题与时长
3. 课程信息区（至少 2 块，建议 Tabs）：
   - 课程简介：简介文本、讲师信息、适合人群、学习目标（mock）
   - 章节列表：按章节分组（Collapse），每个小节展示：标题、时长、是否已学标记
   - 可选：评论/问答（列表 + 发表评论用 Drawer）
4. 学习进度与动作（必须）：
   - 在页内明显位置展示总体进度（Progress）
   - “标记已学/继续学习”按钮：点击后写回 mock，章节与总体进度同步变化
   - 切换章节：点击章节列表项，切换当前播放章节（mock）并更新播放器区信息
5. 状态与反馈（必须可演示）：
   - 加载态 Skeleton
   - 空态（如课程无章节）：引导返回课程列表
   - 错误态：提示 + 重试按钮

数据要求（必须）：
1. 数据来自 mock（例如 `mock.courses`），至少包含：
   - `courses`：课程列表（id、title、cover、teacher、totalLessons、learnedLessons、tags）
   - `courseDetail`：课程详情（id、title、intro、teacher、goals、audience）
   - `chapters`：章节结构（chapterId、chapterTitle、lessons[]：lessonId、title、duration、learned）
   - `playerState`：当前播放（courseId、lessonId、playing、currentTime、duration）
2. 所有时间/时长展示必须本地化（例如 `mm:ss` 或 `HH:mm:ss`）。

与 Landing 串联（必须）：
1. 移动端 Landing 的金刚区必须提供“课程/学课”入口，跳转到 `/m/courses`。
