[app]
title = SnakeGame
package.name = snakegame
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv

version = 0.1

requirements = python3,kivy

orientation = portrait

fullscreen = 1

# ====== Android 关键配置 ======
android.api = 33
android.minapi = 21

# 🔥 核心：禁止 buildozer 自己下载 SDK / build-tools
android.skip_update = True

# 避免 buildozer 乱猜 build-tools
android.accept_sdk_license = False

# 架构
android.archs = arm64-v8a

# ====== 日志 & 调试 ======
log_level = 2
