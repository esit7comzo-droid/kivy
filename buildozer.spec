[app]

# 앱 정보
title = MyApp
package.name = myapp
package.domain = org.example
version = 0.1

# 소스 설정
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# 필요한 라이브러리
requirements = python3,kivy

# 화면 방향
orientation = portrait

# 전체화면 여부
fullscreen = 0


[buildozer]

log_level = 2
warn_on_root = 1


# 🔽 Android 설정
[app:android]

# 최소 지원 버전 (Android 5.0)
android.minapi = 21

# 타겟 SDK
android.target = 33

# 컴파일 SDK
android.api = 33

# NDK 버전 (자동이면 보통 주석 가능)
# android.ndk = 25b

# 권한 예시 (필요하면 추가)
# android.permissions = INTERNET
