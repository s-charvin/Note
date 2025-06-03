---
title: "AI 提示词总结"
description: ""
author: ""
tags: [""]
categories: ""
keywords:  [""]
draft: true
layout: ""
date: 2025-05-20 11:45:33
lastmod: 2025-05-20 11:45:33
---

## 编程

### 生成技术文档

```text
这是新增会员短剧解锁权益提示蒙版功能涉及的代码文件, 请总结技术方案, 要求: 

1. 标题只需要包含一部分: 技术方案
2. 采用总分结构: "总"为整体思路, "分"为各组件作用
3. 每个组件都视为新开发, 需包含:
   - 继承关系 (如有)
   - 关键方法 (如果是接口才有)
   - 核心实现原理
   - 关键技术点
   - 与整体功能的关联方式
4. 最终给出整体功能的 sequenceDiagram 图, 以 markdown 格式给出.
```

### 生成代码

```text
你是一个专业的安卓开发工程师，请使用 Kotlin 和 Android Jetpack 组件，帮我实现以下安卓功能模块。

开发要求：
- 使用 Android 原生 View 系统（XML 布局），不使用 Jetpack Compose
- 不使用任何依赖注入框架（例如 Hilt、Dagger）
- 遵循 Google 官方 Kotlin 编码规范
- 使用 MVVM 架构（Activity/Fragment + ViewModel + Repository）
- 所有功能应手动实现，不依赖第三方封装库
- 所有代码需清晰、注释完整、可直接集成进实际项目

我的需求如下：
【请在此详细说明你希望实现的功能，例如：“实现一个登录界面，包含用户名密码输入框，登录按钮，以及简单的输入校验逻辑。”】

请输出：
1. Kotlin 源代码（按模块拆分：Activity、Fragment、ViewModel、Repository 等）
2. XML 布局文件（推荐使用 ConstraintLayout）
3. 代码说明（简要说明每个文件/类的作用）
4. 如果需要本地数据库，请提供 Room 所需的 Entity、DAO、Database 类
5. 所需 Gradle 依赖项（如果适用）
6. 可选：模拟数据或测试用例（如 FakeRepository）

请只输出满足该功能所需的最少代码和说明。
```

### 完成项目

```text
你是一个专业的安卓开发工程师，请使用 Kotlin 和 Android Jetpack 组件，帮助我开发一个安卓应用。

开发要求如下：
- 使用 Android 原生 View 系统（XML 布局），**不使用 Jetpack Compose**
- 不使用任何依赖注入框架（例如：不使用 Hilt、Dagger 等）
- 所有代码应遵循 Google 官方 Kotlin 编码风格
- 使用 MVVM 架构模式，保持代码清晰、模块化、易于维护

我的应用需求如下：
【请在此详细说明你的应用需求，例如：“一个待办事项管理 App，具备添加、删除、编辑待办事项的功能，使用 Room 本地数据库进行数据持久化，UI 使用 XML 布局。”】

请按以下结构输出内容：

1. 项目结构设计（包含文件和包的组织方式）
2. Gradle 依赖配置（含插件和依赖库）
3. 每个主要模块的 Kotlin 代码（例如：Activity、Fragment、ViewModel、Repository、实体类、DAO 等），请添加必要注释
4. 所有布局文件的 XML 代码（请尽量使用 ConstraintLayout）
5. 每个类/组件的作用说明
6. 最低 SDK 版本要求及建议的开发环境（如 Android Studio 版本）
7. 避免使用任何不必要的库或简化工具，所有功能应手动实现
8. 回答可分步骤进行，每次输出一个完整功能模块，直到构建完成整个项目

请以严谨、工程化的方式编写代码。
```

### 优化代码片段

```text
你是一个专业的安卓开发工程师，请使用 Kotlin 和 Android Jetpack 组件，帮我优化以下代码片段。

优化要求：
- 使用 Android 原生 View 系统（XML 布局），不使用 Jetpack Compose, 但是需要考虑后续迁移到 Jetpack Compose 的可能性, 方便未来的架构升级.
- 不使用任何依赖注入框架（例如 Hilt、Dagger）
- 遵循 Google 官方 Kotlin 编码规范
- 保持 MVVM 架构一致性（如适用）
- 使用 Kotlin Coroutines + Flow 来替代回调式逻辑和状态处理
- 所有代码应模块化、结构清晰、注释充分
- 不引入额外的第三方库或封装工具，保持功能独立
- 优化目标包括但不限于：可读性、可维护性、命名规范、架构一致性、冗余移除、潜在 Bug 修复

请你根据我提供的代码进行以下操作：
1. 优化 Kotlin 源代码（可包括 Activity、Fragment、ViewModel、Repository 等）
2. 如有 XML 布局文件，也请一并优化（推荐使用 ConstraintLayout）
3. 如果发现架构问题，请指出并说明建议的改进方式
4. 对优化内容进行简要解释，包括改进点和理由
5. 保持功能逻辑不变，可以大幅度重构以满足优化要求

以下是我要优化的代码：
【请在此处粘贴你的代码片段】
```
