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
lastmod: 2024-05-08 13:03:14
---

# IOS 开发配置

## 基本开发环境

### 代理环境安装

Github 镜像加速方法
- 压缩包下载加速：
    - `https://mirror.ghproxy.com/[file url]`
    - 备用： `https://hub.gitmirror.com/[file url]`
    - 备用： `https://doc.fastgit.org/[file url]`
    - 示例： `https://mirror.ghproxy.com/https://github.com/stilleshan/dockerfiles/archive/master.zip`
- Clone 加速：
    - `https://mirror.ghproxy.com/[repo url]`
    - 备用： `https://gitclone.com/github.com/...`
    - 备用： `https://github.com.cnpmjs.org/[repo url]`
    - 示例： `git clone https://mirror.ghproxy.com/https://github.com/stilleshan/dockerfiles`

```
V2rayU 程序加速下载链接：
// arm64（m1）
https://mirror.ghproxy.com/https://github.com/yanue/V2rayU/releases/download/v3.8.0/V2rayU-arm64.dmg
// x86/x64
https://mirror.ghproxy.com/https://github.com/yanue/V2rayU/releases/download/v3.8.0/V2rayU-64.dmg

在终端使用代理：
export http_proxy=http://127.0.0.1:1087;export https_proxy=http://127.0.0.1:1087;export ALL_PROXY=socks5://127.0.0.1:1080



```

