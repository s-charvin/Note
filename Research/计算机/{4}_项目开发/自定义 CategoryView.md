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
lastmod: 2024-05-20 13:55:32
---

## CategoryView 组件设计思路

为了构建一个 CategoryView 组件，需要考虑以下三个方面：显示需求设计、数据管理与更新以及用户事件处理. 
- 显示需求设计主要包括可视组件的整体布局、样式设计、内容展示等. 
- 数据管理与更新主要包括数据源的设计、数据的更新、数据与视图的绑定等. 
- 用户事件处理主要包括用户交互事件的处理、事件传递、事件响应等. 

### 阶段实现：标签和内容区域

CategoryView 的主要功能是展示不同类别的内容，每个类别通过标签选项进行选择，然后根据选中的标签类别展示相关的具体内容. 

因此，一个 CategoryView 至少需要包含两个部分：标签选项显示区域和内容区域. 
- 标签选项显示区域：用于显示所有类别标签，用户可以点击标签切换类别内容. 
- 内容区域：用于显示当前选择类别的内容. 

此外，在实际使用 CategoryView 时，可能需要根据需求自定义为侧边栏或顶边栏展示，因此可以在最初设计时就考虑此问题，避免后续重复构造一个独立组件. 

根据以上需求，可以设计一个简单的 `MyCategoryView` 组件，包含标签选项显示区域和内容区域. 组件的主要部分包括：

1. **标签选项显示区域 (`tabView`)**：
    - 使用 `UICollectionView` 实现. 
    - 支持水平或垂直滚动，通过 `orientation` 属性控制. 
    - 每个标签通过 `UICollectionViewCell` 展示. 
    - 允许用户通过点击标签来切换内容区的显示. 
2. **内容区域 (`containerView`)**：
    - 同样使用 `UICollectionView` 实现. 
    - 支持分页显示，与标签选项同步更新. 
    - 背景色和滚动设置区别于标签区，提供视觉上的区分. 

根据 `orientation` 的设置， `tabView` 和 `containerView` 的布局会相应调整，支持水平和垂直两种布局方式. 

