#!/usr/bin/env python
"""
Configuration validation script
Проверяет, что все зависимости установлены и готовы к использованию
"""

import sys
import subprocess
from pathlib import Path


def check_python_version():
    """Проверить версию Python"""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8+ required")
        return False
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor}")
    return True


def check_required_files():
    """Проверить наличие необходимых файлов"""
    required_files = [
        "conftest.py",
        "pytest.ini",
        "requirements.txt",
        "src/pages/base_page.py",
        "src/pages/events_page.py",
        "src/components/base_component.py",
        "src/components/header.py",
        "src/components/filter_panel.py",
        "src/components/event_card.py",
        "tests/test_events_page.py",
    ]

    all_exist = True
    for file in required_files:
        path = Path(file)
        if path.exists():
            print(f"✅ {file}")
        else:
            print(f"❌ {file} - NOT FOUND")
            all_exist = False

    return all_exist


def check_packages():
    """Проверить установленные пакеты"""
    required_packages = [
        ("selenium", "Selenium WebDriver"),
        ("pytest", "Pytest Framework"),
        ("allure", "Allure Reporting"),
        ("dotenv", "Python-dotenv"),
        ("webdriver_manager", "WebDriver Manager"),
    ]

    print("\nChecking required packages:")
    all_installed = True

    for package, name in required_packages:
        try:
            __import__(package)
            print(f"✅ {name}")
        except ImportError:
            print(f"❌ {name} - NOT INSTALLED")
            all_installed = False

    return all_installed


def main():
    """Main validation"""
    print("=" * 60)
    print("GreenCity Tests - Configuration Validation")
    print("=" * 60)

    print("\n1. Python Version Check:")
    python_ok = check_python_version()

    print("\n2. Required Files Check:")
    files_ok = check_required_files()

    print("\n3. Required Packages Check:")
    packages_ok = check_packages()

    print("\n" + "=" * 60)

    if python_ok and files_ok and packages_ok:
        print("✅ ALL CHECKS PASSED - Ready to run tests!")
        print("\nQuick start:")
        print("  pytest -v")
        print("  pytest --alluredir=allure-results")
        print("  allure serve allure-results")
        return 0
    else:
        print("❌ SOME CHECKS FAILED")
        if not packages_ok:
            print("\nTo install missing packages:")
            print("  pip install -r requirements.txt")
        return 1


if __name__ == "__main__":
    sys.exit(main())
