# Kang GitHub README

> 先读懂仓库，再把 README 写成符合项目、证据和读者的公开介绍。

`kang-github-readme` 是由 **Kang** 创建并维护的 GitHub README 设计与审核 Skill。它既适合新仓库首次编写，也适合已有 README 的局部优化、事实审计和仓库展示一致性检查。

## 为什么需要它

很多 README 的问题不是 Markdown 写得不够多，而是没有回答读者最关心的问题：这是什么、对谁有用、能否运行、证据在哪里、下一步怎么做。固定模板又容易把每个项目写成同一种结构，甚至把本机状态、未验证能力或不必要的模块带进公开仓库。

这个 Skill 以仓库事实和读者任务为起点，动态选择信息结构，并在修改前给出足以判断质量的真实文案预览。

## 工作方式

1. 分阶段读取仓库根目录、现有 README、许可证、清单、命令、测试和可用素材。
2. 判断项目类型、目标读者、公开或私有模式、语言与证据强度。
3. 用 `verified / historical / to verify / do not publish` 区分事实。
4. 给出具有稳定编号的 `保留 / 改写 / 新增 / 删除` 预览。
5. 用户确认后锁定范围，只修改批准的条目。
6. 分别处理 README、视觉素材、GitHub 元数据和发布权限。

它不会强制所有仓库使用同一套章节，也不会因为“整体还能更好”而越过用户批准的局部范围。

## 你可以这样说

- “先分析这个 GitHub 项目，给我 README 结构和首屏文案预览。”
- “只优化 README 的简介，其他章节不要动。”
- “审计这个 README 里的命令、链接和功能声明，先不要修改文件。”
- “检查 README 和 GitHub Description、Topics 是否一致，分开给我建议。”
- “这是私有仓库，README 主要给内部团队交接使用。”

## 输出内容

根据任务范围，输出通常包括：

- 项目类型、读者、可见性、语言和证据判断；
- 代表性首屏文案与动态信息结构；
- 带稳定编号的保留、改写、新增、删除建议；
- 局部修改的范围锁定与范围外清单；
- 已验证事实、待核验内容和禁止公开内容；
- 修改后的文件、验证结果和仍未解决的证据缺口；
- 单独列出的视觉素材、GitHub 元数据和发布建议。

## 权限边界

以下四项互不自动授权：

1. 修改 README 或相关文档；
2. 创建、替换或上传视觉素材；
3. 修改 GitHub Description、Topics、主页等元数据；
4. 提交、创建 Pull Request、合并、发布或部署。

默认先预览。批准某个条目不代表批准整份方案，也不代表允许外部 GitHub 写入。

## 使用前提

- 需要能够读取目标仓库及其现有文档。
- 涉及运行命令、截图、外部链接或 GitHub 设置时，需要相应工具和权限；缺失时会明确降级并标记未验证。
- 公开仓库中的命令、版本、链接和能力声明应有当前证据支持。
- 私有仓库仍不得暴露密钥值、认证文件或不必要的个人信息。

公开源码：[KanG-ciyuan/kang-github-readme](https://github.com/KanG-ciyuan/kang-github-readme)

**Codex 安装已验证**：已从公开仓库 `main` 分支安装到 Codex 全局 Skill 目录，并通过包校验。`npx 安装尚未验证`，因此本仓库不把 `npx` 发现或安装写成已验证能力。

## 本地验证

```bash
python3 -m unittest discover -s tests -v
python3 scripts/trigger_eval.py --cases evals/trigger-cases.json --output reports/trigger-eval.json
python3 scripts/output_eval.py --cases evals/output-cases.json --output reports/output-eval.json
python3 scripts/validate_skill.py .
```

## 证据状态

当前已验证：

- 包结构、身份一致性和公开信息边界；
- 28 个确定性触发案例；
- 8 个 `recorded_fixture` 输出契约案例；
- 预览优先、范围锁定、私有仓库策略和分阶段检查规则。
- GitHub 公开仓库与 Pull Request 发布路径；
- 从公开仓库安装到 Codex 的全局安装路径。

当前未验证：

- 真实模型提供方的端到端调用表现；
- 人工盲评或用户偏好胜率；
- `npx` 发现与安装流程；
- GitHub Release；
- 相对其他公开 README Skill 的全面优势。

保存样例通过只证明规则结构符合预期，不等于真实模型质量或普遍审美提升。

## 常见问题

### 为什么不直接修改 README？

大幅重写和局部优化都默认先给代表性预览，避免方向错误后再返工。用户明确要求直接修改时，仍需确认具体写入范围。

### 只改简介时会顺便修其他章节吗？

不会。发现冲突时会生成新的建议编号，未经批准的章节保持不变。

### 外部链接无法访问怎么办？

本地链接继续检查，外部链接标记为未验证，不会假装已经完成全网校验。

### 可以处理私有仓库吗？

可以。内容会转向内部交接、所有权和支持路径，但密钥保护规则不会降低。

## 作者

Created and maintained by **Kang**.

## License

MIT License. Copyright (c) 2026 Kang.
