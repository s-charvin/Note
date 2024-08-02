---
title: ""
description: ""
author: ""
tags: [""]
categories: ""
keywords:  [""]
draft: true
layout: ""
date: 2024-07-30 18:00:49
lastmod: 2024-07-30 18:11:28
---
```kotlin
// MyCategoryViewTabItem.kt
package com.zhangyue.library.categoryView

interface MyCategoryViewTabItemProtocol {
    var index: Int
    var isSelected: Boolean
    var itemWidth: Float
}

class MyCategoryViewTabItem : MyCategoryViewTabItemProtocol {
    override var index: Int = 0
    override var isSelected: Boolean = false
    override var itemWidth: Float = 0f
}
```

```kotlin
// MyCategoryViewTabCell.kt
package com.zhangyue.library.categoryView

import android.view.View
import androidx.recyclerview.widget.RecyclerView

abstract class MyCategoryViewTabCell(itemView: View) : RecyclerView.ViewHolder(itemView) {
    abstract var item: MyCategoryViewTabItemProtocol?
    abstract fun reloadData()
}
```

```kotlin
// MyCategoryViewTabViewEventHandler.kt
package com.zhangyue.library.categoryView

interface MyCategoryViewTabViewEventHandler {
    fun tabView(tabView: MyCategoryViewTabView, didSelectItemAt: Int)
}

open class DefaultMyCategoryViewTabViewEventHandler : MyCategoryViewTabViewEventHandler {
    override fun tabView(tabView: MyCategoryViewTabView, didSelectItemAt: Int) {
        tabView.setSelectedIndex(didSelectItemAt, true)
    }
}
```

```kotlin
// MyCategoryViewTabViewDataSource.kt
package com.zhangyue.library.categoryView

import android.graphics.Rect
import android.view.View
import androidx.recyclerview.widget.RecyclerView

interface MyCategoryViewTabViewDataSource {
    var identifier: String
    var tabItems: MutableMap<Int, MyCategoryViewTabItem>
    var itemSpacing: Float
    var tabContentInset: Rect
    var spacingAverageEnabled: Boolean

    fun count(): Int
    fun items(): MutableMap<Int, MyCategoryViewTabItem>
    fun registerCellClass(tabView: MyCategoryViewTabView, identifier: String)
    fun tabView(tabView: MyCategoryViewTabView, numberOfItemsInSection: Int): Int
    fun tabView(tabView: MyCategoryViewTabView, cellForItemAt: Int): RecyclerView.ViewHolder
    fun tabView(tabView: MyCategoryViewTabView, insetForSectionAt: Int): Rect
    fun tabView(tabView: MyCategoryViewTabView, sizeForItemAt: Int): Int
    fun tabView(tabView: MyCategoryViewTabView, minimumLineSpacingForSectionAt: Int): Float
    fun tabView(tabView: MyCategoryViewTabView, minimumInteritemSpacingForSectionAt: Int): Float

    operator fun get(index: Int): MyCategoryViewTabItem?
    operator fun set(index: Int, value: MyCategoryViewTabItem?)
}
```

```kotlin
// MyCategoryViewTabView.kt
package com.zhangyue.library.categoryView

import android.content.Context
import android.graphics.Rect
import android.util.AttributeSet
import android.view.View
import android.widget.FrameLayout
import androidx.recyclerview.widget.RecyclerView
import androidx.recyclerview.widget.LinearLayoutManager

class MyCategoryViewTabView @JvmOverloads constructor(
    context: Context,
    attrs: AttributeSet? = null,
    defStyleAttr: Int = 0
) : FrameLayout(context, attrs, defStyleAttr) {

    enum class Orientation {
        HORIZONTAL, VERTICAL
    }

    var dataSource: MyCategoryViewTabViewDataSource? = null
        set(value) {
            field = value
            value?.let {
                for ((index, item) in it.items()) {
                    item.isSelected = index == selectedIndex
                }
            }
            collectionView.adapter?.notifyDataSetChanged()
        }

    var eventHandler: MyCategoryViewTabViewEventHandler? = DefaultMyCategoryViewTabViewEventHandler()

    private val collectionView: RecyclerView
    private var selectedIndex: Int = 0

    init {
        val layoutManager = LinearLayoutManager(context)
        layoutManager.orientation = LinearLayoutManager.HORIZONTAL
        collectionView = RecyclerView(context).apply {
            this.layoutManager = layoutManager
            this.adapter = object : RecyclerView.Adapter<RecyclerView.ViewHolder>() {
                override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): RecyclerView.ViewHolder {
                    return dataSource?.tabView(this@MyCategoryViewTabView, viewType)
                        ?: throw IllegalStateException("DataSource is not set")
                }

                override fun onBindViewHolder(holder: RecyclerView.ViewHolder, position: Int) {
                    val item = dataSource?.get(position)
                    if (holder is MyCategoryViewTabCell) {
                        holder.item = item
                        holder.reloadData()
                    }
                }

                override fun getItemCount(): Int {
                    return dataSource?.count() ?: 0
                }

                override fun getItemViewType(position: Int): Int {
                    return position
                }
            }
        }
        addView(collectionView)
    }

    fun setSelectedIndex(index: Int, animated: Boolean) {
        val oldIndex = selectedIndex
        if (index < 0 || index >= (dataSource?.count() ?: 0)) return
        if (index == selectedIndex) return

        selectedIndex = index
        dataSource?.get(oldIndex)?.isSelected = false
        dataSource?.get(selectedIndex)?.isSelected = true
        collectionView.adapter?.notifyItemChanged(oldIndex)
        collectionView.adapter?.notifyItemChanged(selectedIndex)
        collectionView.scrollToPosition(selectedIndex)
    }
}
```
