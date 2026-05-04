# Awesome AI Agent Skills 中文精选

一个中文维护的 AI agent skills / coding workflow 精选清单。目标不是收录最多，而是帮你快速判断：**装什么、什么时候用、有什么风险**。

本仓库偏向“实际可安装、用途明确、公开维护信号较好”的项目。推荐等级来自公开 README、安装方式、维护活跃度、社区反馈和可复用程度的综合判断，不是客观排行榜。

## 快速推荐

| 你想解决的问题 | 优先看 | 为什么 |
| --- | --- | --- |
| 让 agent 写代码前先想清楚 | [obra/superpowers](https://github.com/obra/superpowers) | 完整的 brainstorming、计划、TDD、review 方法论 |
| 日常工程小技能，少而锋利 | [mattpocock/skills](https://github.com/mattpocock/skills) | grill-me、tdd、diagnose、to-prd 等高频技能很实用 |
| 团队工程流程沉淀 | [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin) | Brainstorm -> Plan -> Work -> Review -> Compound 的闭环清楚 |
| Next.js / React 前端质量 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | Vercel 官方 React/Next.js 性能和 UI 规则 |
| Supabase / Postgres | [supabase/agent-skills](https://github.com/supabase/agent-skills) | 官方 Supabase 和 Postgres best practices |
| Expo / React Native | [expo/skills](https://github.com/expo/skills)、[callstackincubator/agent-skills](https://github.com/callstackincubator/agent-skills) | 移动端官方/生态经验 |
| 营销、SEO、CRO、内容创作 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | SaaS 营销和增长任务覆盖完整 |
| 学习怎么写 skill | [openai/skills](https://github.com/openai/skills)、[anthropics/skills](https://github.com/anthropics/skills) | 官方参考、模板和复杂文档 skills |

## 安全提醒

第三方 skill 不是纯文本收藏夹。很多仓库会包含 `scripts/`、插件 manifest、安装脚本、自动更新、浏览器或部署能力。安装前至少检查：

- `SKILL.md` 的触发条件和具体指令。
- `scripts/`、`bin/`、`setup`、`package.json`、插件 manifest。
- 是否会修改 `CLAUDE.md`、`AGENTS.md`、`.codex/`、`.claude/` 或团队配置。
- 是否有 telemetry、自动更新、浏览器控制、部署、GitHub token、云服务 token 等权限。
- 是否适合项目级安装；不确定时先装到临时项目里试。

## 推荐等级

| 等级 | 含义 |
| --- | --- |
| `highly_recommended` | 值得优先试用，适用面广或技术栈内价值高 |
| `recommended` | 推荐按需安装，通常适合明确场景 |
| `situational` | 有明显价值，也有明显流程或权限成本 |
| `reference_only` | 更适合作为官方参考、模板或发现目录 |
| `caution` | 可以研究，但不建议无审查全量安装 |

## 完整工程工作流

### [obra/superpowers](https://github.com/obra/superpowers)

**推荐等级：** `highly_recommended`

**适合：** 多文件功能开发、TDD、系统化 debugging、code review、强制先计划再执行。

**安装：**

```text
/plugin install superpowers@claude-plugins-official
```

Codex App 可在 Plugins 侧边栏搜索 Superpowers；Gemini CLI 可用：

```bash
gemini extensions install https://github.com/obra/superpowers
```

**亮点：** 它是完整软件开发方法论，不只是 prompt pack。通过 brainstorming、worktree、TDD、review 等技能，把 agent 从“马上写代码”拉回到“先理解、再计划、再验证”。

**注意：** 对小任务偏重；团队采用前要确认 worktree、review 和分支习惯。

### [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin)

**推荐等级：** `highly_recommended`

**适合：** 团队工程流程、长期项目知识沉淀、计划/执行/review/复盘闭环。

**安装：**

```text
/plugin marketplace add EveryInc/compound-engineering-plugin
/plugin install compound-engineering
```

Codex 可用：

```bash
bunx @every-env/compound-plugin install compound-engineering --to codex
```

**亮点：** `Brainstorm -> Plan -> Work -> Review -> Compound -> Repeat` 的流程很清楚，重点是让每次工程工作都沉淀成下一次可复用的资产。

**注意：** 比单个 skill 重。团队如果不愿维护计划、review 和复盘记录，会觉得流程感过强。

### [garrytan/gstack](https://github.com/garrytan/gstack)

**推荐等级：** `situational`

**适合：** founder、技术负责人、Web 产品，需要 `/office-hours`、`/plan-eng-review`、`/review`、`/qa`、`/ship`、`/cso` 等多角色工作流。

**安装：**

```bash
git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git ~/.claude/skills/gstack
cd ~/.claude/skills/gstack
./setup
```

**亮点：** 产品、工程、设计、QA、安全、发布角色很完整，浏览器 QA 和 review 场景具体。

**注意：** 安装脚本和 team mode 较有侵入性。建议先个人试用 `/office-hours`、`/plan-eng-review`、`/review`、`/qa`，确认适合后再考虑团队模式。

## 单点工程 Skills

### [mattpocock/skills](https://github.com/mattpocock/skills)

**推荐等级：** `highly_recommended`

**适合：** 需求澄清、TDD、bug 诊断、PRD、issue、架构改进和 git guardrails。

**安装示例：**

```bash
npx skills@latest add mattpocock/skills/to-prd
```

**亮点：** 小、清楚、可组合。`grill-me`、`diagnose`、`tdd`、`to-prd` 这类技能非常适合作为日常默认工具。

**注意：** 这是个人技能目录，不是完整团队平台；建议按需安装，而不是默认全装。

### [softaworks/agent-toolkit](https://github.com/softaworks/agent-toolkit)

**推荐等级：** `recommended`

**适合：** README、架构图、依赖升级、session handoff、skill 质量检查、日常工程小工具。

**安装：**

```bash
npx skills add softaworks/agent-toolkit
```

Claude Code marketplace：

```text
/plugin marketplace add softaworks/agent-toolkit
```

**亮点：** 覆盖 development、documentation、planning、professional workflows，适合 cherry-pick。

**注意：** 不建议无脑全量安装；不同 skill、agent、command 的跨工具适配度不同。

## 技术栈专项

### [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills)

**推荐等级：** `highly_recommended`

**适合：** React、Next.js、UI code review、bundle size、data fetching、render 性能。

**安装：**

```bash
npx skills add vercel-labs/agent-skills
```

**亮点：** Vercel 官方维护，规则具体，比泛泛的“前端专家 persona”可靠得多。

**注意：** 技术栈相关性强。部署类 skill 涉及线上发布时，要确认账号和项目边界。

### [supabase/agent-skills](https://github.com/supabase/agent-skills)

**推荐等级：** `highly_recommended`

**适合：** Supabase Auth、RLS、SSR、Edge Functions、Realtime、Storage、Postgres query/index/RLS/connection pooling。

**安装：**

```bash
npx skills add supabase/agent-skills
npx skills add supabase/agent-skills --skill supabase-postgres-best-practices
```

**亮点：** 官方 Supabase 产品经验和 Postgres best practices，尤其适合 schema review、RLS 和性能问题。

**注意：** 不能替代生产数据库变更评审；迁移和权限变更一定要人工检查。

### [expo/skills](https://github.com/expo/skills)

**推荐等级：** `recommended`

**适合：** Expo 应用、EAS build、部署、debug、Expo Router、移动端 UI 和数据请求。

**安装：**

```text
/plugin marketplace add expo/skills
/plugin install expo
```

通用安装：

```bash
bunx skills add expo/skills
```

**亮点：** Expo 官方维护，适合 Expo 项目的构建、部署和调试。

**注意：** README 提到主要针对 Claude Code 和 Opus 模型调优；其他 agent 可用但需要项目内验证。

### [callstackincubator/agent-skills](https://github.com/callstackincubator/agent-skills)

**推荐等级：** `recommended`

**适合：** React Native 性能优化、升级、移动端 CI、GitHub Actions。

**安装示例：**

```bash
git clone https://github.com/callstackincubator/agent-skills.git
cp -r agent-skills/skills/* .codex/skills/
```

Gemini CLI：

```bash
gemini skills install https://github.com/callstackincubator/agent-skills.git
```

**亮点：** Callstack 生态经验，和 Expo 官方 skills 互补。

**注意：** incubator 仓库，具体 skill 要随 React Native 版本验证。

## 内容创作与营销

### [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills)

**推荐等级：** `recommended`

**适合：** SaaS 营销页、CRO、SEO、AI SEO、A/B test、cold email、launch strategy、growth engineering。

**安装：**

```bash
npx skills add coreyhaines31/marketingskills
npx skills add coreyhaines31/marketingskills --skill page-cro copywriting
```

Claude Code plugin：

```text
/plugin marketplace add coreyhaines31/marketingskills
/plugin install marketing-skills
```

**亮点：** 内容、SEO、转化率优化、增长工程覆盖完整，很适合技术创始人和技术营销。

**注意：** 输出要结合真实客户研究和品牌语气修订。市场、广告和 SEO 建议都有时效性。

## 官方参考

### [openai/skills](https://github.com/openai/skills)

**推荐等级：** `reference_only`

**适合：** 学习 Codex skills 结构，安装 OpenAI curated/experimental skills，参考官方实现。

**安装示例：**

```text
$skill-installer gh-address-comments
$skill-installer install https://github.com/openai/skills/tree/main/skills/.experimental/create-plan
```

**注意：** 单个 skill 的许可证可能在各自目录中；experimental skills 要额外验证。

### [anthropics/skills](https://github.com/anthropics/skills)

**推荐等级：** `reference_only`

**适合：** 学习 Agent Skills 规范、模板、document skills、Claude 平台 skills 使用方式。

**安装：**

```text
/plugin marketplace add anthropics/skills
/plugin install document-skills@anthropic-agent-skills
/plugin install example-skills@anthropic-agent-skills
```

**注意：** 部分 document skills 是 source-available，不全是开源；示例性质强，关键任务前要自己测试。

## 发现目录与谨慎参考

### [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills)

**推荐等级：** `reference_only`

大型发现目录，收录官方团队和社区 skills。适合按技术栈找候选，不建议把它当成已审计清单。

### [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills)

**推荐等级：** `caution`

覆盖面极广，工程、产品、营销、合规、C-level 都有。适合找灵感或挑单个 skill，不建议无审查全量安装。

### [daymade/claude-code-skills](https://github.com/daymade/claude-code-skills)

**推荐等级：** `situational`

包含 GitHub ops、Cloudflare troubleshooting、QA、promptfoo evaluation、Terraform、i18n 等专项技能。适合按需研究，公共反馈信号弱于官方技术栈仓库。

## 数据源

主要条目维护在 [`data/skills.yml`](data/skills.yml)。提交新条目前请运行：

```bash
python3 scripts/validate.py
```

## 收录原则

见 [`CONTRIBUTING.md`](CONTRIBUTING.md)。一句话版：公开、可安装、用途明确、有维护信号；谨慎对待安装脚本、自动更新和需要外部 token 的 skill。

## License

MIT. 见 [`LICENSE`](LICENSE)。
