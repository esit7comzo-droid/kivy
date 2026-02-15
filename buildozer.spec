[app]

title = MyApp
package.name = myapp
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1

requirements = python3,kivy

orientation = portrait
fullscreen = 0


[buildozer]
log_level = 2
warn_on_root = 1


# 🔽 Android 설정
[app:android]

# 최소 Android 5.0
android.minapi = 21

# SDK / Target
android.api = 33
android.target = 33

# 🔥 build-tools 완전 고정 (37-rc1 차단 핵심)
android.build_tools_version = 33.0.2

# 안정 NDK
android.ndk = 25b

# SDK 자동 업데이트 방지
android.skip_update = True

# 라이선스 자동 승인
android.accept_sdk_license = True

# 필요 시 권한 추가
# android.permissions = INTERNET
