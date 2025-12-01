# MAGI系统 - EVA
## 副标题：基于多重人格理论的分布式AI决策平台

[![Project Status: Active](https://img.shields.io/badge/Project%20Status-Active-green.svg)](https://github.com/ewanqian/MAGI-System)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python Version: 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Framework: Flask](https://img.shields.io/badge/Framework-Flask-lightgrey.svg)](https://flask.palletsprojects.com/)
[![Documentation: Complete](https://img.shields.io/badge/Documentation-Complete-green.svg)](https://github.com/ewanqian/MAGI-System/blob/master/README.md)

## 项目愿景

MAGI System 是一个基于《新世纪福音战士》世界观的深度研究平台，旨在探索**人工智能本质**、**意识与存在**以及**人机协作未来**。

本项目的核心目标是构建一个超越传统AI范式的系统，融合多重人格理论、分布式决策架构和实时交互能力，能够在各种复杂场景下提供全面、深入的分析和决策支持。

## 与众不同之处

### 1. 基于多重人格理论的决策系统
MAGI系统将赤木直子的三种人格（科学家、母亲、女人）分别植入独立的决策模块中，使其能够模拟人类的多重身份思考模式，提供更全面、更人性化的决策支持。

### 2. 模块化可扩展的知识库系统
- **Obsidian原生支持**：直接使用Obsidian等笔记管理软件打开知识库，实现知识的可视化关联和探索
- **分层模块化设计**：知识库采用分层模块化结构，便于知识的组织、扩展和关联
- **跨学科知识整合**：整合哲学、人工智能学、计算机科学和认知科学等多学科知识
- **动态知识推理**：支持基于向量相似度的知识检索和基础的知识推理功能

### 3. 符合EVA世界观的沉浸式体验
- 忠实还原EVA中的MAGI系统设计
- 支持EVA风格的UI设计和交互效果
- 深度融入EVA世界观核心概念

### 4. 支持ACG项目开发的实验性平台
- 可作为游戏中的NPC决策系统
- 支持沉浸式体验开发
- 提供多媒体艺术装置的AI驱动

## 核心价值

- **跨学科研究平台**：整合哲学、人工智能学、计算机科学和认知科学
- **可扩展的知识库系统**：支持本地文档管理和Obsidian等工具集成，实现知识的可视化关联和探索
- **模块化架构设计**：支持未来的3D渲染、VR/AR集成和跨平台部署
- **ACG项目开发的实验性平台**：为ACG项目提供AI决策支持
- **开源协作生态**：欢迎全球研究者共同参与，推动AI研究的边界
- **多重人格决策机制**：基于赤木直子的三种人格，提供更全面、更人性化的决策支持
- **EVA世界观深度融入**：忠实还原EVA中的MAGI系统设计，提供沉浸式体验

## 项目简介

本项目模拟了《新世纪福音战士》中的MAGI超级计算机系统，实现了三个不同人格（Melchior、Balthasar、Casper）的决策逻辑，并提供了一个交互式Web界面，允许用户与MAGI系统进行对话。

MAGI系统由赤木直子博士开发，她将自己作为科学家、母亲和女人的三种人格分别植入三台超级电脑中，使其能够模拟人类的多重身份思考模式。

## 三个人格

- **Melchior**：科学家人格，基于赤木直子作为科学家的思维模式，注重逻辑和数据
- **Balthasar**：母亲人格，基于赤木直子作为母亲的思维模式，注重情感和生命价值
- **Casper**：女性人格，基于赤木直子作为女人的思维模式，注重效率和实际结果

## 项目结构

```
magi-system/
├── backend/          # 后端代码
│   ├── app.py        # Flask应用主文件
│   └── requirements.txt  # 依赖列表
├── frontend/         # 前端代码
│   └── index.html    # Web界面
├── knowledge/        # 知识库
│   ├── eva/             # EVA世界观知识
│   ├── philosophy/      # 哲学基础
│   ├── ai/              # 人工智能理论
│   ├── theory/          # 决策理论
│   ├── architecture/    # 系统架构
│   ├── multimedia/      # 多媒体集成
│   └── research/        # 相关研究
├── scripts/          # 脚本文件
│   └── start-magi.ps1  # 一键启动脚本
└── README.md         # 项目说明
```

## 技术栈

- **后端**：Python 3.8+、Flask、Ollama
- **前端**：HTML5、CSS3、JavaScript
- **知识库**：ChromaDB、Markdown
- **部署**：本地部署，支持一键启动

## 安装要求

- Python 3.8+
- Ollama（用于运行本地语言模型）
- 现代Web浏览器

## 快速开始

### 1. 安装Ollama

从[Ollama官网](https://ollama.com/)下载并安装Ollama，然后拉取所需模型：

```bash
ollama pull llama3
```

### 2. 启动MAGI系统

运行一键启动脚本：

```powershell
# 在项目根目录下
.\scripts\start-magi.ps1
```

### 3. 使用系统

脚本会自动打开Web浏览器，访问前端界面。您可以在聊天框中输入问题或指令，MAGI系统的三个人格会分别给出响应。

## 项目批评与改进方向

### 1. 人格差异化严重不足
**批判**：三个人格的对话几乎没有区别，科学家不像科学家，母亲不像母亲，女人不像女人。你说这是三个不同的人格？我看就是同一个AI换了个名字！
**改进方向**：为每个人格设计明确的价值体系和决策权重，科学家人格增加技术术语和数据引用，母亲人格强化情感表达和生命关怀，女人人格注重效率和实际结果。
**实现方案**：在prompt中明确指定每个人格的语言风格、常用词汇和决策优先级，使用不同的temperature参数调整随机性。

### 2. 世界观融入完全是摆设
**批判**：号称基于EVA世界观，但除了名字，完全感受不到EVA的氛围。你把问题换成任何其他主题，得到的回答都差不多，根本没有EVA核心概念的深度融入！
**改进方向**：将EVA核心概念（如AT力场、人类补完计划、使徒威胁）作为决策参数，影响三个人格的思考逻辑。
**实现方案**：在知识库中添加EVA核心概念的权重值，在生成响应时将这些概念作为上下文输入，确保响应符合EVA世界观。

### 3. 核心决策机制缺失
**批判**：MAGI系统的核心是三人格投票，但现在只是三个独立回答，根本没有投票和最终决策。你这是挂羊头卖狗肉！
**改进方向**：实现MAGI系统核心的三人格投票机制，根据不同场景的权重计算最终决策。
**实现方案**：为每个回答添加决策倾向标签（同意/反对/中立），根据场景重要性分配不同人格的权重，计算最终决策结果。

### 4. 前端UI徒有其表
**批判**：前端看起来像EVA，但交互体验极差。没有MAGI特有的界面元素，没有动态效果，没有声音反馈，完全没有沉浸感！
**改进方向**：添加EVA风格的动态效果、音效和交互反馈，增强MAGI系统的沉浸感。
**实现方案**：添加扫描线效果、数字雨动画、MAGI特有的字体和颜色方案，添加简单的音效反馈。

### 5. 知识库结构混乱
**批判**：知识库虽然分了目录，但内容组织混乱，知识之间没有关联，无法实现复杂的知识推理。你这就是把文件随便扔到不同文件夹里！
**改进方向**：优化知识库结构，添加知识之间的关联，实现基础的知识推理功能。
**实现方案**：使用Obsidian的链接功能关联不同主题的知识，添加知识图谱可视化，实现基于向量相似度的知识检索。

### 6. 交互方式单一至极
**批判**：只能通过文本输入，连个预设问题都没有。你这是2025年的AI应用？我看就是90年代的聊天室！
**改进方向**：添加预设问题库，支持语音输入，实现多模态交互。
**实现方案**：添加EVA主题的预设问题，集成Web Speech API支持语音输入，添加简单的图像识别功能。

### 7. 性能优化完全没有
**批判**：响应速度慢得离谱，每次提问都要等半天。你这是在测试用户的耐心吗？
**改进方向**：优化模型调用和响应生成速度，添加缓存机制。
**实现方案**：使用Ollama的streaming模式，实现响应的实时生成，添加常用问题的缓存机制，优化模型参数。

### 8. 代码质量惨不忍睹
**批判**：代码结构混乱，没有注释，没有模块化设计。你这是写一次性代码吗？
**改进方向**：重构代码，实现模块化设计，添加详细的注释和文档。
**实现方案**：将后端代码拆分为人格模块、知识库模块和API模块，添加详细的函数注释和API文档。

### 9. 测试保障为零
**批判**：没有任何测试，代码质量完全靠运气。你这是在拿用户当测试员吗？
**改进方向**：添加单元测试和集成测试，确保代码质量。
**实现方案**：使用pytest框架添加单元测试，测试核心功能，添加简单的集成测试，验证API的正确性。

### 10. 文档严重不足
**批判**：文档只有基本的使用说明，没有架构设计，没有API文档，没有开发指南。你这是想让别人怎么贡献？
**改进方向**：完善项目文档，包括架构设计、API文档和开发指南。
**实现方案**：使用Markdown编写详细的架构设计文档，使用Swagger生成API文档，添加开发环境搭建和贡献指南。

## 知识库系统

MAGI系统采用了模块化的知识库设计，支持多种知识来源的整合和关联：

### 知识库结构

知识库采用了分层模块化设计，便于知识的组织、关联和扩展：

- **eva/**：包含EVA世界观的核心知识，如基本设定、角色信息、使徒数据等
- **philosophy/**：哲学基础，包括人格分裂理论、人工智能伦理、数字存在主义等
- **ai/**：人工智能理论，包括多重代理系统、混合智能系统、涌现行为等
- **theory/**：决策理论，包括投票机制、共识算法、价值体系等
- **architecture/**：系统架构，包括服务导向架构、实时通信协议、事件驱动设计等
- **multimedia/**：多媒体集成，包括3D渲染、视觉效果、音频集成等
- **research/**：相关研究，包括历史案例、学术研究、艺术与科技融合等

### Obsidian集成

知识库支持Obsidian等笔记管理软件的直接使用，您可以：

- 使用Obsidian打开`knowledge`目录，直接浏览和编辑所有知识文件
- 利用Obsidian的链接功能关联不同主题的知识，构建知识网络
- 使用Obsidian的图表功能可视化知识关系，发现隐藏的关联
- 利用Obsidian的插件扩展功能，增强知识库的实用性
- 使用Obsidian的搜索功能快速定位所需知识

## 未来研究方向

### 1. AI Agent应用

- **自主AI Agent开发**：构建基于MAGI系统的自主AI Agent，支持多任务协作
- **决策支持Agent**：开发能够为复杂决策提供多视角分析的AI Agent
- **多Agent系统**：探索多个MAGI系统之间的协作与竞争机制
- **Agent社会模拟**：模拟基于MAGI架构的AI Agent社会，研究涌现行为

### 2. ACG项目开发

- **游戏NPC决策系统**：将MAGI系统作为游戏中的NPC决策核心，提供更真实的角色行为
- **沉浸式体验开发**：结合VR/AR技术，创建沉浸式的MAGI系统交互体验
- **动画制作辅助**：利用MAGI系统生成动画剧本和角色决策
- **虚拟偶像智能**：为虚拟偶像提供基于MAGI架构的智能决策支持
- **多媒体艺术装置**：开发基于MAGI系统的AI驱动多媒体艺术装置

### 3. 认知科学研究

- **多重人格决策模型**：研究人类多重身份下的决策机制，验证MAGI系统的合理性
- **意识涌现机制**：探索复杂系统中意识涌现的可能性
- **人机协作认知过程**：研究人类与MAGI系统协作时的认知过程
- **价值体系模拟**：模拟不同价值体系下的决策差异

### 4. 技术扩展

- **3D渲染与VR/AR集成**：实现基于WebGL或Unity/Unreal Engine的3D可视化
- **实时通信协议支持**：完善OSC、WebSocket、MQTT等实时通信协议的支持
- **边缘计算与分布式部署**：支持边缘设备部署和分布式计算
- **量子计算的潜在应用**：探索量子计算在MAGI系统中的应用可能性
- **区块链集成**：研究区块链技术在多Agent系统中的应用

## 实验性目的

MAGI系统的开发具有以下实验性目的：

1. **探索AI的新范式**：超越传统的单一AI模型，探索多重人格AI的可能性和优势
2. **研究人机协作新模式**：探索人类与AI协作决策的有效模式
3. **推动ACG内容创作创新**：为ACG项目提供新的创作工具和思路
4. **创新知识管理方式**：探索AI辅助的知识管理和关联方式
5. **研究未来交互体验**：研究未来沉浸式交互的可能性和实现方式
6. **验证复杂系统设计**：验证基于多重代理的复杂系统设计的可行性

## API接口

### POST /api/magi/ask

向MAGI系统提问，获取三个人格的响应。

**请求体**：
```json
{
  "query": "您的问题或指令"
}
```

**响应**：
```json
{
  "melchior": {
    "name": "Melchior",
    "role": "科学家",
    "response": "响应内容",
    "decision": "同意"
  },
  "balthasar": {
    "name": "Balthasar",
    "role": "母亲",
    "response": "响应内容",
    "decision": "反对"
  },
  "casper": {
    "name": "Casper",
    "role": "女性",
    "response": "响应内容",
    "decision": "同意"
  },
  "final_decision": "同意",
  "decision_reason": "基于科学家和女性人格的同意，母亲人格的反对，根据当前场景权重计算得出最终决策。"
}
```

### GET /api/magi/status

获取系统状态信息。

**响应**：
```json
{
  "status": "online",
  "personalities": [
    {
      "id": "melchior",
      "name": "Melchior",
      "role": "科学家"
    },
    {
      "id": "balthasar",
      "name": "Balthasar",
      "role": "母亲"
    },
    {
      "id": "casper",
      "name": "Casper",
      "role": "女性"
    }
  ],
  "knowledge_base_size": 15,
  "uptime": "2h 30m"
}
```

## 自定义配置

### 修改模型

在`backend/app.py`中修改使用的模型：

```python
response = ollama.generate(
    model="llama3",  # 这里可以替换为其他Ollama支持的模型
    prompt=full_prompt,
    stream=False
)
```

### 扩展知识库

在`knowledge`目录下添加新的Markdown文件，系统会自动使用这些知识来辅助决策。

## 开发说明

### 后端开发

1. 激活虚拟环境：
   ```powershell
   .\backend\.venv\Scripts\Activate.ps1
   ```

2. 安装依赖：
   ```powershell
   pip install -r .\backend\requirements.txt
   ```

3. 启动开发服务器：
   ```powershell
   python .\backend\app.py
   ```

### 前端开发

直接编辑`frontend/index.html`文件，刷新浏览器即可看到更改。

### 知识库开发

使用Markdown格式编写知识库内容，放置到相应的目录中。支持Obsidian等笔记管理软件的直接使用。

## 贡献与协作

我们欢迎全球研究者和开发者参与MAGI系统的开发和研究：

- 提交代码和功能建议
- 扩展知识库内容
- 参与跨学科研究
- 开发基于MAGI系统的应用
- 提供反馈和改进意见

## 技术路线图

### 短期目标（1-3个月）

1. 增强三个人格的差异化表现
2. 实现三人格投票决策机制
3. 深度融入EVA世界观核心概念
4. 添加EVA风格的动态效果和音效
5. 优化知识库结构和知识关联

### 中期目标（3-6个月）

1. 实现多模态交互（语音输入、图像识别）
2. 优化响应速度和性能
3. 重构代码，实现模块化设计
4. 添加单元测试和集成测试
5. 完善项目文档

### 长期目标（6-12个月）

1. 3D渲染与VR/AR集成
2. 游戏引擎集成
3. 移动应用开发
4. 分布式部署支持
5. 量子计算探索

## 许可证

MIT License

## 作者

ewanqian

## 致谢

- 《新世纪福音战士》动画及相关作品
- Ollama团队提供的本地语言模型支持
- Flask和ChromaDB等开源项目
- 哲学、人工智能和计算机科学领域的相关研究
- ACG文化社区的创意和灵感
- Obsidian团队提供的优秀笔记管理工具

---

# MAGI System - EVA (English Version)

## Project Vision

MAGI System is not just a simple simulation based on the Neon Genesis Evangelion worldview, but a deep research platform exploring the essence of artificial intelligence, consciousness and existence, and the future of human-computer collaboration.

Our goal is to build a system that transcends traditional AI paradigms, integrating multiple personality theory, distributed decision-making architecture, and real-time interaction capabilities to provide comprehensive, in-depth analysis and decision support in various complex scenarios.

## Core Values

- **Interdisciplinary Research Platform**: Integrating philosophy, artificial intelligence, computer science, and cognitive science
- **Extensible Knowledge Base System**: Supporting local document management and integration with tools like Obsidian
- **Modular Architecture Design**: Supporting future 3D rendering, VR/AR integration, and cross-platform deployment
- **Experimental Platform for ACG Project Development**: Providing AI decision support for ACG projects

## Project Introduction

This project simulates the MAGI supercomputer system from Neon Genesis Evangelion, implementing the decision-making logic of three distinct personalities (Melchior, Balthasar, Casper) and providing an interactive web interface that allows users to converse with the MAGI system.

The MAGI system was developed by Dr. Naoko Akagi, who implanted her three personalities as a scientist, mother, and woman into three supercomputers, enabling it to simulate human multi-identity thinking patterns.

## Quick Start

### 1. Install Ollama

Download and install Ollama from the [Ollama official website](https://ollama.com/), then pull the required model:

```bash
ollama pull llama3
```

### 2. Start the MAGI System

Run the one-click startup script:

```powershell
# In the project root directory
.\scripts\start-magi.ps1
```

### 3. Use the System

The script will automatically open a web browser to access the front-end interface. You can enter questions or commands in the chat box, and the three personalities of the MAGI system will each give responses.

---

# MAGIシステム - EVA (日本語版)

## プロジェクトビジョン

MAGIシステムは、「新世紀エヴァンゲリオン」の世界観に基づく単なるシミュレーションではなく、人工知能の本質、意識と存在、そして人間とコンピューターの協働の未来を探求するための深度研究プラットフォームです。

私たちの目標は、伝統的なAIパラダイムを超越したシステムを構築することです。多重人格理論、分散意思決定アーキテクチャ、リアルタイム対話機能を融合し、様々な複雑なシナリオで包括的かつ深い分析と意思決定支援を提供します。

## クイックスタート

### 1. Ollamaのインストール

[Ollama公式ウェブサイト](https://ollama.com/)からOllamaをダウンロードしてインストールし、必要なモデルを取得します：

```bash
ollama pull llama3
```

### 2. MAGIシステムの起動

ワンクリック起動スクリプトを実行します：

```powershell
# プロジェクトルートディレクトリで
.\scripts\start-magi.ps1
```

### 3. システムの使用

スクリプトは自動的にWebブラウザを開き、フロントエンドインターフェースにアクセスします。チャットボックスに質問やコマンドを入力すると、MAGIシステムの3つの人格がそれぞれ応答します。