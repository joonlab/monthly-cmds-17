#!/usr/bin/env python3
"""Playwright 동적 페이지 스크래핑 (데모 사이트 — robots/ToS 안전).
pip install playwright && playwright install"""
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    b = p.chromium.launch(headless=True)   # 화면 보려면 headless=False
    page = b.new_page()
    page.goto("https://demo.playwright.dev/todomvc")
    page.wait_for_load_state("networkidle")  # JS 렌더 완료 대기

    page.get_by_placeholder("What needs to be done?").fill("배우기")
    page.keyboard.press("Enter")
    print(page.locator(".todo-list li").all_inner_texts())
    b.close()
