#!/usr/bin/env python3
"""Playwright 로그인 세션 저장/재사용 패턴.
pip install playwright && playwright install
주의: state.json은 본인 사칭 가능한 쿠키 포함 → .gitignore 필수, 커밋 금지."""
from playwright.sync_api import sync_playwright

STATE = "state.json"

def save_auth():
    """1단계: 1회 로그인 후 인증상태(쿠키/스토리지)를 파일로 저장 (headed)."""
    with sync_playwright() as p:
        b = p.chromium.launch(headless=False)
        ctx = b.new_context()
        page = ctx.new_page()
        page.goto("https://github.com/login")
        # 데모: 직접 입력 대신 사용자가 화면에서 수동 로그인하도록 대기해도 됨
        # page.get_by_label("Username or email address").fill("USERNAME")
        # page.get_by_label("Password").fill("PASSWORD")
        # page.get_by_role("button", name="Sign in").click()
        input("로그인 완료 후 Enter...")  # 수동 로그인 대기(2FA 등)
        ctx.storage_state(path=STATE)
        b.close()
        print(f"saved -> {STATE}")

def use_auth():
    """2단계: 저장된 상태를 주입해 로그인 단계를 건너뛰고 바로 사용."""
    with sync_playwright() as p:
        b = p.chromium.launch(headless=True)
        ctx = b.new_context(storage_state=STATE)   # ★ 재사용
        page = ctx.new_page()
        page.goto("https://github.com/settings/profile")
        print("title:", page.title())
        b.close()

if __name__ == "__main__":
    import sys
    (save_auth if len(sys.argv) > 1 and sys.argv[1] == "save" else use_auth)()
