---
title: "{{语言学习_Kotlin}}"
description: ""
author: ""
tags: 
categories:
  - ""
keywords:
  - ""
draft: true
layout: ""
date: 2025-04-01 20:12:17
lastmod: 2025-04-01 20:12:27
---

## kotlin 基础

## kotlin 协程

> [!cite]
> [一文看透 Kotlin 协程本质](https://blog.csdn.net/m0_37796683/article/details/119106967)
> [探秘Kotlin协程机制](https://www.geekailab.com/doc/as/book/docs/Part2/%E7%BA%BF%E7%A8%8B%E4%B8%8E%E7%BA%BF%E7%A8%8B%E6%B1%A0%E5%BC%80%E5%8F%91%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF/5.kotlin_coroutine.html)
> [深挖Kotlin协程原理：协程调度与挂起](https://zhuanlan.zhihu.com/p/556030328)

同步编程, 代码顺序执行, 代码块一个接一个的执行, 代码块之间没有交互, 也没有并发

异步编程, 代码块之间可以交互, 也可以并发执行, 代码块之间可以相互影响, 也可以相互等待

- 基于 Callback 的异步编程, 把耗时操作放在另外一个线程执行, 执行完后通过回调函数进行结果处理. 问题是会导致回调地狱, 代码可读性差, 维护成本高.
- 基于 Future 的异步编程, 通过 Future 对象来表示一个异步操作的结果, 可以在需要耗时操作结果的地方通过 Future 对象来获取异步操作的结果. 问题是 Future 对象的 get() 方法是阻塞的, 会导致线程阻塞, 影响性能.
- 基于 RxKotlin 的异步编程, 通过 Single 构建链式调用, 通过 subscribe() 方法来处理异步操作的结果. 问题是调用状态处理困难, 错误处理困难, 代码可读性差, 维护成本高.
- 基于协程的异步编程, 通过挂起和恢复让线程中处理异步结果数据的代码段, 非阻塞式挂起, 等待异步操作完成后恢复执行相应的代码段. 同时支持通过协程作用域来管理协程的生命周期, 通过挂起函数来实现异步操作, 通过协程上下文来传递协程的状态.

启动协程的代码可以分为三个部分: `CoroutineScope`(作用域), `launch | 其他`(执行器), `CoroutineContext`(调度环境), 常用的协程构建器有如下几个:

- `runBlocking(Dispatchers.Main){...}` 无作用域, 启动协程并阻塞当前线程等待结果, 直到协程执行完成, 返回结果.
- `GlobalScope.launch(Dispatchers.IO){...}` 启动全局协程执行任务，无需结果, 它会在新的线程中启动一个协程, 并立即返回一个 `Job` 对象. 通过 `Job` 对象可以取消协程, 也可以获取协程的运行状态.
- `lifecycle.coroutineScope.launch(Dispatchers.IO){...}` 启动局部作用域内的协程执行任务，无需结果, 它会在新的线程中启动一个协程, 并立即返回一个 `Job` 对象. 通过 `Job` 对象可以取消协程, 也可以获取协程的运行状态. 这个方法会自动绑定到生命周期, 当生命周期结束时, 协程会自动取消.
    - 类似的还包含 `viewLifecycleOwner.lifecycleScope.launch{...}`, `viewModelScope.launch` 等.
- `CoroutineScope(Dispatchers.IO).launch{...}` 启动局部作用域内的协程执行任务，无需结果, 它会在新的线程中启动一个协程, 并立即返回一个 `Job` 对象. 通过 `Job` 对象可以取消协程, 也可以获取协程的运行状态. 这个方法可以通过获取到的 `scope` 对象管理协程的生命周期.
- `launch(Dispatchers.IO){...}` 继承当前作用域, 启动协程执行任务, 只能在 `CoroutineScope` 内部使用, 也就是 `suspend` 函数内使用. 特点与上述类似.
- `async(Dispatchers.IO){...}` 继承当前作用域, 启动协程执行任务, 无需结果, 只能在 `CoroutineScope` 内部使用, 也就是 `suspend` 函数内使用. 它会在新的线程中启动一个协程, 并立即返回一个 `Deferred` 对象. 通过 `Deferred` 对象可以获取协程的运行状态, 也可以取消协程. 通过 `deferred.await()` 方法可以获取协程的结果. 这个方法会自动绑定到生命周期, 当生命周期结束时, 协程会自动取消.
- `withContext(Dispatchers.IO){...}` 继承当前作用域, 启动协程执行任务, 会挂起当前协程，等待协程返回的结果, 只能在 `CoroutineScope` 内部使用, 也就是 `suspend` 函数内使用.

kotlin 的协程实现方式是无栈协程, 类似于针对回调加了个语法糖的支持. 协程内所运行的 `suspend` 函数, 编译器会将执行过程分为多个 `Continuation` 协程体片段, 其内部承载了代码片段的上下文, 状态等信息, 然后利用状态机的方式来实现协程的挂起和恢复. 不同状态对应不同的 `Continuation` 协程体片段. 不过会根据上下文所需的线程类型判断是否要切换线程.

## kotlin Flow

> [!cite]
> [Kotlin协程之flow工作原理](https://juejin.cn/post/6966047022814232613)

冷流: `flow {emit(1), ...}`, 每次调用 `collect` 都会重新执行传入的 lambda 表达式, 也只在这时触发执行.
热流: `StateFlow`, 用于保存状态, 只要有订阅者, 发生数据变化(不能相同)就会通知所有订阅者.
热流: `SharedFlow`, 用于广播数据, 只要有订阅者, 发生数据变化(可以相同)就会通知所有订阅者. 还可以设置缓存大小, 以及是否重放.
