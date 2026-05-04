# Contributing

感谢你帮这个清单变得更可靠。本仓库的目标是“精选可安装”，不是收录最多。

## 收录标准

候选项目需要同时满足：

- 有公开仓库或公开文档。
- 有明确安装方式，最好支持 `npx skills`、Claude Code plugin、Codex skill installer、Gemini CLI 或清晰的手动安装。
- 至少包含可复用的 `SKILL.md`、agent workflow、slash command、plugin 或等价资产。
- 用途明确，能说明适合什么场景、不适合什么场景。
- 有基本维护信号，例如近期提交、issue/PR 活动、官方团队维护、真实用户反馈或被多个目录引用。

优先收录：

- 官方技术栈团队维护的 skills。
- 能显著改善规划、TDD、debug、review、QA、发布、文档、内容创作等真实工作流的项目。
- 可 cherry-pick 的单点技能，而不是要求全量接管环境的仓库。
- 有清楚权限边界和安全说明的项目。

不收录或降级为谨慎参考：

- 只有一句 prompt，没有安装说明或结构化 skill 的项目。
- 大量 AI 批量生成、用途重复、缺少维护信号的项目。
- 安装脚本权限不透明，或默认执行高风险操作却没有说明的项目。
- 过度营销、效果承诺不可验证、把 star 数当作唯一质量证明的项目。
- 需要泄露 private token、浏览器 session 或生产凭据才能试用的项目。

## 推荐等级

- `highly_recommended`：值得优先试用，适用面广或技术栈内价值高。
- `recommended`：推荐按需安装，通常适合明确场景。
- `situational`：有明显价值，也有明显流程、权限或迁移成本。
- `reference_only`：适合作为官方参考、模板或发现目录。
- `caution`：可以研究，但不建议无审查全量安装。

## 如何添加条目

1. 在 `data/skills.yml` 添加一个条目。
2. 确保字段完整：`id`、`name`、`repo_url`、`category`、`recommendation`、`agents`、`install`、`best_for`、`avoid_when`、`highlights`、`cautions`、`evidence`、`license`、`last_checked`。
3. 如果这是首页精选项目，同步更新 `README.md` 对应分类。
4. 运行校验：

```bash
python3 scripts/validate.py
```

## 写作风格

- 用中文解释判断理由，保留英文项目名和关键术语。
- 避免夸张承诺，例如“必装”“最强”“100% 提升效率”。
- 明确写出“什么时候不要用”。
- 安装命令尽量引用官方 README；不确定时写“查看 README 按需安装”，不要编造命令。
- 对会运行脚本、改配置、自动更新、访问浏览器、访问云服务的项目，必须写 `cautions`。

## 安全检查清单

提交前请至少看一眼：

- `SKILL.md`
- `scripts/`、`bin/`、`setup`
- `package.json` 或类似依赖清单
- plugin manifest，例如 `.claude-plugin/`、`.codex-plugin/`
- 是否修改 `CLAUDE.md`、`AGENTS.md`、`.claude/`、`.codex/`
- 是否需要 token、cookies、浏览器 profile、部署权限

## 数据维护

`last_checked` 使用 `YYYY-MM-DD`。如果你只是修错别字，不需要更新；如果你重新检查了 README、安装命令、许可证或维护状态，请更新日期。
