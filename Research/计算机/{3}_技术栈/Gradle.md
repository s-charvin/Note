# Gradle

## Gradle 使用

> [!cite]
> [Gradle6.5 User Guide](https://docs.gradle.org/6.5/userguide/userguide.html)
> [GradleLatest User Guide](https://docs.gradle.org/current/userguide/userguide.html)

### 安装

- 先决条件
    - `java -version` >= [1.8 ~ 23](https://docs.gradle.org/current/userguide/compatibility.html#compatibility)
    - 环境变量 `JAVA_HOME` 指向 JDK 目录.

```bash
brew install gradle
gradle -v
gradle init --type java-application  --dsl kotlin
# 或
gradle init --type java-application  --dsl groovy
```

### 基本命令

> [!tip]
> Gradle 支持 Kotlin 和 Groovy 两种语言来编写构建脚本. Kotlin 支持类型安全, 代码提示等特性, 同时新功能也会优先支持 Kotlin. 可以通过脚本文件名的后缀区分, 如 `build.gradle.kts` 和 `build.gradle`.

Gradle 项目目录结构:

```plaintext
.
├── build // 构建输出目录
├── .gradle // 缓存目录
│   └── ⋮
├── gradle
│   ├── libs.version.toml // 依赖版本管理(Gradle 7.0+ 支持)
│   └── wrapper
│       ├── gradle-wrapper.jar // Gradle Wrapper JAR 文件
│       └── gradle-wrapper.properties // Gradle Wrapper 配置文件
├── gradlew // 使用 wrapper 执行构建的脚本
├── gradlew.bat // 使用 wrapper 执行构建的脚本(Windows)
├── settings.gradle(.kts) // 定义子项目列表的项目设置文件
├── build.gradle(.kts) // 项目构建脚本(子项目会有)
└── ⋮ (其他项目文件)
```

Gradle Wrapper 是一个用于构建 Gradle 项目的脚本, 通过它可以在没有安装 Gradle 的情况下构建项目. 它会自动下载指定版本的 Gradle 并执行构建任务. 其中 `gradle-wrapper.properties` 包含了 Gradle Wrapper 的配置信息, 如下载地址, 版本等. `gradle-wrapper.jar` 包含了用于下载 Gradle 代码的 JAR 文件. 可以通过以下命令更新或创建 Gradle Wrapper:

```bash
./gradlew wrapper --gradle-version latest --distribution-type all
# 或
gradle wrapper --gradle-distribution-url https://services.gradle.org/distributions/gradle-7.0-bin.zip --gradle-distribution-sha256-sum 0e1
./gradlew --version # 查看 Gradle 版本
```

`gradlew` 和 `gradlew.bat` 分别是 Unix 和 Windows 类型系统下的 Gradle Wrapper 执行脚本, 可以通过它们执行 Gradle 任务. 例如:

```bash
# 一些默认任务
./gradlew tasks --all # 查看所有可执行任务
./gradlew jar # 执行构建可执行 JAR 文件的任务
./gradlew build # 执行完整的构建任务
./gradlew run # 执行运行任务
./gradlew clean # 执行清理任务

# 自定义任务
./gradlew :app:cusTask # 执行 app 子项目的自定义任务
```

Gradle 的构建过程从根项目开始, 递归构建子项目. 其中根项目可以通过 `settings.gradle(.kts)` 文件定义构建过程中需要一起构建的子项目列表. 同时每个项目都有一个(根项目可以没有)构建脚本 `build.gradle(.kts)` 定义了构建过程中需要执行的任务, 依赖等.

```kotlin
// settings.gradle.kts

plugins {
    id("org.gradle.toolchains.foojay-resolver-convention") version "0.7.0"
}

rootProject.name = "tutorial"
include("app")
```

```kotlin
// build.gradle.kts

plugins {
    // Apply the application plugin to add support for building a CLI application in Java.
    application
}

repositories {
    // Use Maven Central for resolving dependencies.
    mavenCentral()
}

dependencies {
    // Use JUnit Jupiter for testing.
    testImplementation(libs.junit.jupiter)

    testRuntimeOnly("org.junit.platform:junit-platform-launcher")

    // This dependency is used by the application.
    implementation(libs.guava)
}

// Apply a specific Java toolchain to ease working on different environments.
java {
    toolchain {
        languageVersion.set(JavaLanguageVersion.of(11))
    }
}

application {
    // Define the main class for the application.
    mainClass.set("running.tutorial.kotlin.App")
}

tasks.named<Test>("test") {
    // Use JUnit Platform for unit tests.
    useJUnitPlatform()
}
```

## Gradle 插件开发
