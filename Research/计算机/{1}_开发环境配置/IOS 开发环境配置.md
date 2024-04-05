---
title: IOS 开发环境配置
description: ""
author: ""
tags: 
categories:
  - ""
keywords:
  - ""
draft: true
layout: ""
date: 2024-04-02 21:18:40
lastmod: 2024-04-03 06:16:17
---

# IOS 开发配置

## 基本系统环境

办公软件([Pages](https://apps.apple.com/us/app/pages/id409201541?mt=12), [‎Keynote](https://apps.apple.com/us/app/keynote/id409183694?mt=12), [Numbers](https://apps.apple.com/us/app/numbers/id409203825?mt=12))
程序管理([免费下载 CleanMyMac X —— 为 Mac 而生的神奇 App](https://macpaw.com/zh/download/cleanmymac))
海外访问([v2rayU](https://github.com/yanue/V2rayU/tree/dev))
跨端文件同步([OneDrive](https://apps.apple.com/us/app/onedrive/id823766827?mt=12))
浏览器([Chorme](https://www.google.com/chrome/), [Edge](https://www.microsoft.com/en-us/edge/download))
笔记记录([Obsidian](https://obsidian.md/download))
终端代理 ( `export http_proxy=http://127.0.0.1:1087;export https_proxy=http://127.0.0.1:1087;export ALL_PROXY=socks5://127.0.0.1:1080` )
剪切板管理([GitHub - p0deje/Maccy: Lightweight clipboard manager for macOS](https://github.com/p0deje/Maccy))
版本管理系统([Sourcetree | Free Git GUI for Mac and Windows](https://www.sourcetreeapp.com/))
gif 录制工具([Gifox 2 for Mac – Delightful GIF Recording, Conversion, Editing and Sharing App](https://gifox.app/))
终端录制工具([GitHub - icholy/ttygif: Convert terminal recordings to animated gifs](https://github.com/icholy/ttygif))
开发者工具箱(DevHub, [He3](https://he3app.com/zh/))
离线文档查看工具([Dash for macOS - API Documentation Browser, Snippet Manager - Kapeli](https://kapeli.com/dash))
brew 可视化界面([Cakebrew](https://www.cakebrew.com/))
文件差异比较([SourceGear | DiffMerge](https://sourcegear.com/diffmerge/downloads.html))
SHH 客户端([Download Termius for Mac](https://termius.com/download/macos))
终端工具补充([hyper](https://github.com/vercel/hyper), [tabby](https://github.com/Eugeny/tabby/))
开发工具预下载([Visual Studio Code November 2023](https://code.visualstudio.com/updates/v1_85))
窗口切换工具([AltTab - Windows alt-tab on macOS](https://alt-tab-macos.netlify.app/))
字典工具([GitHub - tisfeng/Easydict: 一个简洁优雅的词典翻译 macOS App。开箱即用，支持离线 OCR 识别，支持有道词典，🍎 苹果系统词典，🍎 苹果系统翻译，ChatGPT，Gemini，DeepL，Google，Bing，腾讯，百度，阿里，小牛，彩云和火山翻译。A concise and elegant Dictionary and Translator macOS App for looking up words and translating text.](https://github.com/tisfeng/Easydict))
苹果开发者前瞻([Releases · insidegui/WWDC](https://github.com/insidegui/WWDC/releases))
Github 镜像加速方法
- 压缩包下载加速：https://github.ur 1.fun
- Clone 加速：https://gitclone.com/github.com/...

## 基本开发环境

Iterm 安装及其配置
- https://iterm 2.com 下载并安装，移动 iTerm 2 到应用目录，打开即可开始使用，首次启动的时候，会提示安装 pip。
- 配置快捷键
	- 配置 Split Pane 切换，开启 Cmd + 数字切换命令行窗口方式。同时可以使用 Cmd + Shift + Enter 放大某一个单独的窗口。
	- 新增 hot key window 配置，使用快捷 Ctrl + ` 快速呼出iTerm窗口。
- 安装主题
	- 主题下载地址：https://github.com/mbadolato/iTerm 2-Color-Schemes
	- 打开 Preferences 配置界面，然后 Profiles → Colors → Color Presets ，在下拉列表中选择 Import，选择刚才解压的 solarized → iterm 2-colors-solarized → Solarized Dark.itermcolors 文件，导入成功后，在 Color Presets 下选择 Solarized Dark 主题，就可以了。
- 设置为默认终端
	- 打开 iTerm，在默认菜单中选择”Make iTerm 2 Default Term”

homebrew 安装及其清华源配置

- 命令直接安装或应用安装
```zsh
# 方法1: 镜像安装命令
xcode-select --install
export HOMEBREW_INSTALL_FROM_API=1
export HOMEBREW_API_DOMAIN="https://mirrors.tuna.tsinghua.edu.cn/homebrew-bottles/api"
export HOMEBREW_BOTTLE_DOMAIN="https://mirrors.tuna.tsinghua.edu.cn/homebrew-bottles"
export HOMEBREW_BREW_GIT_REMOTE="https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/brew.git"
export HOMEBREW_CORE_GIT_REMOTE="https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-core.git"
git clone --depth=1 https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/install.git brew-install
/bin/bash brew-install/install.sh
rm -rf brew-install

# 方法2: 官方安装命令
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 方法3: 应用安装包下载地址
https://github.com/Homebrew/brew/releases


# 补充：仅针对基于 Apple Silicon CPU 设备上的 macOS 系统（命令行运行 `uname -m` 应输出 `arm64`）
test -r ~/.bash_profile && echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.bash_profile
test -r ~/.zprofile && echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
```

- Zsh 中设置默认源
```zsh
# 创建所需配置文件(如果没有, 有则不需创建)
touch .zprofile

# 情况1: 为 Zsh 终端设置源（默认）
test -r ~/.zprofile && echo 'export HOMEBREW_API_DOMAIN="https://mirrors.tuna.tsinghua.edu.cn/homebrew-bottles/api"' >> ~/.zprofile
test -r ~/.zprofile && echo 'export HOMEBREW_BREW_GIT_REMOTE="https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/brew.git"' >> ~/.zprofile
test -r ~/.zprofile && echo 'export HOMEBREW_CORE_GIT_REMOTE="https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-core.git"' >> ~/.zprofile

# 情况2: 为 bash 终端设置源
test -r ~/.bash_profile && echo 'export HOMEBREW_API_DOMAIN="https://mirrors.tuna.tsinghua.edu.cn/homebrew-bottles/api"' >> ~/.bash_profile  # bash
test -r ~/.bash_profile && echo 'export HOMEBREW_BREW_GIT_REMOTE="https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/brew.git"' >> ~/.bash_profile  # bash
test -r ~/.bash_profile && echo 'export HOMEBREW_CORE_GIT_REMOTE="https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-core.git"' >> ~/.bash_profile
test -r ~/.profile && echo 'export HOMEBREW_API_DOMAIN="https://mirrors.tuna.tsinghua.edu.cn/homebrew-bottles/api"' >> ~/.profile
test -r ~/.profile && echo 'export HOMEBREW_BREW_GIT_REMOTE="https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/brew.git"' >> ~/.profile
test -r ~/.profile && echo 'export HOMEBREW_CORE_GIT_REMOTE="https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-core.git"' >> ~/.profile

# 更新数据
source ~/.zprofile
brew update
```

ohmyzsh 安装及其配置

- 直接安装命令
```zsh
# 镜像安装指令
sh -c "$(curl -fsSL https://gitee.com/mirrors/oh-my-zsh/raw/master/tools/install.sh)"
# 官方安装指令
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```
- 安装插件， zoxide 支持历史地址快速跳转，fzf 提供跳转选择框， zsh-autosuggestions 提供命令自动补全，zsh-syntax-highlighting 提供语法高亮显示
```zsh
brew install zsh-syntax-highlighting
echo "source $(brew --prefix)/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh" >> ~/.zshrc

brew install zsh-autosuggestions
echo "source $(brew --prefix)/share/zsh-autosuggestions/zsh-autosuggestions.zsh" >> ~/.zshrc

brew install fzf
brew install zoxide

# 环境变量设置1：默认设置
echo 'eval "$(zoxide init zsh)"' >> ~/.zshrc
# 环境变量设置2：修改为 autojump 风格的 j 命令
echo 'eval "$(zoxide init zsh --cmd j)"' >> ~/.zshrc

source ~/.zshrc

# 使用提示：默认使用 z 匹配历史记录直接跳转
z anypath
# 使用提示：如果安装了 fzf，zi 在有多个选择时就会出现可视化选择框让你选择，如果只有一个则会直接跳转
zi anypath

# 使用提示：匹配历史记录直接跳转
j anypath
# 使用提示：如果安装了fzf，ji在有多个选择时就会出现可视化选择框让你选择，如果只有一个则会直接跳转
ji anypath
```

- 安装主题
	- 下载和安装字体：[GitHub - romkatv/powerlevel10k: A Zsh theme](https://github.com/romkatv/powerlevel10k#meslo-nerd-font-patched-for-powerlevel10k), 并在 iterm 2 的 **Preferences > Profiles > Text > Font** 将字体设定为 MesloLGS NF
	- 下载和注册主题
```zsh
brew install powerlevel10k
echo "source $(brew --prefix)/share/powerlevel10k/powerlevel10k.zsh-theme" >>~/.zshrc
```


  Xcode 安装及其版本管理
  
- 命令直接下载和安装 xcodes
```zsh
brew install --cask xcodes
```
- 通过 xcodes 安装指定版本的 xcode, 然后通过以下命令配置 xcode

```zsh
# 启用Xcode中文本编辑器的实时拼写检查功能
defaults write com.apple.dt.Xcode AutomaticallyCheckSpellingWhileTyping -bool YES
# 启用Xcode中文本编辑器自动移除行尾的空格功能
defaults write com.apple.dt.Xcode DVTTextEditorTrimTrailingWhitespace -bool YES
# 启用Xcode中文本编辑器自动移除空行中的空格功能
defaults write com.apple.dt.Xcode DVTTextEditorTrimWhitespaceOnlyLines -bool YES
# 启用Xcode中文本编辑器将制表符转换为空格功能
defaults write com.apple.dt.Xcode DVTTextEditorTabsToSpaces -bool YES
# 设置Xcode中文本编辑器使用制表符时的宽度为2个字符
defaults write com.apple.dt.Xcode DVTTextIndentTabWidth -int 4
# 设置Xcode中文本编辑器的缩进宽度为2个字符
defaults write com.apple.dt.Xcode DVTTextIndentWidth -int 4
# 设置Xcode中文本编辑器页面垂直参考线的位置为第160列
defaults write com.apple.dt.Xcode DVTTextShowPageGuide -bool YES
defaults write com.apple.dt.Xcode DVTTextPageGuideLocation -int 160
```

安装和配置  Copilot for Xcode
- 安裝 [Node](https://nodejs.org/en)，下载后选择 ßpkg 文件双击安装
- 安装 Copilot for Xcode
```zsh
brew install --cask copilot-for-xcode
```
- 在系统设置的 `隐私与安全性 -> 扩展` 中点击 `Xcode Source Editor` , 选中里面的 ` Copilot` 开启扩展.
- 点击软件的 `General -> Refresh` 刷新权限,并根据弹出提示, 设置 `accessibility Settings` 权限.
- 点击软件的 `Service -> Github Copilot -> Github Copilot Language Server` 的 `install` 安装服务; 然后点击相同区域新出现的 `Sign In` 登录并进入 GitHub 的验证页面, 输入被自动放入剪切板的设备代码, 授权连接此设备; 再继续点击 `"Confirm Sign-in"` 完成登录验证.
- 点击软件的 `Feature -> Suggestion`  将 `Feature Provider` 设置为 `GitHub Copilot`
- 通过 Xcode 创建或打开一个项目, 根据弹出提示允许 Copilot for Xcode 的文件访问权限.

安装和配置 Swiftfy for Xcode
- 下载安装器: [Objective-C to Swift Converter | Swiftify](https://swiftify.com/xcode-extension/)
- 跟着页面教程继续安装和配置

CocoaPods 安装及其配置，用于管理 Xcode 项目的依赖项

- 修改 gem 镜像源
```zsh
# 检查现在系统是哪个源
gem sources -l 
# 移除https://rubygems.org/
gem sources --remove https://rubygems.org/
# 添加国内ruby
gem sources --add https://mirrors.tuna.tsinghua.edu.cn/rubygems/
# 检查是否替换成功
gem sources -l 
```

- 安装最新版本 ruby

```zsh
# 查看 ruby 的安装目录
which -a ruby
# 通过 Homebrew 安装 ruby
brew install ruby
# 需把可执行文件导入全局变量 PATH 中即可，使用如下命令（安装后会有命令提示， 路径不同以提示为主）
echo 'export PATH="/usr/local/opt/ruby/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

- 安装 CocoaPods

```zsh
# 安全起见可以先删除
sudo gem uninstall cocoapods

# OS 10.11之后（新版本方式）
sudo gem install cocoapods

# 旧版设置(新版无效)
pod setup

# 可选: 官方 repo 设置
git clone https://github.com/CocoaPods/Specs.git ~/.cocoapods/repos/master
# 可选: 清华源 repo 设置（新版本方式）
pod repo remove master
git clone https://mirrors.tuna.tsinghua.edu.cn/git/CocoaPods/Specs.git ~/.cocoapods/repos/master
# 可选: 清华源 repo 设置（旧版本方式）
pod repo add master https://mirrors.tuna.tsinghua.edu.cn/git/CocoaPods/Specs.git
pod repo update

## 验证安装
pod repo list
## 项目的podFile文件第一行添加以下指令
source 'https://mirrors.tuna.tsinghua.edu.cn/git/CocoaPods/Specs.git'

# 安装测试
pod search Alamofire

安装好了之后 如果执行pod install 报错 可能是因为没有勾选使用Rosetta打开 (应用程序-实用工具-终端-显示简介-勾选“Rosetta”)
就执行
sudo arch -x86_64 gem install ffi 
```

## Xcode 使用

### Xcode 的布局

The Toolbar 工具栏

![](IOS%20开发环境配置.assets/image-20240403060421.png)

The Project Navigator 项目导航器

![](IOS%20开发环境配置.assets/image-20240403060501.png)

The Other Navigators 其他子导航器

![](IOS%20开发环境配置.assets/image-20240403060537.png)

Inspectors 检查器

### 项目设置

![](IOS%20开发环境配置.assets/image-20240403060508.png)

### 资源目录

应用程序图标资源

![](IOS%20开发环境配置.assets/image-20240403060754.png)

PDF 资源

![](IOS%20开发环境配置.assets/image-20240403060813.png)

### Xcode 主题

### 自定义模拟器

### Xcode 源代码控制

### Storyboard 故事板界面布局

图层和文件大纲

![](IOS%20开发环境配置.assets/image-20240403061318.png)

View Controller 视图控制器

Inspectors 检查员

![](IOS%20开发环境配置.assets/image-20240403061443.png)

文件检查器是特定于 Storyboard 的。您可以禁用整个 Storyboard 的自动布局或大小类别。

身份检查器允许您将视图控制器连接到类。类是您的 Swift 文件 - 它们允许您编写动画和数据脚本以附加到您的对象。 Storyboard 中的视图控制器可以连接到 ViewController.swift 类文件，类似于将 javascript 文件包含到 HTML 文件中。

连接检查器管理视图控制器的对象与 Swift 文件代码之间的连接。稍后我们会看到更多的实际情况。


Object Library 对象库

![](IOS%20开发环境配置.assets/image-20240403061617.png)



The Media library 媒体库

![](IOS%20开发环境配置.assets/image-20240403061610.png)

## CocoaPods 使用

1. 终端进入 xcode 项目目录，创建 `Podfile` 初始文件

```zsh
cd project
pod init
```

2. 修改 Podfile 文件，管理依赖库项目

```
# 如果使用的清华源, 取消下行注释
# source 'https://mirrors.tuna.tsinghua.edu.cn/git/CocoaPods/Specs.git'

# 设置应用平台
platform :ios, '10.0'

# 隐藏所有警告
inhibit_all_warnings!

target 'FirstProject' do

  # 表明是为 Swift 项目, 依赖的库编译生成动态框架 .frameworkds，而不是 .a
  use_frameworks!

  # 默认使用最新版本依赖
  pod 'xxx'

  # 使用固定版本依赖
  pod 'xxx', '2.0.0'

  # 使用大约 6.0.x 版本范围依赖
  pod 'xxx', '~> 6.0.0'

  # 使用比较版本范围依赖，支持>=，>，<，<=
  pod 'xxx' , '<=1.0'

  # 使用本地依赖库， 支持指定自定义路径
  pod 'xxx', :path => '本地代码仓库的路径/xxx.podspec' 
  
  # 使用 git 仓库地址加载依赖库， 支持限定tag，branch和commit ID等
  pod 'xxx', :git => 'git仓库地址' , :tag => '2.2.2'
  pod 'xxx', :git => 'git仓库地址' , :branch => 'development'
  pod 'xxx', :git => 'git仓库地址' , :commit => 'abcdef123456'
  
  # 自定义控制警告信息的显示
  pod 'xxx', '~> 1.0.0', :inhibit_warnings => false

end
```

3. 安装/更新第三方库

```zsh
pod install
pod update
```

安装完成后会自动创建 `Pods` 目录、 `Podfile.lock` 文件、和 `.xcworkspace` 目录。
- `Pods` 目录用于存放所有第三方库的源代码文件、资源文件、头文件和静态库等内容。每个库都会在此目录下单独创建一个文件夹，以便项目能够按需引用这些库的资源和代码。然后主项目依赖 Pods 项目，将源码管理工作都迁移到了 Pods 项目中，而 Pods 项目最终会编译成一个名为 libPods.a 的静态库文件，主项目只需要依赖这个.a 文件即可。
- `Podfile.lock` 文件用于记录和锁定当前项目中当前使用的每个库的确切版本信息，以确保项目的每个成员都使用相同版本的第三方库。
- `project.xcworkspace` 目录中包含了一个用于包含和替代主 Xcode 项目和 Pods 中依赖项目的汇总工作空间文件。可以直接被 Xcode 打开，以便同时管理主项目和 Pods 依赖项目。

Pods 目录下下载了第三方库，此目录需要加入 .gitignore 文件中，避免随 git 提交. 文件配置可参考 [gitignore.io ](https://www.toptal.com/developers/gitignore)


对于资源文件，CocoaPods 提供了一个名为 Pods-resources.sh 的 bash 脚本，该脚本在每次项目编译的时候都会执行，将第三方库的各种资源文件复制到目标目录中。

- .podspec 库描述文件：包含了库基本描述、源码文件、依赖库、编译选项等信息。平常使用的 AFNetworing、SDWebImage 等三方库，都需要将自己的库描述文件提交到 cocoaPods 的官方远程索引库当中。

基本指令介绍

- pod install：重新解析依赖文件，会根据 (.podspec)库描述文件中的 source 找到库的源码地址，安装到项目中。如果发现项目中有 Podfile.lock 文件，直接执行该文件；若没有，执行 Podfile 文件，然后生成 Podfile.lock 文件;
- pod update：更新 repo 并重新解析依赖文件，不管是否有 Podfile.lock 文件，直接执行 Podfile 文件，然后生成 Podfile.lock 文件。
- pod update AFNetworking，更新指定库；
- pod init：为项目创建 Podfile 文件
- pod repo update：更新仓库信息
- pod setup：初始化、更新仓库信息。会把当前时间点的远端索引库 clone 到本地，并可以通过前往文件~/.cocoapods/repos/master/Specs  查看本地的索引库；
- pod search 库名：从本地仓库索引记录搜索库是否存在。第一次搜索会特别慢，因为会在 ~/Library/Caches/CocoaPods 路径下生成一个检索索引文件 search_index.json ，之后搜索会直接在该文件内查找，快很多。
- pod 集成三方库
- pod 更新远端库 

- 执行 pod install / pod update 指令时，会触发 cocoaPods 更新本地 Spec 仓库。

```zsh
# --verbose：查看详细的执行日志
# --no-repo-update : 告诉pod不用检测和更新本地spec仓库
pod install --verbose --no-repo-update 
pod update --verbose --no-repo-update 
```

4. 常用第三方库

> [!cite]
> https://www.jianshu.com/p/d 669 a 81 b 4 a 30
> https://github.com/Tim 9 Liu 9/TimLiu-iOS/blob/master/Swift.md
> https://flycoit.com/2017/08/03/%E 7%AC%AC%E 4%B 8%89%E 5%91%A 8-cocoapods%E 5%92%8 C%E 7%AC%AC%E 4%B 8%89%E 6%96%B 9%E 6%A 1%86%E 6%9 E%B 6/


```
platform :iOS, '8.0'

target 'CuteKids' do     #项目工程名
	# use_frameworks!

    pod 'AFNetworking','~> 3.1.0' #网络请求
    pod 'Reachability'            #网络情况监测

    pod 'YYModel' #数据解析
    pod 'JSONModel' #数据解析

    pod 'JSPatch'                 #JS和OC是通过JavaScriptCore互传消息的 (热修复)
    pod 'WebViewJavascriptBridge'    #OC、JS交互（,'~> 5.0' #OC、JS交互）


    pod 'MJRefresh'               #下拉刷新，上拉加载更多（拓展性强）

    pod 'SVProgressHUD'             #提示框 (pod 'MBProgressHUD', '~> 0.9') 都可以
    pod 'MBProgressHUD', '~> 0.9'   #提示框
    pod 'M13ProgressSuite','~> 1.2.7' #多风格的进程加载指示

    pod 'MWPhotoBrowser' #图片浏览
    pod 'SDWebImage'              #图片的加载及缓存
    pod 'SDCycleScrollView','~> 1.6' #无限轮播 

    pod 'FLEX', '~> 2.0', :configurations => ['Debug']   #Xcode界面调试工具
    pod 'Masonry','~> 1.0.2'      #约束建立
    pod 'UITableView+FDTemplateLayoutCell', '~> 1.5.beta' # 自动计算tableviewcell高度

    pod 'CYLTabBarController' #视图位置、响应

    pod 'ActionSheetPicker-3.0'   #地区选择

    pod 'IQKeyboardManager','~> 3.3.7'  #兼容IOS7    # 键盘


    pod 'YYText'   #富文本       聊天表情+文字并排
    pod 'ZSSRichTextEditor'               #富文本处理
    pod 'TTTAttributedLabel', '~> 1.13.3' # 富文本 文字视图效果

    pod 'ZBarSDK', '~> 1.3.1'                   # 扫描二维码，条形码
    pod 'LBXScan','~> 1.1.1' #二维码

    pod 'JDStatusBarNotification', '~> 1.5.2'  # 状态栏显示提醒信息

    pod 'KxMenu', '~> 1'  # 弹出式菜单



    pod 'FMDB/common' , '~>2.5'     #数据库
    pod 'FMDB/SQLCipher','~>2.5'    #数据库加解密
    pod 'LKDBHelper' #数据库

    pod 'MLeaksFinder'  #可以把它放在MobileProject_Local的target中这样就不会影响到产品环境 #内存泄露
    pod 'CocoaLumberjack','~> 2.0.0-rc'  #Mac和iOS上一个简捷、强大、灵活的日志框架
    pod 'UMengAnalytics-NO-IDFA'#友盟统计无IDFA版SDK

    pod 'skpsmtpmessage' #邮件发送

    pod 'BPushSDK', '~> 1.4.0-1'      # 百度推送
    pod 'GTSDK'  #个推SDK


    pod 'BaiduMapKit' #百度地图SDK

    pod 'UMengSocial', '~> 4.3'  #友盟社会化分享及第三方登录

    pod   'RongCloudIMKit', '~> 2.2.6'       # 融云第三方框架




    pod 'RegexKitLite', '4.0' #正则表达式

    pod 'XAspect' #轻量级、面向切面编程的库。允许你在每一个类和每一个实例中存在的方法里面加入任何代码。


      # Pods for CuteKids

      target 'CuteKids Tests' do
        inherit! :search_paths
        # Pods for testing
      end

    end


```


SwiftLint 安装和使用

- 安装
```zsh
brew install swiftlint
```
- 下载[配置文件](https://github.com/kodecocodes/swift-style-guide/blob/main/com.raywenderlich.swiftlint.yml)
- 为项目添加一个自动化脚本( `Project -> Build Phases ->  + -> New Run Script Phase` ), 并为其修改名字, 例如 `Format Code` , 再将其拖动到编译脚本前面 `Compile Sources` .
- 修改项目中( `Project -> Build Settings ->  All -> User Script Sandboxing` ) 为 `No`


```bash
export PATH="/opt/homebrew/bin:$PATH"

if [ -f ~/program/SwiftLint/com.raywenderlich.swiftlint.yml ]; then
  if which swiftlint >/dev/null; then
    swiftlint --no-cache --config ~/program/SwiftLint/com.raywenderlich.swiftlint.yml
  else
    echo "warning: SwiftLint not installed, download from https://github.com/realm/SwiftLint"
  fi
else
  if which swiftlint > /dev/null; then
    swiftlint
  else
    echo "warning: SwiftLint not installed, download from https://github.com/realm/SwiftLint"
  fi
fi
```


Sourcetree  安装和使用