[v2box](https://apps.apple.com/us/app/v2box-v2ray-client/id6446814690?l=zh-Hans-CN)
[Furious](https://github.com/LorenEteval/Furious/releases)

### homebrew 安装及其清华源配置

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
(echo; echo 'eval "$(/opt/homebrew/bin/brew shellenv)"') >> /Users/charvin/.zprofile
test -r ~/.zprofile && echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
```

- Zsh 中设置默认源
```zsh
# 创建所需配置文件(如果没有,   有则不需创建)
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

### 常见系统软件安装

办公软件([Pages](https://apps.apple.com/us/app/pages/id409201541?mt=12),   [‎Keynote](https://apps.apple.com/us/app/keynote/id409183694?mt=12),   [Numbers](https://apps.apple.com/us/app/numbers/id409203825?mt=12),   [微信：自带截图和ocr工具](https://apps.apple.com/cn/app/%E5%BE%AE%E4%BF%A1/id836500024?mt=12))
跨端文件同步([OneDrive](https://apps.apple.com/us/app/onedrive/id823766827?mt=12))
程序管理([Lemon Cleaner](https://apps.apple.com/cn/app/%E8%85%BE%E8%AE%AF%E6%9F%A0%E6%AA%AC%E6%B8%85%E7%90%86-lemon-cleaner/id1449962996?mt=12))
浏览器([Chorme](https://www.google.com/chrome/),   [Edge](https://www.microsoft.com/en-us/edge/download))： `brew install --cask google-chrome`
笔记记录([Obsidian](https://obsidian.md/download))： `brew install --cask obsidian`
版本管理系统([Sourcetree](https://www.sourcetreeapp.com/))： `brew install --cask sourcetree`
brew 可视化界面([Cakebrew](https://www.cakebrew.com/))： `brew install cakebrew --cask`
SHH 客户端([Download Termius for Mac](https://termius.com/download/macos))： `brew install --cask termius`
开发工具预下载([Visual Studio Code November 2023](https://code.visualstudio.com/updates/v1_85))： `brew install --cask visual-studio-code`
字典工具([Easydict](https://github.com/tisfeng/Easydict))： `brew install --cask easydict`
苹果开发者前瞻([Releases · insidegui/WWDC](https://github.com/insidegui/WWDC/releases))： `brew install --cask wwdc`
鼠标和触控板适配设置（[scroll-reverser](http://pilotmoon.com/scrollreverser/)）： `brew install --cask scroll-reverser`
跨端鼠标共享([ShareMouse](https://www.sharemouse.com/download/)) 
剪切板管理([Maccy](https://github.com/p0deje/Maccy))： `brew install --cask maccy`
gif 录制工具([Gifox 2](https://gifox.app/))： `brew install --cask gifox`
终端录制工具([ttygif](https://github.com/icholy/ttygif))： `brew install ttygif`
截图工具([Snipaste](https://www.snipaste.com/)) `brew install --cask snipaste`
开发者工具箱(DevHub,   [He3](https://he3app.com/zh/))
离线文档查看工具([Dash](https://kapeli.com/dash))
文件差异比较([SourceGear | DiffMerge](https://sourcegear.com/diffmerge/downloads.html))： `brew install --cask diffmerge`
终端工具补充([hyper](https://github.com/vercel/hyper),   [tabby](https://github.com/Eugeny/tabby/))： `brew install --cask tabby` `brew install --cask hyper`
窗口切换工具([AltTab](https://alt-tab-macos.netlify.app/))： `brew install --cask alt-tab`
文件下载工具([Folx](https://www.mac-downloader.com/))
输入法([微信输入法](https://z.weixin.qq.com/))

### Iterm 安装及其配置

- 安装命令： `brew install --cask iterm2`
- 设置为默认终端：打开 iTerm,  在默认菜单中选择”Make iTerm 2 Default Term”
![](IOS%20开发环境配置.assets/截屏2024-04-07%2018.27.54.png)

#### 配置主题

- 主题[下载地址](https://github.com/mbadolato/iTerm 2-Color-Schemes),  下载并解压压缩包,  找到 ”schemes“ 文件夹. 
- 找到 Settings 配置界面中的 Profiles → Colors → Color Presets 
![](IOS%20开发环境配置.assets/Pasted%20image%2020240407183725.png)
- 点击 Color Presets ,  在其下拉列表中选择 Import. 然后在刚才解压的”schemes“  文件夹中选择自己想要的颜色配置方案文件进行导入. 
![](IOS%20开发环境配置.assets/Pasted%20image%2020240407184213.png)
- 重新点击 Color Presets ,  在其下拉列表中选择新导入的主题. 

#### 配置快捷键

- 配置 Split Pane 切换,  开启 Cmd + 数字切换命令行窗口方式. 同时可以使用 Cmd + Shift + Enter 放大某一个单独的窗口. 
- 新增 hot key window 配置,  使用快捷 Ctrl + ` 快速呼出iTerm窗口. 

#### 缩短终端用户名和主机名显示

```bash
#编辑配置文件
vim ~/.zshrc

#在文件最后增加 DEFAULT_USER="xxxxx" 配置
DEFAULT_USER="xxxxx"

#退出编辑后执行使配置生效
source ~/.zshrc 
```

#### 状态栏设置

- 找到 iTerm2 -> Settings 配置界面中的 Profiles → Session → 勾选 Status bar enable -> configure Status bar
![](IOS%20开发环境配置.assets/Pasted%20image%2020240407185748.png)
- 拖动自己想要的展示内容到下面空白处即可. 如果展示内容过多,  可以进入 Advanced -> 勾选 Prefer tight packing to stable positioning. 同时开启 auto-Rainbow
![](IOS%20开发环境配置.assets/Pasted%20image%2020240407191654.png)

#### 窗口设置

- 找到 iTerm2 -> Settings 配置界面中的 Profiles → Window 根据自己的需求设置窗口透明度、背景图片、行列数以及风格等. 
![](IOS%20开发环境配置.assets/Pasted%20image%2020240407193618.png)

#### 整体样式兼容设置

- 找到 iTerm2 -> Settings 配置界面中的 Appearence → General ,  将 Theme 改为 Minimal
![](IOS%20开发环境配置.assets/Pasted%20image%2020240407194050.png)

#### 解除终端历史行数限制

- 找到 iTerm2 -> Settings 配置界面中的 Profiles → Terminal ,  勾选 Unlimited scrollback
![](IOS%20开发环境配置.assets/Pasted%20image%2020240407195636.png)

#### 微调

问题：提示类插件的提示词清晰度不够
![](IOS%20开发环境配置.assets/Pasted%20image%2020240407210426.png)
- 提高颜色对比度. 找到 iTerm2 -> Settings 配置界面中的 Profiles → Colors ,  设置 Minimum Contrast 数值
![](IOS%20开发环境配置.assets/Pasted%20image%2020240407210414.png)

![](IOS%20开发环境配置.assets/Pasted%20image%2020240407210707.png)

#### 最终效果：

![](IOS%20开发环境配置.assets/Pasted%20image%2020240407195716.png)

### ohmyzsh 安装及其配置

- 直接安装命令
```zsh
# 镜像安装指令
sh -c "$(curl -fsSL https://gitee.com/mirrors/oh-my-zsh/raw/master/tools/install.sh)"
# 官方安装指令
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```
- 安装插件,   zoxide 支持历史地址快速跳转,  fzf 提供跳转选择框,   zsh-autosuggestions 提供命令自动补全,  zsh-syntax-highlighting 提供语法高亮显示
```zsh
brew install zsh-syntax-highlighting
echo "source $(brew --prefix)/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh" >> ~/.zshrc

brew install zsh-autosuggestions
echo "source $(brew --prefix)/share/zsh-autosuggestions/zsh-autosuggestions.zsh" >> ~/.zshrc


brew install zsh-autocomplete

brew install fzf
echo 'eval "$(fzf --zsh)"' >> ~/.zshrc

brew install zoxide

# 环境变量设置1：默认设置
echo 'eval "$(zoxide init zsh)"' >> ~/.zshrc
# 环境变量设置2：修改为 autojump 风格的 j 命令
echo 'eval "$(zoxide init zsh --cmd j)"' >> ~/.zshrc

source ~/.zshrc

# 使用提示：默认使用 z 匹配历史记录直接跳转
z anypath
# 使用提示：如果安装了 fzf,  zi 在有多个选择时就会出现可视化选择框让你选择,  如果只有一个则会直接跳转
zi anypath

# 使用提示：匹配历史记录直接跳转
j anypath
# 使用提示：如果安装了fzf,  ji在有多个选择时就会出现可视化选择框让你选择,  如果只有一个则会直接跳转
ji anypath
```

#### powerlevel10k 主题配置

- 下载 powerlevel10k 和注册主题
```zsh
brew install powerlevel10k
echo "source $(brew --prefix)/share/powerlevel10k/powerlevel10k.zsh-theme" >>~/.zshrc
```

重启终端,  进入 powerlevel10k 的配置过程(不小心退出时,  可以使用 p10k configure 命令重新进入)
- 最开始会自动询问是否下载字体,   选择是
- 如果没有询问,  则手动下载和安装字体：下载地址 [GitHub - romkatv/powerlevel10k: A Zsh theme](https://github.com/romkatv/powerlevel10k#meslo-nerd-font-patched-for-powerlevel10k),   并在 iterm 2 的 **Preferences > Profiles > Text > Font** 将字体设定为 MesloLGS NF

#### 最终效果

![](IOS%20开发环境配置.assets/Pasted%20image%2020240407215441.png)

### Xcode 安装及其版本管理

  
- 命令直接下载和安装 xcodes
```zsh
brew install --cask xcodes
```
- 通过 xcodes 安装指定版本的 xcode,   然后通过以下命令配置 xcode

#### Xcode 配置

- 设置代码出现的问题和错误仅在代码编辑器显示提示图标或标记,  而不显示详细信息. 
- 设置开启文件自动锁定和解锁,  便于多编辑器编码情景
- 设置显示文件扩展名
![](IOS%20开发环境配置.assets/Pasted%20image%2020240408164249.png)

- 开启代码折叠
- 开启列数代码指南为100
- 关闭代码行自动换行
![](IOS%20开发环境配置.assets/Pasted%20image%2020240408170005.png)

- 完全开启自动修剪尾随空格
![](IOS%20开发环境配置.assets/Pasted%20image%2020240408170319.png)

- 开启粘贴时重新缩进
- 开启大括号独行缩进控制
- 开启注释缩进控制
- 开启注释自动对齐
![](IOS%20开发环境配置.assets/Pasted%20image%2020240408171436.png)

- 设置 git 参数
![](IOS%20开发环境配置.assets/Pasted%20image%2020240408171847.png)

#### 安装和配置  Copilot for Xcode

- 安裝 [Node](https://nodejs.org/en) 
```
brew install node@20
echo 'export PATH="/opt/homebrew/opt/node@20/bin:$PATH"' >> ~/.zshrc

// 编译器可选设置
export LDFLAGS="-L/opt/homebrew/opt/node@20/lib"
export CPPFLAGS="-I/opt/homebrew/opt/node@20/include"
```
- 安装 Copilot for Xcode `brew install --cask copilot-for-xcode`
- 在系统设置的 `隐私与安全性 -> 扩展` 中点击 `Xcode Source Editor` ,   选中里面的 ` Copilot` 开启扩展.
![](IOS%20开发环境配置.assets/Pasted%20image%2020240408181021.png)
- 点击软件的 `General -> Refresh` 刷新权限,  并根据弹出提示,   设置 `accessibility Settings` 权限.
![](IOS%20开发环境配置.assets/Pasted%20image%2020240408181204.png)
- 点击软件的 `Service -> Github Copilot -> Github Copilot Language Server` 的 `install` 安装服务.
- 修改软件使用的集成终端为系统默认终端,   避免因为环境变量问题无法使用 node
![](IOS%20开发环境配置.assets/Pasted%20image%2020240408182214.png)
- 然后点击相同区域新出现的 `Sign In` 登录并进入 GitHub 的验证页面,   输入被自动放入剪切板的设备代码,   授权连接此设备; 
![](IOS%20开发环境配置.assets/Pasted%20image%2020240408182512.png)
- 再继续点击 `"Confirm Sign-in"` 完成登录验证.
- 点击软件的 `Feature -> Suggestion`  将 `Feature Provider` 设置为 `GitHub Copilot`
![](IOS%20开发环境配置.assets/Pasted%20image%2020240408182635.png)
- 通过 Xcode 创建或打开一个项目,   根据弹出提示允许 Copilot for Xcode 的文件访问权限.

#### 安装和配置代码检查和格式化工具 swift-format & SwiftLint

SwiftLint 安装和使用

- 安装
```zsh
brew install swiftlint
```
- 下载[配置文件](https://github.com/kodecocodes/swift-style-guide/blob/main/com.raywenderlich.swiftlint.yml)
```
curl -LJO https://github.com/kodecocodes/swift-style-guide/raw/main/com.raywenderlich.swiftlint.yml -o /Users/charvin/程序数据/SwiftLint/swiftlint.yml
```
- 根据需求修改配置文件,   比如修改缩进宽度为 4,   必须使用 self,   设置内容声明顺序等

```yml
# 指定不需要进行代码风格检查的文件或文件夹列表. 
excluded:
···

# 禁用的规则列表
disabled_rules:
···

# 分析器规则列表,  用于进行代码静态分析
analyzer_rules:
···
  - explicit_self

# 可选规则列表,  只有在明确选择时才会应用
opt_in_rules:
···
  - prefer_self_in_static_references
  - prefer_self_type_over_type_of_self
  - type_contents_order

# 自定义规则列表,  用于定义特定的代码风格检查规则
custom_rules:
···


# 缩进宽度的配置
indentation_width:
  indentation_width: 4

```

swift-format 安装和使用

```
brew install swift-format
```

#### CocoaPods 安装及其配置,  用于管理 Xcode 项目的依赖项

- 修改 gem 镜像源(无代理情况下)
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
# 需把可执行文件导入全局变量 PATH 中即可,  使用如下命令（安装后会有命令提示,   路径不同以提示为主）
echo 'export PATH="/opt/homebrew/opt/ruby/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc

# For compilers to find ruby you may need to set:
  export LDFLAGS="-L/opt/homebrew/opt/ruby/lib"
  export CPPFLAGS="-I/opt/homebrew/opt/ruby/include"
```

- 安装 CocoaPods

```zsh
sudo gem install cocoapods --verbose

# 如果中途错误,  重装后找不到pod,   则手动添加环境变量
echo 'export PATH="/opt/homebrew/lib/ruby/gems/3.3.0/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```
- 配置 CocoaPods
```
pod init
pod install

# 安装验证和测试
pod repo list
pod search Alamofire

# 后续更新时使用的指令
pod repo update
```
- 配置 CocoaPods (无代理情况下)
```
# 清华源 repo 设置
pod repo remove master
git clone https://mirrors.tuna.tsinghua.edu.cn/git/CocoaPods/Specs.git ~/.cocoapods/repos/tunaSpecs
# 可选: 清华源 repo 设置（上述方式不行再用）
pod repo add tunaSpecs https://mirrors.tuna.tsinghua.edu.cn/git/CocoaPods/Specs.git


# 安装验证和测试
pod repo list
pod search Alamofire

# 后续更新时使用的指令
pod repo update

# 注意: 使用非官方源,   需要在项目的 podFile 文件第一行添加源地址,   如下
source 'https://mirrors.tuna.tsinghua.edu.cn/git/CocoaPods/Specs.git'

安装好了之后 如果执行 pod install 报错 可能是因为没有勾选使用 Rosetta 打开 (应用程序-实用工具-终端-显示简介-勾选“Rosetta”)
就执行
sudo arch -x86_64 gem install ffi 
```

## Xcode 使用

### 创建 PlayGround 文件

xcode 的启动界面只提供了创建项目,   克隆远程项目和打开项目的功能.
![](IOS%20开发环境配置.assets/image-20240421125603.png)

每个项目会包含很多文件,   能够提供一个完整的程序搭建模板,   如果只需要考虑单代码文件情况,   编写一些试验性代码并实时查看结果,   可以通过 xcode 启动页面的左上角状态栏创建 playground 文件.

![](IOS%20开发环境配置.assets/image-20240421130109.png)

创建 playground 文件时,   可以选择基本的文件结构模板,   比如空白代码,   游戏页,   地图页和视图页.

![](IOS%20开发环境配置.assets/image-20240421130518.png)

每个 playground 打开后的界面共包含四部分:
- 最左侧是调试区域,   可以通过在指定代码行点击运行按钮,   编译和运行此代码行之前的所有代码.
- 最右侧是视图展示区域,   只有在代码中定义了视图,   并将视图通过 PlayGroundPage 进行展示后出现.
- 左侧第二个区域为代码区域.
- 最后一个是变量展示区域,   可以在代码运行后,   展示每一行所使用的变量值.

![](IOS%20开发环境配置.assets/image-20240421131428.png)

### 创建 Xcode 项目

通过点击 Xcode 启动界面的新项目创建按钮,   可以进入项目创建流程. 它首先会提供许多可以满足不同需求的起始项目模板,   包括跨平台,   IOS,   Macos 等. 

对于新手来说,   建议新创建一个 IOS 的基础项目,   如 App,   而不是跨平台的. 因为目前有些可以提高编程效率的工具,   还未支持跨平台项目. 除非你坚持完全使用官方所提供的开发环境.

![](IOS%20开发环境配置.assets/image-20240421132736.png)

然后是配置项目信息:
1. **Product Name**：应用程序的名称,  用户在手机或电脑上看到的名字. 例如,  如果正在开发一个计算器应用,  可能会将其命名为“超级计算器”. 
2. **Team**：开发者账号下的团队,  主要用于签名应用程序. 这里需要选择与 Apple 开发者账户关联的团队.
3. **Organization Identifier**：组织标识符通常是反向DNS格式的字符串,  用来唯一地标识开发团队或公司. 例如,  如果公司网站是 `example.com` ,  则可以设置为 `com.example` . 
4. **Bundle Identifier**：唯一标识应用程序的字符串,  通常是组织标识符后面跟上应用的名称. 比如 `com.example.SuperCalculator` . 这在App Store发布应用时必须唯一. 
5. **Interface**：界面设置通常指定应用支持的用户界面类型,  如Storyboard或SwiftUI等,   取决于选择的开发方法.
6. **Language**：这指的是应用编写时使用的主要编程语言,  如Swift或Objective-C. 
7. **Storage**：存储配置通常涉及到数据存储的选择,  如使用Core Data,  SQLite数据库或简单的文件存储等. 
8. **Host in CloudKit**：这个选项用于指定是否使用CloudKit来托管应用的数据. 启用后,  可以利用iCloud进行数据同步和存储. 
9. **Include Tests**：这个选项用于指定是否在项目中包含自动化测试,  通常有单元测试和UI测试. 启用测试有助于在开发过程中确保代码质量和功能正常.

![](IOS%20开发环境配置.assets/image-20240421133452.png)

点击下一步,  将整个项目文件夹保存到电脑的某个位置. 并开启 git 版本控制.
![](IOS%20开发环境配置.assets/image-20240421135120.png)

#### Xcode 项目布局

![](IOS%20开发环境配置.assets/image-20240421140409.png)


图中为完整的 Xcode 项目界面布局, 其主要被分成了五个部分, 每个部分都被红色框标出, 分别起着不同的作用：

1. **导航器区域（Navigator area）** - 界面左侧区域, 可以选择不同的导航器来进行不同的任务, 如项目文件和资源结构、搜索、版本控制历史记录等. 
2. **编辑器区域（Editor area）** - 界面中间大区域, 用于查看和编辑代码或进行界面设计.
3. **工具栏（Toolbar）** - 界面顶部的区域, 用于运行项目、查看版本分支、配置和构建项目、选择运行设备以及配置编辑器视图等. 
4. **实用工具区域（Utility area）** - 界面右侧的区域, 展示关于在编辑器中选中的文件或项目元素的详细信息和属性.
5. **调试区域（Debug area）** - 界面底部的区域, 在运行项目时用来显示输出和调试信息.

#### Toolbar 工具栏

![](IOS%20开发环境配置.assets/image-20240421164825.png)
图示为 Xcode 工具栏部分, 红色框选的各部分从左到右分别是:

1. **导航器控制按钮** - 控制是否显示或隐藏导航器区域
2. **运行按钮** - 三角形按钮用来编译和运行应用程序. 当程序正在运行或正在编译时, 旁边会出现一个停止按钮
3. **项目版本分支菜单** - 展示和控制当前项目的 git 版本分支
4. **Scheme菜单** - 显示和切换不同的编译配置(scheme), 一个 scheme 是一组程序进行编译、运行、测试、分析和部署设置的参数集合.
5. **设备选择菜单** - 选择运行应用的设备或模拟器.
6. **活动视图** - 显示当前项目的构建和运行状态, 例如是否正在构建、是否构建成功或失败。
7. **Xcode 云端管理** - 
8. **实用工具控制按钮** - 控制是否显示或隐藏实用工具区域

![](IOS%20开发环境配置.assets/image-20240421143619.png)


补充: 最右侧有个 ➕ , 用于打开 xcode 内置的资源库, 方便插入各种资源和代码片段到项目中. 具体来说, 其提供了以下几种插入选项:
- **视图 (View)**: 快速插入各种预定义的视图, 控件, 布局等到用户界面或用户代码中.
- **修饰符 (Modifiers)**: 
- **代码片段 (Snippets)**: 拖放基本的代码片段到代码编辑器中.
- **媒体 (Media)**: 插入工作区资产中的图片和其他媒体文件到用户界面或用户代码中.
- **颜色 (Color)**: 通过颜色选取器, 选择和插入颜色到代码中.
- **符号 (Symbols)**: 选择 Apple 体系的 SF Symbols 预定义符号集中的符号, 插入到用户界面或用户代码中.

#### Navigator 导航器

1. **项目导航器（Project Navigator）** - 显示项目中的文件和资源列表，你可以从这里快速访问任何项目文件。
2. **源代码管理导航器（Source Control Navigator）** - 提供对版本控制系统的访问，包括查看提交历史、分支和合并等操作。
3. **书签导航器（Bookmark Navigator）** - 设置和管理书签，方便快速跳转到代码中的特定部分。
4. **搜索导航器（Find Navigator）** - 允许你在整个项目中进行文本搜索和替换操作。
5. **问题导航器（Issue Navigator）** - 显示编译过程中出现的警告、错误和其他编译问题。
6. **测试导航器（Test Navigator）** - 列出所有的测试用例和测试套件，允许你运行和管理单元测试和UI测试。
7. **调试导航器（Debug Navigator）** - 当项目运行并进入调试模式时，展示了调试信息，如CPU、内存的使用情况以及线程和堆栈信息。
8. **断点导航器（Breakpoint Navigator）** - 管理项目中设置的所有断点，包括添加、删除和禁用断点。
9. **报告导航器（Report Navigator）** - 显示项目的构建历史，包括每次构建的详细结果和运行测试的输出。

![](IOS%20开发环境配置.assets/image-20240421145712.png)

#### Editor 编辑器

Xcode 的编辑器区域是多功能的, 根据在导航器区域选择的文件类型显示不同的编辑器视图:

- **项目编辑器**：用于查看和修改项目的设置，如应用的版本号、构建设置等。
- **代码编辑器**：显示和编辑`.swift`等代码文件，提供语法高亮、代码完成等功能。
- **视图编辑器**：在选择`.storyboard`文件时，提供图形界面来布局应用的视图和控制器。
- **资源编辑器**：用于管理`.xcassets`资源，如图片和图标，以可视化方式展示资源集。
- **应用配置编辑器**：编辑 `.plist` 配置文件，可以设置应用的配置选项和属性。
- **数据模型编辑器**：设计和编辑Core Data的数据模型。

#### Utility 实用工具

#### Debug 调试区域

Xcode的调试区域被设计用来帮助开发者在运行应用程序时诊断和解决问题。图中展示的部分包含了几个关键功能：

1. **变量查看器** - 在图像左侧的部分是变量查看器，其中“Auto”选项卡自动显示当前停止点上下文中的相关变量。开发者可以查看和修改变量的值，并通过“Local Variables”检查当前作用域中的变量，“All Variables, Registers, Globals and Statics”查看所有可访问的变量和寄存器。同时, 当进入调试过程后, 在变量查看器的上方会出现一系列按钮，可以用来控制调试过程，如继续执行、暂停、一步步执行代码等。右下方有一个搜索栏，允许过滤变量列表，快速找到需要查看的变量。
2. **控制台输出** - 这通常是调试区域的底部区域，在这个视图中不可见。它会显示标准输出和错误流，以及调试会话期间的其他日志信息。右下方有一个控制台的过滤和设置选项。你可以根据消息的类型（如 Debug, Error 等）来过滤控制台输出，让你更容易地关注重要的信息。
6. **元数据过滤器** - 这是一个弹出式菜单，允许你选择控制台显示的额外信息，如类型、时间戳、库、进程/线程标识（PID:TID）、子系统和类别。这有助于更深入地理解日志消息的上下文。

![](IOS%20开发环境配置.assets/image-20240421150024.png)

它通常包括控制台输出和变量监视器, 可以帮助开发者调试他们的应用程序. 

#### 项目格式化脚本

- 为项目添加一个自动化脚本( `Project -> Build Phases ->  + -> New Run Script Phase` ),   并为其修改名字,   例如 `Lint Code` ,   再将其拖动到编译脚本 `Compile Sources` 前面 .

- 修改项目中( `Project -> Build Settings ->  All -> User Script Sandboxing` ) 为 `No`

```bash
if [ -f ~/程序数据/SwiftLint/swiftlint.yml ]; then
  if which swiftlint >/dev/null; then
    swiftlint --config ~/程序数据/SwiftLint/swiftlint.yml --no-cache
  else
    echo "warning: SwiftLint not installed,   download from https://github.com/realm/SwiftLint"
  fi
else
  if which swiftlint > /dev/null; then
    swiftlint --no-cache
  else
    echo "warning: SwiftLint not installed,   download from https://github.com/realm/SwiftLint"
  fi
fi
```

### 编辑视图

![](IOS%20开发环境配置.assets/image-20240422212133.png)

#### 编辑快捷键

shift + 选中始末元素

command + D

command + =

选中后 + control + 点击拖拽: 设置对象与其他对象的联系, 如布局约束, 等.

选中后 + option + 点击拖拽: 复制元素, 并拖动到指定位置

选中后 + option + 移动鼠标: 查看选中元素与鼠标指向元素的距离

shift + 选中: 可以选中多个目标.

option + 滚轮滑动: 放大和缩小

#### 视图组件

#### 注意事项:

layer.cornerRadius 应该和 Clip to Bounds 一起使用
layer.shadowOpacity, layer.shadowRadius 和 layer.shadowOffset 应该不和 Clip to Bounds 一起使用
代码创建的视图，且使用 Auto Layout 进行布局时，需将视图的 translatesAutoresizingMaskIntoConstraints 属性值设为 false

### 自动布局

Alignment Constraints

Leading Edges
Trailing Edges
Top Edges
Bottom Edges
Horizontal Centers
Vertical Centers
Baselines
Horizontally in Container
Vertically in Container

Pin Constraints


Spacing to nearest neighbor
Constrain to margins
width
Height
Equal Widths
Equal Heights
Aspect Ratio

Resolve Auto Layout Issues

### 在 XCode 中手动安装 iOS 模拟器

找到下载地址

1. 打开 XCode, 点击桌面左上角状态栏的 `Xcode > Settings` 打开设置窗口, 在其内部的 `Platforms > ➕ > IOS` 查看所有可供下载的模拟器列表.
![](IOS%20开发环境配置.assets/image-20240422132644.png)
2. 单击要下载的模拟器, 点击窗口右下角的下载和安装按钮以开始正常的下载过程. 在此示例中, 我正在下载 iOS 15.5 模拟器.
![](IOS%20开发环境配置.assets/image-20240422133114.png)
![](IOS%20开发环境配置.assets/image-20240422133916.png)


3. 打开 Console.app 控制台程序, 并确保正在查看“所有消息”选项卡, 点击开始. 此时控制台会追踪当前运行程序的日志记录.
![](IOS%20开发环境配置.assets/image-20240422133443.png)
4. 先取消 xcode 模拟器的下载, 然后暂停控制台的追踪.
![](IOS%20开发环境配置.assets/image-20240422134058.png)
5. 搜索 xcode 的模拟器下载记录, 搜索关键词为 `Download Cancelled` , 然后在搜索到的条目中就可以找到当前取消下载的模拟器的下载链接.
![](IOS%20开发环境配置.assets/image-20240422134319.png)

6. 通过以下命令, 下载模拟器文件到 xcode 缓存目录中.
```bash
curl -o ~/Library/Caches/com.apple.dt.Xcode/Downloads/com.apple.pkg.iPhoneSimulatorSDK15_5-15.5.1.1653527639.dmg https://devimages-cdn.apple.com/downloads/xcode/simulators/com.apple.pkg.iPhoneSimulatorSDK15_5-15.5.1.1653527639.dmg

# 如果下载速度很慢, 可以通过 aria2 进行并行加速下载. 下载命令如下
# 需要先安装 aria2
# brew install aria2
aria2c -x 16 -s 16 -o ~/Library/Caches/com.apple.dt.Xcode/Downloads/com.apple.pkg.iPhoneSimulatorSDK15_5-15.5.1.1653527639.dmg https://devimages-cdn.apple.com/downloads/xcode/simulators/com.apple.pkg.iPhoneSimulatorSDK15_5-15.5.1.1653527639.dmg --console-log-level=warn

```

7. 重新返回模拟器下载页面, 点击模拟器开始下载, 此时因为已经有了缓存文件, 会略过下载流程, 直接开始安装.


> [!TODO]
> 安装模拟器后, 模拟器只有一部分出现在了设备选择栏中, 有些不能使用.

### Xcode 主题

### 自定义模拟器

### Xcode 源代码控制

### Storyboard 故事板界面布局

图层和文件大纲

![](IOS%20开发环境配置.assets/image-20240403061318.png)

View Controller 视图控制器

Inspectors 检查员

![](IOS%20开发环境配置.assets/image-20240403061443.png)

文件检查器是特定于 Storyboard 的. 您可以禁用整个 Storyboard 的自动布局或大小类别. 

身份检查器允许您将视图控制器连接到类. 类是您的 Swift 文件 - 它们允许您编写动画和数据脚本以附加到您的对象.  Storyboard 中的视图控制器可以连接到 ViewController.swift 类文件,  类似于将 javascript 文件包含到 HTML 文件中. 

连接检查器管理视图控制器的对象与 Swift 文件代码之间的连接. 稍后我们会看到更多的实际情况. 


Object Library 对象库

![](IOS%20开发环境配置.assets/image-20240403061617.png)



The Media library 媒体库

![](IOS%20开发环境配置.assets/image-20240403061610.png)

## CocoaPods 使用

1. 终端进入 xcode 项目目录,  创建 `Podfile` 初始文件

```zsh
cd project
pod init
```

2. 修改 Podfile 文件,  管理依赖库项目

```
# 如果使用的清华源,   取消下行注释
# source 'https://mirrors.tuna.tsinghua.edu.cn/git/CocoaPods/Specs.git'

# 设置应用平台
platform :ios,   '10.0'

# 隐藏所有警告
inhibit_all_warnings!

target 'FirstProject' do

  # 表明是为 Swift 项目,   依赖的库编译生成动态框架 .frameworkds,  而不是 .a
  use_frameworks!

  # 默认使用最新版本依赖
  pod 'xxx'

  # 使用固定版本依赖
  pod 'xxx',   '2.0.0'

  # 使用大约 6.0.x 版本范围依赖
  pod 'xxx',   '~> 6.0.0'

  # 使用比较版本范围依赖,  支持>=,  >,  <,  <=
  pod 'xxx' ,   '<=1.0'

  # 使用本地依赖库,   支持指定自定义路径
  pod 'xxx',   :path => '本地代码仓库的路径/xxx.podspec' 
  
  # 使用 git 仓库地址加载依赖库,   支持限定tag,  branch和commit ID等
  pod 'xxx',   :git => 'git仓库地址' ,   :tag => '2.2.2'
  pod 'xxx',   :git => 'git仓库地址' ,   :branch => 'development'
  pod 'xxx',   :git => 'git仓库地址' ,   :commit => 'abcdef123456'
  
  # 自定义控制警告信息的显示
  pod 'xxx',   '~> 1.0.0',   :inhibit_warnings => false

end
```

3. 安装/更新第三方库

```zsh
pod install
pod update
```

安装完成后会自动创建 `Pods` 目录、 `Podfile.lock` 文件、和 `.xcworkspace` 目录. 
- `Pods` 目录用于存放所有第三方库的源代码文件、资源文件、头文件和静态库等内容. 每个库都会在此目录下单独创建一个文件夹,  以便项目能够按需引用这些库的资源和代码. 然后主项目依赖 Pods 项目,  将源码管理工作都迁移到了 Pods 项目中,  而 Pods 项目最终会编译成一个名为 libPods.a 的静态库文件,  主项目只需要依赖这个.a 文件即可. 
- `Podfile.lock` 文件用于记录和锁定当前项目中当前使用的每个库的确切版本信息,  以确保项目的每个成员都使用相同版本的第三方库. 
- `project.xcworkspace` 目录中包含了一个用于包含和替代主 Xcode 项目和 Pods 中依赖项目的汇总工作空间文件. 可以直接被 Xcode 打开,  以便同时管理主项目和 Pods 依赖项目. 

Pods 目录下下载了第三方库,  此目录需要加入 .gitignore 文件中,  避免随 git 提交. 文件配置可参考 [gitignore.io ](https://www.toptal.com/developers/gitignore)


对于资源文件,  CocoaPods 提供了一个名为 Pods-resources.sh 的 bash 脚本,  该脚本在每次项目编译的时候都会执行,  将第三方库的各种资源文件复制到目标目录中. 

- .podspec 库描述文件：包含了库基本描述、源码文件、依赖库、编译选项等信息. 平常使用的 AFNetworing、SDWebImage 等三方库,  都需要将自己的库描述文件提交到 cocoaPods 的官方远程索引库当中. 

基本指令介绍

- pod install：重新解析依赖文件,  会根据 (.podspec)库描述文件中的 source 找到库的源码地址,  安装到项目中. 如果发现项目中有 Podfile.lock 文件,  直接执行该文件；若没有,  执行 Podfile 文件,  然后生成 Podfile.lock 文件;
- pod update：更新 repo 并重新解析依赖文件,  不管是否有 Podfile.lock 文件,  直接执行 Podfile 文件,  然后生成 Podfile.lock 文件. 
- pod update AFNetworking,  更新指定库；
- pod init：为项目创建 Podfile 文件
- pod repo update：更新仓库信息
- pod setup：初始化、更新仓库信息. 会把当前时间点的远端索引库 clone 到本地,  并可以通过前往文件~/.cocoapods/repos/master/Specs  查看本地的索引库；
- pod search 库名：从本地仓库索引记录搜索库是否存在. 第一次搜索会特别慢,  因为会在 ~/Library/Caches/CocoaPods 路径下生成一个检索索引文件 search_index.json ,  之后搜索会直接在该文件内查找,  快很多. 
- pod 集成三方库
- pod 更新远端库 

- 执行 pod install / pod update 指令时,  会触发 cocoaPods 更新本地 Spec 仓库. 

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
platform :iOS,   '8.0'

target 'CuteKids' do     #项目工程名
	# use_frameworks!

    pod 'AFNetworking',  '~> 3.1.0' #网络请求
    pod 'Reachability'            #网络情况监测

    pod 'YYModel' #数据解析
    pod 'JSONModel' #数据解析

    pod 'JSPatch'                 #JS和OC是通过JavaScriptCore互传消息的 (热修复)
    pod 'WebViewJavascriptBridge'    #OC、JS交互（,  '~> 5.0' #OC、JS交互）


    pod 'MJRefresh'               #下拉刷新,  上拉加载更多（拓展性强）

    pod 'SVProgressHUD'             #提示框 (pod 'MBProgressHUD',   '~> 0.9') 都可以
    pod 'MBProgressHUD',   '~> 0.9'   #提示框
    pod 'M13ProgressSuite',  '~> 1.2.7' #多风格的进程加载指示

    pod 'MWPhotoBrowser' #图片浏览
    pod 'SDWebImage'              #图片的加载及缓存
    pod 'SDCycleScrollView',  '~> 1.6' #无限轮播 

    pod 'FLEX',   '~> 2.0',   :configurations => ['Debug']   #Xcode界面调试工具
    pod 'Masonry',  '~> 1.0.2'      #约束建立
    pod 'UITableView+FDTemplateLayoutCell',   '~> 1.5.beta' # 自动计算tableviewcell高度

    pod 'CYLTabBarController' #视图位置、响应

    pod 'ActionSheetPicker-3.0'   #地区选择

    pod 'IQKeyboardManager',  '~> 3.3.7'  #兼容IOS7    # 键盘


    pod 'YYText'   #富文本       聊天表情+文字并排
    pod 'ZSSRichTextEditor'               #富文本处理
    pod 'TTTAttributedLabel',   '~> 1.13.3' # 富文本 文字视图效果

    pod 'ZBarSDK',   '~> 1.3.1'                   # 扫描二维码,  条形码
    pod 'LBXScan',  '~> 1.1.1' #二维码

    pod 'JDStatusBarNotification',   '~> 1.5.2'  # 状态栏显示提醒信息

    pod 'KxMenu',   '~> 1'  # 弹出式菜单



    pod 'FMDB/common' ,   '~>2.5'     #数据库
    pod 'FMDB/SQLCipher',  '~>2.5'    #数据库加解密
    pod 'LKDBHelper' #数据库

    pod 'MLeaksFinder'  #可以把它放在MobileProject_Local的target中这样就不会影响到产品环境 #内存泄露
    pod 'CocoaLumberjack',  '~> 2.0.0-rc'  #Mac和iOS上一个简捷、强大、灵活的日志框架
    pod 'UMengAnalytics-NO-IDFA'#友盟统计无IDFA版SDK

    pod 'skpsmtpmessage' #邮件发送

    pod 'BPushSDK',   '~> 1.4.0-1'      # 百度推送
    pod 'GTSDK'  #个推SDK


    pod 'BaiduMapKit' #百度地图SDK

    pod 'UMengSocial',   '~> 4.3'  #友盟社会化分享及第三方登录

    pod   'RongCloudIMKit',   '~> 2.2.6'       # 融云第三方框架




    pod 'RegexKitLite',   '4.0' #正则表达式

    pod 'XAspect' #轻量级、面向切面编程的库. 允许你在每一个类和每一个实例中存在的方法里面加入任何代码. 


      # Pods for CuteKids

      target 'CuteKids Tests' do
        inherit! :search_paths
        # Pods for testing
      end

    end


```



Sourcetree  安装和使用
