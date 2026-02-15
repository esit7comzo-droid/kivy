[app]

title = MyApp
package.name = myapp
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1
requirements = python3,kivy

orientation = portrait


[buildozer]
log_level = 2


[app:android]

android.minapi = 21
android.api = 33
android.target = 33

# 🔥 핵심 1: 프리뷰 비활성화
android.skip_update = True

# 🔥 핵심 2: build-tools 강제 고정
android.build_tools_version = 33.0.2

# 🔥 핵심 3: NDK 고정
android.ndk = 25b

# 라이선스 자동 승인
android.accept_sdk_license = True
