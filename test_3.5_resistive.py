#!/usr/bin/env python3
"""
Test script for 3.5" resistive touchscreen configuration
Validates board configuration and device driver files
"""

import json
import os
import re

def test_board_config():
    """Test the board configuration JSON file"""
    print("Testing board configuration...")
    
    config_path = "CYD-Klipper/boards/esp32-3248S035R.json"
    
    if not os.path.exists(config_path):
        print(f"❌ Board config file not found: {config_path}")
        return False
    
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
        
        # Check required fields
        required_fields = ['build', 'name', 'frameworks', 'upload']
        for field in required_fields:
            if field not in config:
                print(f"❌ Missing required field: {field}")
                return False
        
        # Check build configuration
        build = config['build']
        if 'extra_flags' not in build:
            print("❌ Missing extra_flags in build config")
            return False
        
        extra_flags = build['extra_flags']
        
        # Check for required defines
        required_defines = [
            'CYD_SCREEN_DRIVER_ESP32_3248S035R',
            'ST7796_DRIVER',
            'CYD_SCREEN_WIDTH_PX=480',
            'CYD_SCREEN_HEIGHT_PX=320'
        ]
        
        for define in required_defines:
            if not any(define in flag for flag in extra_flags):
                print(f"❌ Missing required define: {define}")
                return False
        
        print("✅ Board configuration is valid")
        return True
        
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON in board config: {e}")
        return False
    except Exception as e:
        print(f"❌ Error testing board config: {e}")
        return False

def test_device_driver():
    """Test the device driver C++ file"""
    print("Testing device driver...")
    
    driver_path = "CYD-Klipper/src/core/device/ESP32-3248S035R.cpp"
    
    if not os.path.exists(driver_path):
        print(f"❌ Device driver file not found: {driver_path}")
        return False
    
    try:
        with open(driver_path, 'r') as f:
            content = f.read()
        
        # Check for required includes and defines
        required_patterns = [
            r'#ifdef CYD_SCREEN_DRIVER_ESP32_3248S035R',
            r'#include <XPT2046_Touchscreen\.h>',
            r'#include <TFT_eSPI\.h>',
            r'XPT2046_Touchscreen touchscreen',
            r'void screen_setup\(\)',
            r'void screen_lv_touchRead\(',
            r'#endif // CYD_SCREEN_DRIVER_ESP32_3248S035R'
        ]
        
        for pattern in required_patterns:
            if not re.search(pattern, content):
                print(f"❌ Missing required pattern: {pattern}")
                return False
        
        print("✅ Device driver is valid")
        return True
        
    except Exception as e:
        print(f"❌ Error testing device driver: {e}")
        return False

def test_platformio_config():
    """Test the platformio.ini configuration"""
    print("Testing platformio.ini configuration...")
    
    ini_path = "CYD-Klipper/platformio.ini"
    
    if not os.path.exists(ini_path):
        print(f"❌ platformio.ini not found: {ini_path}")
        return False
    
    try:
        with open(ini_path, 'r') as f:
            content = f.read()
        
        # Check for our environment
        if '[env:esp32-3248S035R]' not in content:
            print("❌ Missing esp32-3248S035R environment in platformio.ini")
            return False
        
        # Check for required libraries
        required_libs = [
            'XPT2046_Touchscreen.git',
            'TFT_eSPI.git',
            'lvgl'
        ]
        
        for lib in required_libs:
            if lib not in content:
                print(f"❌ Missing required library: {lib}")
                return False
        
        print("✅ PlatformIO configuration is valid")
        return True
        
    except Exception as e:
        print(f"❌ Error testing platformio.ini: {e}")
        return False

def test_ci_integration():
    """Test that the CI script includes our configuration"""
    print("Testing CI integration...")
    
    ci_path = "ci.py"
    
    if not os.path.exists(ci_path):
        print(f"❌ CI script not found: {ci_path}")
        return False
    
    try:
        with open(ci_path, 'r') as f:
            content = f.read()
        
        if '"esp32-3248S035R"' not in content:
            print("❌ esp32-3248S035R not found in CI script")
            return False
        
        print("✅ CI integration is valid")
        return True
        
    except Exception as e:
        print(f"❌ Error testing CI integration: {e}")
        return False

def main():
    """Run all tests"""
    print("🧪 Testing 3.5\" Resistive Touchscreen Configuration\n")
    
    tests = [
        test_board_config,
        test_device_driver,
        test_platformio_config,
        test_ci_integration
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Configuration is ready to use.")
        print("\nTo build the firmware:")
        print("cd CYD-Klipper")
        print("pio run -e esp32-3248S035R")
    else:
        print("❌ Some tests failed. Please check the configuration.")
    
    return passed == total

if __name__ == "__main__":
    main() 