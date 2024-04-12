---
title: "{{ZIKRouter}}"
description: ""
author: ""
tags: 
categories:
  - ""
keywords:
  - ""
draft: true
layout: ""
date: 2024-04-12 10:28:59
lastmod: 2024-04-12 12:12:34
---
ZIKRouter 进行模块间通信和依赖管理的过程.

SourceModule <- Router <- DestinationModule

依赖注入

源模块有时会需要某些对象的功能或服务才能完成其内部任务。通常情况下，源模块不会直接创建它所需要的依赖对象，而是先声明此对象, 然后在使用时再通过某种方式（例如依赖注入）来获取依赖对象。

```swift

class ConcreteNetworkService: NetworkService {
    func fetchData(completion: @escaping (Data?, Error?) -> Void) {
        // 实际的网络请求实现
    }
}

// 在 `ViewController` 中声明依赖需求
class ViewController: UIViewController {
    var networkService: ConcreteNetworkService!

    override func viewDidLoad() {
        super.viewDidLoad()
        networkService.fetchData { data, error in
            if let data = data {
                // 处理数据
            } else if let error = error {
                // 处理错误
            }
        }
    }

// 注入依赖对象
let service = ConcreteNetworkService()
let vc = ViewController()
vc.networkService = service

```

运行时依赖管理

 `Router` 负责在运行时动态地将依赖对象传递给源模块, 其具体实现是基于接口管理来完成的. 
 - 源模块通过抽象声明所需的接口, 来指定所需要的依赖对象应该满足的需求;
 - 目的地模块为源模块所需的所有接口需求提供具体功能实;
 - 路由器

```swift
protocol NetworkService {
    func fetchData(completion: @escaping (Data?, Error?) -> Void)
}
```
