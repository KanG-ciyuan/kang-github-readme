# Kang GitHub README

[English](README.md) | 简体中文

[![Status: Experimental](https://img.shields.io/badge/status-experimental-orange.svg)](#status)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

`kang-github-readme` 是一个 Agent Skill 包，用于创建、审计、重构和有选择地改进 GitHub 仓库的 README，以及围绕它的公开展示层——Description、Topics、主页和截图。它先预览、再落笔，并且以证据为准：分阶段读取仓库，把每一条实质性声明归入四态事实账本，用稳定的编号给出真实文案预览，最后只做你已经批准的最小改动。

有四件事互不自动授权：**README 修改、视觉素材、GitHub 元数据、Git 发布。**

本包是 Markdown + YAML + Python 的 Skill 包，不是一个应用。声明版本 `0.1.1`，采用 MIT 许可证。

## 为什么需要它

多数 README 的问题不是 Markdown 写得不够多，而是读者真正关心的问题没有被回答——这是什么、对谁有用、能不能跑起来、证据在哪里、下一步做什么；以及声明被反复复述成了事实，背后却什么都没有。常见的两种修法会让情况更糟：固定模板把同一套章节顺序盖到每个项目上；一句“优化一下 README”则悄悄改动了没人要求改的章节，甚至把本机状态、未验证能力或内部笔记带进公开仓库。

这个 Skill 改以仓库事实和读者任务为起点，按项目动态选择信息结构，并且在改动任何文件之前先给出足够真实的拟稿内容，让方向可以被审查。

本包用一句话说明自己的职责（`SKILL.md:14`）：

> Create or selectively improve repository-specific GitHub README content and related public presentation. Treat the README as a reader-facing project page, not a fixed template or a dump of internal instructions.

即：把 README 当作面向读者的项目页面，而不是固定模板，也不是内部说明的堆放处。

## 错误做法与正确做法

| 错误做法 | 使用本 Skill |
| --- | --- |
| 一次性重写整份 README，之后才发现方向不对 | 先给出真实拟稿的代表性预览；每条建议可接受、修改、推迟或拒绝 |
| “优化一下简介” 却顺手改掉了另外三个章节 | 范围锁定：批准某一条不等于批准相邻章节；未批准的章节列入 `Outside scope` |
| 能力声明写一次之后就被当作事实反复引用 | 每条实质性声明都带账本状态：`verified`、`historical`、`to verify` 或 `do not publish` |
| 把 README 的批准当成可以改 Topics 或直接提交的许可 | 四类授权相互独立；读取与提议本身不构成任何授权 |
| 文档里的命令、版本、链接慢慢和代码脱节 | 按范围核验命令、版本、本地链接与密钥暴露，未解决的缺口照实报告 |
| 用拼凑的截图暗示产品已经完成 | 缺失素材进入缺口清单；禁止伪造产品截图 |

## 工作方式

七个有序步骤（`SKILL.md:20-28`）：

1. 分阶段读取仓库——根目录文件、现有 README、许可证、清单、文档、测试、运行命令、发布记录、可用素材；宁可停下来明确写出证据缺口，也不做全量扫描。
2. 建立 `verified / historical / to verify / do not publish` 事实账本。
3. 在改动任何内容之前，给出带稳定编号的代表性预览。
4. 分别确认 README、素材、GitHub 元数据和发布这四类范围。
5. 把已接受的编号转化为显式范围锁定。
6. 做最小的、连贯的、已批准的改动，验证它，并报告仍未解决的缺口。
7. 只有在被单独要求时才发布；绝不直接向默认分支推送。

### 本包定义的三套标签

它们刻意彼此独立，不能互相替代。

| 标签集 | 取值 | 用途 |
| --- | --- | --- |
| 公开声明账本 | `verified` · `historical` · `to verify` · `do not publish` | 某句话是否可以公开陈述，以及以什么范围陈述 |
| 链接状态 | `verified` · `redirected` · `broken` · `unverified` | 外部链接检查的结果——或者诚实地表示没有检查 |
| 评估来源 | `recorded_fixture` · `provider_backed` · `human_reviewed` | 一个数字来自哪一类评估 |

本包**没有**表示“仅由合成数据支持”的标签：在声明维度上最接近的诚实状态是 `to verify`，在评估维度上是 `recorded_fixture`。

## 核心能力

| 能力 | 作用 | 定义位置 |
| --- | --- | --- |
| 按项目类型选结构 | 8 行分类矩阵（产品应用、视觉前端、CLI、库/SDK、API/服务、模板、Agent Skill、研究项目）决定模块，而不是套用模板 | [project-type-playbook.md](references/project-type-playbook.md) |
| 代表性预览 | 7 部分组成——分类、信息架构、首屏文案、编号建议、逐节前后对照文案、证据缺口、与 README 分开的元数据提案 | [readme-structure-playbook.md](references/readme-structure-playbook.md) |
| 稳定编号 | `P1 Preserve` · `R1 Rewrite` · `A1 Add` · `D1 Remove`，每条可接受、修改、推迟或拒绝，并在后续迭代中保持 | [readme-structure-playbook.md](references/readme-structure-playbook.md) |
| 范围锁定 | 已批准的编号变成显式锁定；未批准章节列入 `Outside scope`；别处的矛盾转化为新的建议编号 | `SKILL.md` · [readme-structure-playbook.md](references/readme-structure-playbook.md) |
| 事实账本 | 对公开声明做四态分类，每个状态都有明确的公开使用规则 | [evidence-and-claims.md](references/evidence-and-claims.md) |
| 链接分类 | 本地链接与图片路径确定性检查；外部链接标记为 `verified` / `redirected` / `broken` / `unverified` | [evidence-and-claims.md](references/evidence-and-claims.md) |
| GitHub 元数据提案 | 针对 Description、Topics、主页、社交预览给出建议，与 README 做矛盾检查，并单独走审批 | [github-metadata.md](references/github-metadata.md) |
| 公开 / 私有读者模式 | 公开仓库面向首次访问的外部读者；私有仓库面向内部交接与恢复路径，密钥管控不因此放松 | [project-type-playbook.md](references/project-type-playbook.md) |
| 增量模式 | 只改某个章节的请求，就只改该章节及其内部必要的直接修补 | [readme-structure-playbook.md](references/readme-structure-playbook.md) |
| 路由边界 | 端到端的 Skill 研究、创建、评估、打包、安装、治理与发布，路由给相应的 Meta Skill，本包不接管 | `SKILL.md` |

## 输出内容

一次运行会返回（`SKILL.md:46-48`、[skill-ir.json](reports/skill-ir.json)）：

- 项目/读者/可见性/语言的分类，以及当前最强的可用证据；
- 范围内声明的四态事实账本；
- 带编号 `P1` / `R1` / `A1` / `D1` 的代表性预览；
- 已批准的范围锁定与显式的 `Outside scope` 清单；
- 修改后的 README 内容、验证证据，以及仍未解决的缺口；
- 与 README 改动分开列出的素材、GitHub 元数据和发布建议。

**范围说明。** 本包中没有任何代码会写 README、生成截图或执行 GitHub API 写入。`scripts/` 下的三个脚本只产出评估报告和校验 JSON；README 文案是由 Agent 在你的批准下撰写的。

## 证据状态

本节所有内容均在仓库根目录下、Python 3.11.15 环境、commit `9a5ce32` 上实际执行。

### 实际运行了什么

```bash
PYTHONPATH=. python3 -m unittest discover -s tests -t tests -p 'test_*.py'
```

```text
.....................................................................
----------------------------------------------------------------------
Ran 18 tests in 0.027s

OK
[exit code: 0]
```

```bash
python3 scripts/validate_skill.py .
```

```json
{
  "ok": true,
  "failures": [],
  "warnings": []
}
```

上述两项测量均可针对当前版本复现。此前那份“要求中文优先 README、并要求写下未经验证的安装声明”的文档契约已被修复 —— 见[文档契约修复](#文档契约修复)。

```bash
python3 scripts/trigger_eval.py --cases evals/trigger-cases.json --output reports/trigger-eval.json
```

```json
{ "total": 28, "passed": 28, "false_positive": 0, "false_negative": 0 }
```

```bash
python3 scripts/output_eval.py --cases evals/output-cases.json --output reports/output-eval.json
```

```json
{ "evidence_type": "recorded_fixture", "provider_backed": false, "human_reviewed": false,
  "total": 8, "passed": 8, "failed": 0 }
```

两个评估脚本还各跑了一次，输出重定向到**仓库之外**的临时文件，再与已提交报告 `diff` 对比：结果与 [trigger-eval.json](reports/trigger-eval.json)、[output-eval.json](reports/output-eval.json) **逐字节一致**。已提交的数字可以从随包脚本和样例复现。

### 这些数字不能说明什么

**触发样例通过，不等于触发路由经过验证。** [trigger_eval.py](scripts/trigger_eval.py) 里的“分类器”是一个关键词匹配器：当文本同时命中 6 个固定主语词之一和 16 个动作词之一，且不含 15 个排除模式之一时，才返回真。28 条样例（14 正、14 负）与它自洽。用本仓库自己的 `classify()` 跑 8 条样例之外的、真实用户很可能会发的请求，结果是：

```text
False  README 太长了，帮我精简一下
False  帮我看看这个项目的 readme 有什么问题
False  优化一下这个仓库的介绍页
False  帮我把 GitHub 仓库首页的介绍改得更清楚
True   这个项目的 README 需要重写
True   Audit this repo's readme file
False  Add badges to the project README
False  帮我把项目的说明文档整理一下
```

8 条里有 6 条被挡在门外。`false_negative: 0` 只说明这 28 条手写样例，不能推广；而且样例中的负例全都不含那 6 个主语词，也就是说它们是被主语门槛挡掉的，与排除模式列表无关——把该列表整个绕开，结果依然是 28/28。

**输出样例是 `recorded_fixture`，不是模型评估。** [output_eval.py](scripts/output_eval.py) 对 [output-cases.json](evals/output-cases.json) 中保存的输出做大小写不敏感的子串断言（`required` 必须出现，`forbidden` 必须不出现）。`provider_backed: false`、`human_reviewed: false`：没有调用任何模型提供方，也没有人做过评审。保存样例通过，只说明这些记录下来的输出满足各自的文本规则，不是质量分数，也不是胜率。

**测试是包契约测试，不是行为测试套件。** [test_package_contract.py](tests/test_package_contract.py) 的 11 个测试里有 10 个是 `is_file()` 或字符串存在性断言。其中两个断言 `manifest.json` *写了* `verified`、README *包含*对应句子——把声明锁进文本并不构成对该声明的证据。只有 `test_package_validator_returns_clean_result` 会去执行另一个程序。另外两个测试文件确实执行了本仓库自己约 150 行的关键词/子串代码。**没有任何测试断言 README 质量、模型输出或安装声明。**

**没有 CI。** 没有 `.github/` 目录，没有 workflow，没有 pre-commit 配置，也没有声明依赖的清单文件。只有人手动运行时，测试才会跑。

<details>
<summary>两种<strong>不可用</strong>的命令写法</summary>

仓库没有 `tests/__init__.py`，因此常见写法会失败：

```text
$ python3 -m unittest discover -s tests -t .
ImportError: Start directory is not importable: '<repository root>/tests'
[exit code: 1]
```

测试模块从仓库根目录导入，所以直接运行单个文件也会失败：

```text
$ python3 tests/test_output_eval.py
ModuleNotFoundError: No module named 'scripts'
[exit code: 1]
```

可用写法就是上面用的那条（`-t tests` 加 `PYTHONPATH=.`）。在恰好装了 pytest 的环境里 `pytest tests/` 也能收集到 18 个测试，但本仓库没有在任何地方声明 pytest。

</details>

### 声明账本

本文档本身，用本包自己的四种状态分类。

| 陈述或内容类别 | 标签 | 依据 |
| --- | --- | --- |
| `kang-github-readme` 是 Kang 拥有的 Agent Skill 包，声明版本 `0.1.1`，MIT 许可 | `verified` | [SKILL.md](SKILL.md)、[manifest.json](manifest.json)、[LICENSE](LICENSE) |
| 它把公开声明分为 `verified` / `historical` / `to verify` / `do not publish` | `verified` | `SKILL.md:23`、[evidence-and-claims.md](references/evidence-and-claims.md) |
| 它在改动前预览带编号的 `P1` / `R1` / `A1` / `D1` 条目 | `verified` | `SKILL.md:32`、[readme-structure-playbook.md](references/readme-structure-playbook.md) |
| 批准某一条不等于批准相邻章节 | `verified` | `SKILL.md:34-36`、[readme-structure-playbook.md](references/readme-structure-playbook.md) |
| README 修改、素材、GitHub 元数据和发布是四个相互独立的授权范围 | `verified` | `SKILL.md:40`、[github-metadata.md](references/github-metadata.md)、[interface.yaml](agents/interface.yaml) |
| 上述 18 个测试、校验器和两个样例评估的实际结果 | `verified` | 本节中的命令 |
| README 是中文优先文档 | `historical` | 对本文件的上一版本成立；本版本为英文主干，配 [README.zh-CN.md](README.zh-CN.md) |
| 版本 `0.1.0` 曾作为 release 发布 | `historical` | commit `6e2f7d5`（`release: publish kang-github-readme v0.1.0`）；当前代码树声明 `0.1.1` |
| 本包于 2026-08-15 完成过一次 Codex 全局安装 | `to verify` | 仅有 [manifest.json](manifest.json) 与 [creation-handoff.md](reports/creation-handoff.md) 的自述；仓库内没有记录该过程的日志、输出或测试 |
| 触发样例证明请求路由正确 | `to verify` | 样例通过，但 8 条样例之外的请求里有 6 条被错误挡掉 |
| 模型质量、提供方实测或人工偏好表现 | 未作声明 | [output-eval.json](reports/output-eval.json) 中 `provider_backed: false`、`human_reviewed: false` |
| 作者本机安装状态、家目录路径、认证文件、通信记录、个人流程笔记 | `do not publish` | [evidence-and-claims.md](references/evidence-and-claims.md)；[validate_skill.py](scripts/validate_skill.py) 中的禁用短语清单 |
| 内部决策笔记与 Agent 工作流计划文档 | `do not publish` | [evidence-and-claims.md](references/evidence-and-claims.md) —— 见[仓库说明](#repository-notes) |

### 已知缺口

以下都属于 `to verify`，同时也是本包自己列出的缺口（[skill-ir.json](reports/skill-ir.json) 的 `missing_evidence`）：

- **安装。** `manifest.json` 声明 `installation.status: verified`，方法为 `codex-skill-installer`，`verified_on: 2026-08-15`。仓库里没有任何东西能复现这一点；守护测试只断言 README 中存在那句话。请把安装视为未经验证。本包不附带安装器，也未记录任何安装流程。
- **提供方实测、人工评审、盲评偏好、胜率、相对其他 README Skill 的优势。** 都没有做，也都未作声明。
- **`npx` 发现与安装。** 未验证，未记录，未声明。
- **外部链接。** 本仓库自身 URL 检查时返回 HTTP 200。下方同级仓库链接为 `NOT_TESTABLE`：在撰写环境中反复检查均超时，因此它们保持 `unverified`，而不是 `verified`。
- **GitHub Release。** 不存在——见 [Status](#status)。
- **生态一致性。** 本包尚未完全符合同级 `kang-meta-skill` 中的包校验器：它对本仓库返回 `ok: false`，含 4 项必需字段失败与若干警告，其中包括 `evals/trigger_cases.json missing`。原因是真实的命名分歧：本包使用连字符文件名（`evals/trigger-cases.json`、`evals/output-cases.json`），而同级仓库使用下划线。本文档按文件的真实名称引用它们。

### 本文件相对上一版本的更正

上一版本中有两条陈述被下调：

| 原陈述 | 本版本 |
| --- | --- |
| 加粗的中文“安装已验证”结论，且归入“当前已验证” | 改为 `to verify`：`manifest.json` 有声明，仓库内无处可复现。该结论原文已不再出现在本包的任何位置 |
| “28 个确定性触发案例”——归入“当前已验证” | 改为“28 条样例通过”，并披露关键词匹配器的内部机制与 8 条中 6 条被错挡的结果 |

这份清单记录的是对本文档本身的更正，不构成该 Skill 表现良好的证据：没有任何提供方实测或人工评估运行过。

### 文档契约修复

本文档的上一版已是英文主干，而本包自己的契约仍要求 `README.md` 必须是中文优先。这打破了三条断言：

- `tests/test_package_contract.py::test_readme_is_a_chinese_first_product_page` 要求 **`README.md` 中**出现 9 个中文字面标题，以及至少 4 行以 `- “` 开头的示例。
- `tests/test_package_contract.py::test_readme_records_verified_public_state` 要求 `README.md` 中出现一句声称安装已验证的中文原文 —— 而本仓库无法为它提供任何证据。
- `scripts/validate_skill.py` 同时强制上述两项，因此 `test_package_validator_returns_clean_result` 也随之失败。

那份契约有两处问题，其中只有一处与语言有关：

1. 它锁死了某个具体文件的语言，而不是断言文档本身的不变量。
2. **它要求一条未经验证的声明。** `manifest.json` 声明 `installation.status: verified`，但本包中没有任何安装记录。要求写下该声明的测试，只能靠把它写出来才能通过。

因此被修复的是契约，而不是把声明塞回去：

| 修复后的断言 | 它现在强制什么 |
| --- | --- |
| `test_readme_is_a_bilingual_cross_linked_pair` | 两份文档都存在且互相链接；各自用本语言承载面向读者的章节；四条随包调用示例在两份文档中都被呈现 |
| `test_verified_install_claim_requires_shipped_evidence` | `manifest.json` 把安装声明为 `verified`；本包**没有**任何安装证据；因此两份文档都必须带 `to verify` 标签，且绝不得复述该声明 |
| `test_readme_states_the_unverified_npx_route` | `npx` 链路与其验证状态一并记录 |

`validate_skill.py` 镜像同样三条规则，并把文档对的两个成员都列入 `REQUIRED_FILES`。

**针对本版本实测结果：** `Ran 18 tests` / `OK`，且 `validate_skill.py` 返回 `{"ok": true, "failures": [], "warnings": []}`。安装声明保持 `to verify`；那句无证据的原文在本包中已不复存在，连引用形式也不再出现。

## Status

- 声明版本 `0.1.1`，在 [manifest.json](manifest.json)、[SKILL.md](SKILL.md)、[skill-ir.json](reports/skill-ir.json) 中一致。
- `manifest.json` 声明 `maturity: production`，[validate_skill.py](scripts/validate_skill.py) 强制该字符串。这是本包自己声明的成熟度层级。
- 面向读者的状态是 **experimental**：`0.1.1` **没有任何 git tag，也没有任何 GitHub Release**。唯一自称 release 的 commit（`6e2f7d5`）发布的是 `0.1.0`；没有 `CHANGELOG`，也没有配置 CI。
- 因此本 README 不带 Release 徽章。指向 `/releases/latest` 的链接今天会 404。

## 你可以这样说

本包在 [interface.yaml](agents/interface.yaml) 中提供了四条自然语言调用示例：

- “先读这个仓库，给我一份 README 结构和首屏文案预览”
- “只优化 README 简介，其他章节不要动”
- “审计 README 里的命令、链接和能力声明，先不修改”
- “分开检查 README 和 GitHub Description、Topics，先只给建议”

同样四条也以 YAML 形式存放在 [interface.yaml](agents/interface.yaml)：

```yaml
examples:
  - "先读这个仓库，给我一份 README 结构和首屏文案预览"
  - "只优化 README 简介，其他章节不要动"
  - "审计 README 里的命令、链接和能力声明，先不修改"
  - "分开检查 README 和 GitHub Description、Topics，先只给建议"
```

针对这类请求返回的预览有七个部分（[readme-structure-playbook.md](references/readme-structure-playbook.md)）：分类、拟定的信息架构、首屏标题与简介、编号建议条目、逐节的前后对照文案、证据缺口，以及与 README 改动分开的元数据提案。仓库里没有附带任何一次真实运行的记录——预览的形状是文档化的，不是展示出来的。

唯一可以精确复现的产物是触发报告：

```bash
python3 scripts/trigger_eval.py --cases evals/trigger-cases.json --output reports/trigger-eval.json
```

## 适用与不适用

| 适用 | 不适用 |
| --- | --- |
| 为还没有 README 的仓库撰写第一版 | 普通 Markdown 编辑——改表格、改嵌套列表、改语法 |
| 审计现有 README 的命令、链接、版本和能力声明 | 广告、落地页或营销文案 |
| 端到端重构一份 README | 修代码、修测试失败、修部署错误 |
| 只改某个章节，例如只动简介 | 产品实现或部署调试 |
| 让 README、Description、Topics、主页保持一致 | 端到端的 Skill 研究、创建、评估、打包、安装、治理与发布——路由给相应的 Meta Skill |
| 私有仓库中用于内部交接与责任归属的 README | 把“私有仓库”当成放松密钥管控的理由 |

## 安全与人工边界

### 四类相互独立的授权

`SKILL.md:40`：

> README edits, asset changes, GitHub metadata changes, and Git publication are separate authorization scopes.

读取可见元数据和给出文案建议，本身不构成任何授权。在此之上：

1. README 相关文件修改——仅在具体条目被批准之后。
2. 创建、替换、生成或上传视觉素材。
3. 修改 GitHub Description、Topics、主页、社交预览或任何其他仓库设置。
4. Git 发布：commit、Pull Request、merge、release、deploy 或推送默认分支。

[github-metadata.md](references/github-metadata.md)：

> README approval does not authorize metadata changes. Metadata approval does not authorize asset upload, commit, Pull Request, merge, release, deploy, or default-branch push.

> Authentication or permission failure must leave the local deliverable intact and be reported as incomplete external state.

最后一句是整条边界的要点：失败的外部动作就停留在失败且可见的状态。它不会变成一句声明，也不会让你已经产出的本地交付物一起消失。默认工作流绝不直接向默认分支推送，发布只在被单独要求时发生。

### 反伪造与隐私

[evidence-and-claims.md](references/evidence-and-claims.md)：

> Repository names and old prose are leads, not proof. Do not invent commands, test results, compatibility, deployment state, adoption, production readiness, performance, or endorsement.

> Do not publish author-local installation state, backup rationale, home-directory paths, private correspondence, authentication files, raw environment content, or personal workflow notes.

[readme-structure-playbook.md](references/readme-structure-playbook.md)：

> Never fabricate a product screenshot or use unrelated art to imply product completeness.

[project-type-playbook.md](references/project-type-playbook.md)——私有可见性绝不放松密钥管控。

`SKILL.md:46-48` 收口：没有证据，就绝不声称发布、安装、提供方评估、人工偏好或普遍的 README 改进效果。

### 这条边界不是什么

它是给 Agent 的指导，不是运行时强制沙箱。它无法阻止 Agent 无视这些规则，本仓库也无法验证 Agent 是否遵守。唯一被机械执行的部分是 [validate_skill.py](scripts/validate_skill.py) 中的检查——禁用短语清单、疑似密钥值正则、作者身份检查和占位符检查——而这些也只在有人运行时才跑。

## 使用前提

- 一个 Python 3 解释器（标准库即可）。本包不声明也不需要任何第三方依赖，没有 `requirements.txt`，也没有 `pyproject.toml`。
- 一个克隆下来的仓库副本；本包没有安装器，也没有发布到任何包仓库。
- 不需要网络访问即可运行测试、验证器和两个 fixture 评测——三者都是纯本地、确定性的。

本节只描述本包自己能验证的前提。安装到某个具体 Agent 运行时的前提**没有**记录在本仓库中，见[证据状态](#证据状态)。

## 快速开始

本包没有安装器，没有 `requirements.txt`，没有 `pyproject.toml`，也没有发布到任何包仓库。克隆仓库后直接阅读 [SKILL.md](SKILL.md)；它路由到的参考文档在 `references/` 下。这里刻意不写安装到某个具体 Agent 运行时的步骤，因为本包既不附带安装器，也没有任何安装记录。

```bash
git clone https://github.com/KanG-ciyuan/kang-github-readme.git
cd kang-github-readme
```

按[证据状态](#证据状态)一节的方式验证本包。这些命令只需要一个 Python 3 解释器和标准库——本仓库没有声明也不需要任何第三方依赖：

```bash
PYTHONPATH=. python3 -m unittest discover -s tests -t tests -p 'test_*.py'
python3 scripts/validate_skill.py .
python3 scripts/trigger_eval.py --cases evals/trigger-cases.json --output reports/trigger-eval.json
python3 scripts/output_eval.py --cases evals/output-cases.json --output reports/output-eval.json
```

若要在不覆盖已提交报告的前提下确认其可复现，把 `--output` 指向仓库之外的临时文件，再对两个文件做 `diff`。

## 包结构

<details>
<summary>25 个已跟踪文件</summary>

| 路径 | 作用 |
| --- | --- |
| [SKILL.md](SKILL.md) | 唯一的 Skill 入口：frontmatter 身份，以及职责、路由边界、工作流、预览契约、范围锁定、权限边界、验证和输出契约 |
| [manifest.json](manifest.json) | 名称、版本、所有权、成熟度、安装与发布声明 |
| [agents/interface.yaml](agents/interface.yaml) | 展示名、默认提示词、四条自然语言示例、兼容性信息和四个权限范围 |
| [references/project-type-playbook.md](references/project-type-playbook.md) | 分阶段读取、8 行项目类型矩阵、读者与可见性、语言选择 |
| [references/readme-structure-playbook.md](references/readme-structure-playbook.md) | 动态模块、7 部分代表性预览、增量模式与范围锁定、视觉证据 |
| [references/evidence-and-claims.md](references/evidence-and-claims.md) | 事实账本、公开/私有内容、命令与版本、链接标签、评估标签 |
| [references/github-metadata.md](references/github-metadata.md) | Description/Topics/主页/社交预览的提议规则，以及分开写入的权限边界 |
| [evals/trigger-cases.json](evals/trigger-cases.json) | 28 条路由样例——14 正、14 负 |
| [evals/output-cases.json](evals/output-cases.json) | 8 条 `recorded_fixture` 样例，各带 `required[]` 与 `forbidden[]` 断言 |
| [scripts/validate_skill.py](scripts/validate_skill.py) | 包结构、身份、隐私、版本与 README 契约校验器，输出 JSON |
| [scripts/trigger_eval.py](scripts/trigger_eval.py) | 确定性关键词分类器与样例运行器 |
| [scripts/output_eval.py](scripts/output_eval.py) | 对记录输出做 required/forbidden 子串匹配 |
| [tests/test_package_contract.py](tests/test_package_contract.py) | 11 个包契约测试 |
| [tests/test_trigger_eval.py](tests/test_trigger_eval.py) | 3 个针对分类器及其样例集的测试 |
| [tests/test_output_eval.py](tests/test_output_eval.py) | 3 个针对子串匹配器的测试 |
| [reports/trigger-eval.json](reports/trigger-eval.json) | 已提交的触发结果，可逐字节复现 |
| [reports/output-eval.json](reports/output-eval.json) | 已提交的输出结果，自我标注为 `recorded_fixture` |
| [reports/skill-ir.json](reports/skill-ir.json) | 机器可读的包 IR，含 `missing_evidence` 清单 |
| [reports/creation-handoff.md](reports/creation-handoff.md) | 构建交接：已验证优势、设计优势、假设、缺失证据 |
| [reports/prior-art-research.md](reports/prior-art-research.md) | 先行技术调研记录，其中写明公开目录查询从未执行 |
| [docs/superpowers/specs/2026-08-15-kang-github-readme-design.md](docs/superpowers/specs/2026-08-15-kang-github-readme-design.md) | 已批准的设计规格（310 行） |
| [docs/superpowers/plans/2026-08-15-kang-github-readme-implementation.md](docs/superpowers/plans/2026-08-15-kang-github-readme-implementation.md) | 实施计划（506 行），含 35 个未勾选任务项 |
| [LICENSE](LICENSE) | MIT，Copyright (c) 2026 Kang |
| [.gitignore](.gitignore) | `.worktrees/`、`__pycache__/`、`*.pyc` |

</details>

<a id="repository-notes"></a>

### 仓库说明

<details>
<summary>公开仓库中保留的内部文档——标注出来，而不是藏起来</summary>

`docs/superpowers/**` 是 816 行内部设计与计划材料，其中计划文件含 35 个未勾选任务项，并嵌有 `0.1.1` 之前的版本片段。它们保留在仓库里，且**不是**产品文档。

按本包自己的规则，这类内容属于可疑的公开材料。[evidence-and-claims.md](references/evidence-and-claims.md) 把 `do not publish` 定义为包含“internal decision note”，而这份计划正是其中之一。移除或迁移它需要仓库所有者决策，超出 README 改动的范围，因此这里只做标注。该计划还引用了一个本包并未附带的 sub-skill。

同一维度上还有两点较小的说明：

- 公开仓库上存在一个未合并分支，它会添加一个指向 `/releases/latest` 的 Release 徽章。由于并不存在任何 release，该徽章会 404。本 README 刻意不加。
- `SKILL.md` 把预览条目称为“stable numbered items”，而实际编号带字母前缀（`P1` / `R1` / `A1` / `D1`）。上文表格以实际实现为准。

</details>

## 常见问题

**这个包会替我写 README 吗？**
不会。本包中的任何代码都不会写 README、生成截图或调用 GitHub 写接口。`scripts/` 里的三个脚本只产出评测报告和校验 JSON；README 文本由 Agent 在你的批准下撰写。

**为什么现在没有 GitHub Release？**
因为从未发布过。`0.1.1` 没有 git tag；唯一自称 release 的 commit（`6e2f7d5`）发布的是 `0.1.0`。因此本 README 不带 Release 徽章。

**安装是否已经验证？**
没有。`manifest.json` 声明 `installation.status: verified`，但本仓库中没有任何安装日志、记录或测试可以复现它。按本包自己的证据规则，该声明在面向读者的一侧标记为 `to verify`。

**为什么 `evals/` 用连字符文件名？**
本包使用 `evals/trigger-cases.json` 与 `evals/output-cases.json`，而同级包使用下划线。这是真实的命名分叉，也是本包未通过同级校验器的原因之一。文件按真实名称引用，未被重命名。

**测试能证明 README 质量吗？**
不能。测试是包契约检查：文件存在性与字符串存在性。没有任何测试断言 README 质量、模型输出或安装声明。

**触发用例通过，是否说明触发是准确的？**
不能这样推断。分类器是关键词匹配器，28 条用例与它自洽；但在 8 条用例之外的合理请求中，有 6 条被路由到别处。

## 作者

本包由 **Kang** 维护，[LICENSE](LICENSE) 中的版权主体同样是 **Kang**。

- GitHub：[KanG-ciyuan](https://github.com/KanG-ciyuan/)
- 仓库：<https://github.com/KanG-ciyuan/kang-github-readme>

本仓库未附带安装记录、评测抄本或作者联系方式以外的任何作者信息。此处不发布个人邮箱、住址目录或其他本机状态，这是本包自己的 `do not publish` 规则。

---

## 属于 Kang 开源 AI 体系

本项目是「面向企业 AI 转型、Agent 协作与 AI 原生产品交付的证据驱动体系」的一部分。

| 阶段 | 项目 | 作用 |
| --- | --- | --- |
| DISCOVER 发现 | [enterprise-ai-diagnostic-skills](https://github.com/KanG-ciyuan/enterprise-ai-diagnostic-skills) | 在自动化之前，先弄清企业真实业务如何运行 |
| DEFINE 定义 | [kang-product-architect](https://github.com/KanG-ciyuan/kang-product-architect) | 把模糊需求转化为可实施、可审查的产品契约 |
| DEFINE 定义 | [kang-enterprise-process-reviewer](https://github.com/KanG-ciyuan/kang-enterprise-process-reviewer) | 审查流程是否可执行、可追责、可恢复 |
| BUILD & COORDINATE 构建与协同 | [kang-agent-workforce](https://github.com/KanG-ciyuan/kang-agent-workforce) | 角色化的 Agent 数字员工团队与显式交接 |
| BUILD & COORDINATE 构建与协同 | [kang-agent-collab](https://github.com/KanG-ciyuan/kang-agent-collab) | Agent 协作与交接协议 |
| BUILD & COORDINATE 构建与协同 | [kang-frontend-standard](https://github.com/KanG-ciyuan/kang-frontend-standard) | AI 构建界面的前端质量标准 |
| VERIFY 验证 | [kang-b2b-ux-auditor](https://github.com/KanG-ciyuan/kang-b2b-ux-auditor) | 用户能否真正把工作做完 |
| VERIFY 验证 | [kang-product-acceptance-auditor](https://github.com/KanG-ciyuan/kang-product-acceptance-auditor) | AI 构建产品的独立验收 |
| DELIVER 交付 | [kang-github-readme](https://github.com/KanG-ciyuan/kang-github-readme) | 证据感知的 README 工程 |
| DELIVER 交付 | [kang-ppt-skill](https://github.com/KanG-ciyuan/kang-ppt-skill) | 证据感知的演示文稿设计 |

**横向基础设施：** [kang-meta-skill](https://github.com/KanG-ciyuan/kang-meta-skill) —
Skill 工程化、评估与发布治理。

**早期工作：** [ai-agent-rules](https://github.com/KanG-ciyuan/ai-agent-rules)、
[workflow-five-steps](https://github.com/KanG-ciyuan/workflow-five-steps)、
[renovation-agent](https://github.com/KanG-ciyuan/renovation-agent)。

阶段地图：

```text
发现 DISCOVER
企业 AI 诊断 Skills
        ↓
定义 DEFINE
Kang Product Architect
Kang Enterprise Process Reviewer
        ↓
构建与协同 BUILD & COORDINATE
Kang Agent Workforce
Kang Agent Collab
Kang Frontend Standard
        ↓
验证 VERIFY
Kang B2B UX Auditor
Kang Product Acceptance Auditor
        ↓
交付 DELIVER
Kang GitHub README
Kang PPT Skill
```

> 这是一张生态地图，不是严格的运行时流水线。各阶段描述的是项目所处的工作位置，
> 而不是强制的执行顺序。

## 开源许可证

本项目采用 [MIT License](LICENSE) 开源。
