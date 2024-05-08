---
title: "{{自定义 CategoryView}}"
description: ""
author: ""
tags: 
categories:
  - ""
keywords:
  - ""
draft: true
layout: ""
date: 2024-05-08 11:20:13
lastmod: 2024-05-08 14:39:45
---

## 主功能和视图展示

- 标签选项显示区域
- 内容区域
- 控制侧边栏还是顶边栏

```swift
//
//  MyCategoryView.swift
//  EventPage
//
//  Created by scw on 2024/1/24.
//

import Foundation
import UIKit
import SnapKit

class MyCategoryView: UIView {
    enum Orientation {
        case horizontal, vertical
    }

    var orientation: Orientation = .horizontal

    // 标签选项显示区域
    lazy var tabCollectionView: UICollectionView = {
        let layout = UICollectionViewFlowLayout()
        layout.scrollDirection = self.orientation == .horizontal ? .horizontal : .vertical
        layout.minimumLineSpacing = 0
        let collectionView = UICollectionView(
            frame: CGRect.zero, collectionViewLayout: layout)
        collectionView.backgroundColor = .gray
        collectionView.showsHorizontalScrollIndicator = false
        collectionView.showsVerticalScrollIndicator = false
        collectionView.scrollsToTop = false
        collectionView.dataSource = self
        collectionView.delegate = self
        return collectionView
    }()

    // 内容区域 UIScrollView
    lazy var containerView: UICollectionView = {
        let layout = UICollectionViewFlowLayout()
        layout.scrollDirection = self.orientation == .horizontal ? .horizontal : .vertical
        layout.minimumLineSpacing = 0
        let collectionView = UICollectionView(
            frame: CGRect.zero, collectionViewLayout: layout)
        collectionView.backgroundColor = .red
        collectionView.isPagingEnabled = true
        collectionView.showsHorizontalScrollIndicator = false
        collectionView.showsVerticalScrollIndicator = false
        collectionView.scrollsToTop = false
        //        collectionView.dataSource = self
        //        collectionView.delegate = self
        return collectionView
    }()

    override init(frame: CGRect) { // 初始化方法
        super.init(frame: frame)
        self.setupViews()
    }

    init (frame: CGRect, orientation: Orientation) {
        super.init(frame: frame)
        self.orientation = orientation
        self.setupViews()
    }

    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }

    private func setupViews() {
        // 设置 collectionView 的属性
        self.tabCollectionView.register(
            UICollectionViewCell.self, forCellWithReuseIdentifier: "testCell")

        self.addSubview(self.containerView)
        self.addSubview(self.tabCollectionView)


        // 使用 NSlayoutConstraint 进行布局
        self.tabCollectionView.translatesAutoresizingMaskIntoConstraints = false
        self.containerView.translatesAutoresizingMaskIntoConstraints = false

        switch self.orientation {
        case .horizontal:
            NSLayoutConstraint.activate([
                self.tabCollectionView.topAnchor.constraint(equalTo: self.topAnchor),
                self.tabCollectionView.leadingAnchor.constraint(equalTo: self.leadingAnchor),
                self.tabCollectionView.trailingAnchor.constraint(equalTo: self.trailingAnchor),
                self.tabCollectionView.heightAnchor.constraint(equalToConstant: 44),

                self.containerView.topAnchor.constraint(equalTo: self.tabCollectionView.bottomAnchor),
                self.containerView.bottomAnchor.constraint(equalTo: self.bottomAnchor),
                self.containerView.leadingAnchor.constraint(equalTo: self.leadingAnchor),
                self.containerView.trailingAnchor.constraint(equalTo: self.trailingAnchor)
            ])
        case .vertical:
            NSLayoutConstraint.activate([
                self.tabCollectionView.topAnchor.constraint(equalTo: self.topAnchor),
                self.tabCollectionView.leadingAnchor.constraint(equalTo: self.leadingAnchor),
                self.tabCollectionView.bottomAnchor.constraint(equalTo: self.bottomAnchor),
                self.tabCollectionView.widthAnchor.constraint(equalToConstant: 44),

                self.containerView.topAnchor.constraint(equalTo: self.topAnchor),
                self.containerView.bottomAnchor.constraint(equalTo: self.bottomAnchor),
                self.containerView.leadingAnchor.constraint(equalTo: self.tabCollectionView.trailingAnchor),
                self.containerView.trailingAnchor.constraint(equalTo: self.trailingAnchor)
            ])
        }
    }
}

// MARK: - UICollectionViewDataSource

extension MyCategoryView: UICollectionViewDataSource {
    // 因为标签栏只有一行, 所以只有一个 section
    public func numberOfSections(in collectionView: UICollectionView) -> Int {
        return 1
    }

    public func collectionView(
        _ collectionView: UICollectionView, numberOfItemsInSection section: Int
    ) -> Int {
        return 5
    }

    public func collectionView(_ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath)
    -> UICollectionViewCell {
        // 初期开发阶段, 先使用默认的随机背景的 UICollectionViewCell 进行标签展示测试
        let reuseCell = self.tabCollectionView.dequeueReusableCell(
            withReuseIdentifier: "testCell",
            for: indexPath
        )
        reuseCell.backgroundColor = UIColor(
            red: CGFloat.random(in: 0...1),
            green: CGFloat.random(in: 0...1),
            blue: CGFloat.random(in: 0...1),
            alpha: 1.0
        )
        return reuseCell
    }
}

// MARK: - UICollectionViewDelegate

extension MyCategoryView: UICollectionViewDelegate {
    public func collectionView(
        _ collectionView: UICollectionView, didSelectItemAt indexPath: IndexPath
    ) {
        return
    }
}

// MARK: - UICollectionViewDelegateFlowLayout

extension MyCategoryView: UICollectionViewDelegateFlowLayout {
    public func collectionView(
        _ collectionView: UICollectionView,
        layout collectionViewLayout: UICollectionViewLayout,
        insetForSectionAt section: Int
    ) -> UIEdgeInsets {
        // 设置标签栏的内边距, 比如左右边距
        return UIEdgeInsets(top: 0, left: 0, bottom: 0, right: 0)}

    public func collectionView(
        _ collectionView: UICollectionView,
        layout collectionViewLayout: UICollectionViewLayout,
        sizeForItemAt indexPath: IndexPath
    ) -> CGSize {
        // 设置每个标签的宽度
        return CGSize(
            width: 44, height: 44)
    }

    public func collectionView(
        _ collectionView: UICollectionView,
        layout collectionViewLayout: UICollectionViewLayout,
        minimumLineSpacingForSectionAt section: Int
    ) -> CGFloat {
        // 当滚动方向为垂直（.vertical）时，一行定义为横向的单元格序列，因此此值表示行间的垂直距离。
        // 当滚动方向为水平（.horizontal）时，一行定义为纵向的单元格序列，此时此值表示行间的水平距离。
        return 30
    }

    public func collectionView(
        _ collectionView: UICollectionView,
        layout collectionViewLayout: UICollectionViewLayout,
        minimumInteritemSpacingForSectionAt section: Int
    ) -> CGFloat {
        // 在垂直滚动模式下，此间距是单元格在横向上的间距。
        // 在水平滚动模式下，此间距是单元格在纵向上的间距。
        return 10
    }
}
```

## 标签选项显示区域设计

标签选项显示区域基于 UICollectionView 实现，通过数据源来提供多个标签数据，并将这些数据转换为对应 cell 元素展示出来。

整体的数据源应该包含一个容器来存放所有标签数据，并记录每个标签之间的间距，提供一些处理数据源的逻辑代码，如转换数据到 cell，以及一些辅助性方法，如获取数量，获取标签空白实例等。

每个标签数据除了其主要展示内容外，必须包含数据所在位置，被选中状态，自动计算的内容宽度和高度。最基础的标签数据 Title 应该包含的内容有：
- 标题文本
- 标题行数目

以纯文字标签数据源为例：

- 标题正常，选中和当前的颜色设置记录
- 标题正常，选中和当前的字体设置记录
- 标题文本宽度固定值