然后分别实现 `tabView` 和 `containerView` 的数据源和代理协议即可控制各区域内容的更新，完成基本的区域展示. 完整代码实现示例如下：

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
    lazy var tabView: UICollectionView = {
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
        self.tabView.register(
            UICollectionViewCell.self, forCellWithReuseIdentifier: "testCell")

        self.addSubview(self.containerView)
        self.addSubview(self.tabView)


        // 使用 NSlayoutConstraint 进行布局
        self.tabView.translatesAutoresizingMaskIntoConstraints = false
        self.containerView.translatesAutoresizingMaskIntoConstraints = false

        switch self.orientation {
        case .horizontal:
            NSLayoutConstraint.activate([
                self.tabView.topAnchor.constraint(equalTo: self.topAnchor),
                self.tabView.leadingAnchor.constraint(equalTo: self.leadingAnchor),
                self.tabView.trailingAnchor.constraint(equalTo: self.trailingAnchor),
                self.tabView.heightAnchor.constraint(equalToConstant: 44),

                self.containerView.topAnchor.constraint(equalTo: self.tabView.bottomAnchor),
                self.containerView.bottomAnchor.constraint(equalTo: self.bottomAnchor),
                self.containerView.leadingAnchor.constraint(equalTo: self.leadingAnchor),
                self.containerView.trailingAnchor.constraint(equalTo: self.trailingAnchor)
            ])
        case .vertical:
            NSLayoutConstraint.activate([
                self.tabView.topAnchor.constraint(equalTo: self.topAnchor),
                self.tabView.leadingAnchor.constraint(equalTo: self.leadingAnchor),
                self.tabView.bottomAnchor.constraint(equalTo: self.bottomAnchor),
                self.tabView.widthAnchor.constraint(equalToConstant: 44),

                self.containerView.topAnchor.constraint(equalTo: self.topAnchor),
                self.containerView.bottomAnchor.constraint(equalTo: self.bottomAnchor),
                self.containerView.leadingAnchor.constraint(equalTo: self.tabView.trailingAnchor),
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
        let reuseCell = self.tabView.dequeueReusableCell(
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
        // 当滚动方向为垂直(.vertical)时，一行定义为横向的单元格序列，因此此值表示行间的垂直距离. 
        // 当滚动方向为水平(.horizontal)时，一行定义为纵向的单元格序列，此时此值表示行间的水平距离. 
        return 30
    }

    public func collectionView(
        _ collectionView: UICollectionView,
        layout collectionViewLayout: UICollectionViewLayout,
        minimumInteritemSpacingForSectionAt section: Int
    ) -> CGFloat {
        // 在垂直滚动模式下，此间距是单元格在横向上的间距. 
        // 在水平滚动模式下，此间距是单元格在纵向上的间距. 
        return 10
    }
}
```

### 阶段实现：自定义标签选项内容

由前面的设计可知，标签选项显示区域 `tabView` 计划基于 `UICollectionView` 实现，其内部每个标签通过 `UICollectionViewCell` 展示. 

在实际开发中，根据任务需求，标签的展示内容可能不仅仅是文字，还可能包含图片、图标、角标等. 因此，需要设计不同类型的标签数据源，用于存储标签的展示内容、样式、状态等信息. 然后在构造 `CategoryView` 时，根据标签数据源的内容，构造和传入对应的标签数据源即可. 

同时, 为了根据数据源的内容来自动控制 `tabView` 中标签的展示，可以将 `tabView` 的关于数据的代理方法进行封装，通过标签数据源来实现. 包括注册标签项的 cell 类型、获取标签项的数量、获取标签项的 cell、获取标签项的大小、获取标签项的间距等.

此外, 考虑到需要根据用户的点击事件来切换内容区域的显示，需要设计一个事件处理器，用于处理用户点击标签的事件.

以下是根据上述设计思路，对 `tabView` 进行封装的示例代码：

```swift
class MyCategoryViewTabView: UICollectionView {
    var viewDataSource: MyCategoryViewTabViewDataSource?
    var eventHandler: MyCategoryViewTabViewEventHandler?

    override init(frame: CGRect, collectionViewLayout layout: UICollectionViewLayout) {
        super.init(frame: frame, collectionViewLayout: layout)
        self.dataSource = self
        self.delegate = self

    }
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
}

// MARK: - UICollectionViewDelegate
extension MyCategoryViewTabView: UICollectionViewDataSource {
    func numberOfSections(in collectionView: UICollectionView) -> Int {
        return 1
    }

    func collectionView(
        _ collectionView: UICollectionView,
        numberOfItemsInSection section: Int
    ) -> Int {
        let count = self.viewDataSource?.count() ?? 0
        return self.viewDataSource?.tabView(self, numberOfItemsInSection: count) ?? count
    }

    func collectionView(
        _ collectionView: UICollectionView,
        cellForItemAt indexPath: IndexPath
    ) -> UICollectionViewCell {
        return self.viewDataSource?.tabView(self, cellForItemAt: indexPath) ?? UICollectionViewCell()
    }
}

// MARK: - UICollectionViewDelegateFlowLayout
extension MyCategoryViewTabView: UICollectionViewDelegateFlowLayout {
    func collectionView(
        _ collectionView: UICollectionView,
        layout collectionViewLayout: UICollectionViewLayout,
        insetForSectionAt section: Int
    ) -> UIEdgeInsets {
        return self.viewDataSource?.tabView(self, insetForSectionAt: section) ?? UIEdgeInsets.zero
    }

    func collectionView(
        _ collectionView: UICollectionView,
        layout collectionViewLayout: UICollectionViewLayout,
        sizeForItemAt indexPath: IndexPath
    ) -> CGSize {
        return self.viewDataSource?.tabView(self, sizeForItemAt: indexPath) ?? CGSize.zero
    }

    func collectionView(
        _ collectionView: UICollectionView,
        layout collectionViewLayout: UICollectionViewLayout,
        minimumLineSpacingForSectionAt section: Int
    ) -> CGFloat {
        return self.viewDataSource?.tabView(self, minimumLineSpacingForSectionAt: section) ?? 0
    }

    func collectionView(
        _ collectionView: UICollectionView,
        layout collectionViewLayout: UICollectionViewLayout,
        minimumInteritemSpacingForSectionAt section: Int
    ) -> CGFloat {
        return self.viewDataSource?.tabView(self, minimumInteritemSpacingForSectionAt: section) ?? 0
    }
}

// MARK: - UICollectionViewDelegate
extension MyCategoryViewTabView: UICollectionViewDelegate {
    func collectionView(
        _ collectionView: UICollectionView,
        didSelectItemAt indexPath: IndexPath
    ) {
        // 选中标签时的操作
        self.eventHandler?.tabView(self, didSelectItemAt: indexPath)
    }
}
```

#### 标签数据源设计

首先，由于标签数据源可能包含不同类型的标签，因此需要设计一个基础的标签数据源协议，用于定义标签数据源的基本属性和方法. 然后根据需求，自定义实现不同的标签数据源类. 

如果不考虑标签数据源的具体内容，一个基础的标签数据源协议一般包含以下内容：
- 标签标识符(`identifier`)：用于标识标签数据源的唯一标识. 
- 标签项集合(`tabItems`)：用于存储标签数据源的所有标签项对象. 
- 标签项间距(`itemSpacing`)：用于记录标签项之间的间距. 
- 一些控制标签项间距的属性：(`isItemSpacingAverageEnabled` 用于控制标签项间距是否均匀分布)
- 一些辅助方法，如获取标签数量、获取标签项、获取标签项实例等. 
- 一些处理数据源的逻辑方法，如注册标签项的 cell 类型、获取标签项的数量、获取标签项的 cell、获取标签项的大小、获取标签项的间距等. 这些逻辑方法实现了 `tabView` 的数据源和代理方法的实现，通过数据来自动控制标签的展示. 
- 支持下标访问标签项，以便快速获取标签项. 

当为 `tabView` 绑定数据源时，会自动通过数据源的 cell 注册方法注册对应标签项的 cell 类型，然后通过数据源的代理方法获取标签项的数量、获取标签项的 cell、获取标签项的大小、获取标签项的间距等.

基础的标签数据源协议示例代码如下：

```swift
protocol MyCategoryViewTabViewDataSource {
    var identifier: String { get set }
    var tabItems: [Int: MyCategoryViewTabItem] { get set }
    var itemSpacing: CGFloat { get set }
    var isItemSpacingAverageEnabled: Bool { get set }

    subscript(index: Int) -> MyCategoryViewTabItem { get set }

    func count() -> Int
    func items() -> [MyCategoryViewTabItemProtocol]
    func itemInstance() -> MyCategoryViewTabItemProtocol

    func registerCellClass(in collectionView: UICollectionView, with identifier: String)

    func tabView(_ tabView: MyCategoryViewTabView, numberOfItemsInSection section: Int) -> Int
    func tabView(_ tabView: MyCategoryViewTabView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell
    func tabView(_ tabView: MyCategoryViewTabView, insetForSectionAt section: Int) -> UIEdgeInsets
    func tabView(_ tabView: MyCategoryViewTabView, sizeForItemAt indexPath: IndexPath) -> CGSize
    func tabView(_ tabView: MyCategoryViewTabView, minimumLineSpacingForSectionAt section: Int) -> CGFloat
    func tabView(_ tabView: MyCategoryViewTabView, minimumInteritemSpacingForSectionAt section: Int) -> CGFloat
}

extension MyCategoryViewTabViewDataSource {

    func registerCellClass(in collectionView: UICollectionView) {
        self.registerCellClass(in: collectionView, with: self.identifier)
    }

    func tabView(_ tabView: MyCategoryViewTabView, numberOfItemsInSection section: Int) -> Int {
        return self.count()
    }

    func tabView(_ tabView: MyCategoryViewTabView, insetForSectionAt section: Int) -> UIEdgeInsets {
        return UIEdgeInsets.zero
    }

    func tabView(_ tabView: MyCategoryViewTabView, minimumLineSpacingForSectionAt section: Int) -> CGFloat {
        return self.itemSpacing
    }

    func tabView(_ tabView: MyCategoryViewTabView, minimumInteritemSpacingForSectionAt section: Int) -> CGFloat {
        return self.itemSpacing
    }
}
```

其中, 标签项集合 `tabItems` 存储了所有的标签项对象，每个对象由提供的标签原始数据转换而来. 通过重载的下标访问方法，可以快速访问 `tabItems` 中的标签项. 这里 `tabItems` 可以采用的字典结构，以标签的索引为键，标签项为值, 方便通过标签的索引快速获取标签项, 同时可以实现懒加载的作用, 只有在需要时才去创建标签项.

想要将不同的标签原始数据转换为标签项对象进行统一管理, 也需要首先定义一个基础的标签项结构，用于定义标签项的基本属性和方法. 然后根据不同数据源需求, 自定义不同类型的标签项结构类.

每个标签项结构除了其主要展示内容外，必须包含标签所在位置，被选中状态，自动计算的标签内容宽度. 根据需求设计的代码示例如下：

```swift
protocol MyCategoryViewTabItemProtocol {
    var index: Int { get set }
    var isSelected: Bool { get set }
    var itemWidth: CGFloat { get set }
}

class MyCategoryViewTabItem: MyCategoryViewTabItemProtocol {
    var index: Int = 0
    var isSelected = false
    var itemWidth: CGFloat = 0
}
```

又因为 `UICollectionView` 最终展示的是 `UICollectionViewCell`，因此需要定义一个基础的标签项 cell 类，用于绑定标签项对象. 然后根据不同的标签项对象，自定义不同类型的标签项 cell 类. 基本的标签项 cell 协议如下：

```swift
protocol MyCategoryViewTabCell {
    associatedtype Item: MyCategoryViewTabItem
    var item: Item? { get set }
    func reloadData()
}
```

#### 标签数据源实现(纯文字标签)

在设计了基础的标签数据源协议后，可以根据实际需求，自定义不同类型的标签数据源类. 以纯文字标签数据源为例，一个基础的纯文字标签数据源除了包含基础的标签数据源协议属性外，还应该包含一些纯文字标签特有的属性和方法，如：
- 标题数据容器(`titles`)：用于存储所有标签的标题文本. 
- 标题行数目(`titleNumberOfLines`)：用于记录标签标题的行数. 
- 标题正常颜色(`titleNormalColor`)：用于记录标签标题的正常颜色. 
- 标题选中颜色(`titleSelectedColor`)：用于记录标签标题的选中颜色. 
- 标题正常字体(`titleNormalFont`)：用于记录标签标题的正常字体. 
- 标题选中字体(`titleSelectedFont`)：用于记录标签标题的选中字体. 

标签数据容器 `titles` 存储了所有标签的原始数据，每个标签数据可以通过 `createTabItem(for index: Int)` 方法转换为标签项对象, 并存储在 `tabItems` 中. 

纯文字标签数据源示例代码如下：

```swift
class MyCategoryViewTitleTabViewDataSource: MyCategoryViewTabViewDataSource {
    var identifier = "MyCategoryViewTitleTabCell"
    var tabItems: [Int : MyCategoryViewTabItem] = [:]
    var itemSpacing: CGFloat = 0
    var isItemSpacingAverageEnabled = false

    var titles: [String] = []
    var titleNumberOfLines: Int = 1
    var titleNormalColor: UIColor = .black
    var titleSelectedColor: UIColor = .red
    var titleNormalFont: UIFont = .systemFont(ofSize: 15)
    var titleSelectedFont: UIFont?

    subscript(index: Int) -> MyCategoryViewTabItem {
        get {
            if let item = self.tabItems[index] {
                return item
            } else {
                let newItem = self.createTabItem(for: index)
                self.tabItems[index] = newItem
                return newItem
            }
        }
        set {
            self.tabItems[index] = newValue
        }
    }

    func count() -> Int {
        return self.titles.count
    }

    func items() -> [MyCategoryViewTabItemProtocol] {
        if self.tabItems.count != self.titles.count {
            for index in 0..<self.titles.count {
                _ = self[index]
            }
        }
        return self.tabItems.values.map { $0 }
    }

    func itemInstance() -> MyCategoryViewTabItemProtocol {
        return MyCategoryViewTitleTabItem()
    }

    func registerCellClass(in collectionView: UICollectionView, with identifier: String = "MyCategoryViewTitleTabCell") {
        self.identifier = identifier
        collectionView.register(
            MyCategoryViewTitleTabCell.self,
            forCellWithReuseIdentifier: identifier
        )
    }

    func tabView(_ tabView: MyCategoryViewTabView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell {
        guard let cell = tabView.dequeueReusableCell(
            withReuseIdentifier: self.identifier,
            for: indexPath
        ) as? MyCategoryViewTitleTabCell else {
            return UICollectionViewCell()
        }
        cell.item = self[indexPath.item] as? MyCategoryViewTitleTabCell.Item
        cell.reloadData()
        return cell
    }

    func tabView(_ tabView: MyCategoryViewTabView, sizeForItemAt indexPath: IndexPath) -> CGSize {
        guard let item = self[indexPath.item] as? MyCategoryViewTitleTabItem else { return .zero }
        let width = item.itemWidth
        return CGSize(width: width, height: tabView.bounds.height)
    }

    private func widthForTitle(_ title: String) -> CGFloat {
        let textWidth = NSString(string: title).boundingRect(
            with: CGSize(width: CGFloat.infinity, height: CGFloat.infinity),
            options: [.usesFontLeading, .usesLineFragmentOrigin],
            attributes: [NSAttributedString.Key.font: self.titleSelectedFont ?? self.titleNormalFont],
            context: nil
        ).size.width
        return CGFloat(ceilf(Float(textWidth)))
    }

    func createTabItem(for index: Int) -> MyCategoryViewTabItem {
        guard index >= 0, index < self.titles.count else {
            fatalError("Index out of range")
        }
        let title = self.titles[index]
        let item = MyCategoryViewTitleTabItem()
        item.index = index
        item.title = title
        item.textWidth = self.widthForTitle(title)
        item.itemWidth = item.textWidth
        item.titleNumberOfLines = self.titleNumberOfLines
        item.titleNormalColor = self.titleNormalColor
        item.titleSelectedColor = self.titleSelectedColor
        item.titleNormalFont = self.titleNormalFont
        item.titleSelectedFont = self.titleSelectedFont ?? self.titleNormalFont
        return item
    }
}
```

`tabItems` 中的最基础的标签项对象除了包含基础的标签项属性外，还应该包含一些纯文字标签特有的属性和方法，如：
- 标题(`title`)：用于记录标签的标题文本.
- 标题行数(`titleNumberOfLines`)：用于记录标签标题的行数.
- 标题宽度(`textWidth`)：用于记录标签标题的宽度.
- 标题正常颜色(`titleNormalColor`)：用于记录标签标题的正常颜色.
- 标题选中颜色(`titleSelectedColor`)：用于记录标签标题的选中颜色.
- 标题正常字体(`titleNormalFont`)：用于记录标签标题的正常字体.
- 标题选中字体(`titleSelectedFont`)：用于记录标签标题的选中字体.

```swift
class MyCategoryViewTitleTabItem: MyCategoryViewTabItem {
    var title: String = ""
    var titleNumberOfLines: Int = 1
    var textWidth: CGFloat = 0
    var titleNormalColor: UIColor = .black
    var titleSelectedColor: UIColor = .red
    var titleNormalFont: UIFont = .systemFont(ofSize: 15)
    var titleSelectedFont: UIFont = .systemFont(ofSize: 15)
}
```

然后为纯文字标签项定义一个基础的标签项 cell 类，用于绑定标签项对象并实现标签项文字的展示, 以及数据刷新逻辑.

```swift

class MyCategoryViewTitleTabCell: UICollectionViewCell, MyCategoryViewTabCell {
    typealias Item = MyCategoryViewTitleTabItem
    var item: Item?
    let titleLabel = UILabel()

    override init(frame: CGRect) {
        super.init(frame: frame)
        self.setupViews()
    }

    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }

    override func layoutSubviews() {
        super.layoutSubviews()
        guard let item = self.item else { return }

        // 使用 sizeThatFits 方法确保标签的高度适合标签内容
        let labelSize = self.titleLabel.sizeThatFits(self.contentView.bounds.size)
        var labelBounds = CGRect(x: 0, y: 0, width: labelSize.width, height: labelSize.height)

        // 使用 textWidth 来限制标签的宽度
        labelBounds.size.width = item.textWidth
        self.titleLabel.bounds = labelBounds
        self.titleLabel.center = self.contentView.center
    }

    func setupViews() {
        self.titleLabel.textAlignment = .center
        self.contentView.addSubview(self.titleLabel)
    }

    func reloadData() {
        guard let item = self.item else { return }
        self.titleLabel.text = item.title
        self.titleLabel.textColor = item.isSelected ? item.titleSelectedColor : item.titleNormalColor
        self.titleLabel.font = item.isSelected ? item.titleSelectedFont : item.titleNormalFont
        self.setNeedsLayout() // 重新布局
    }
}


```
