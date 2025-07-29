# 3.5" Resistive Touchscreen Configuration for Klipper-cyd

This configuration adds support for 3.5" resistive touchscreens to the Klipper-cyd project.

## Hardware

The configuration is designed for ESP32-based 3.5" resistive touchscreens with the following specifications:
- **Display**: 3.5" TFT with ST7796 driver
- **Resolution**: 480x320 pixels
- **Touch**: XPT2046 resistive touch controller
- **Interface**: SPI

## Configuration Files

### Board Configuration
- **File**: `boards/esp32-3248S035R.json`
- **Features**:
  - ST7796 display driver
  - XPT2046 resistive touch support
  - 480x320 resolution
  - Optimized UI scaling for 3.5" screen

### Device Driver
- **File**: `src/core/device/ESP32-3248S035R.cpp`
- **Features**:
  - Combined ST7796 display and XPT2046 touch handling
  - Proper pin assignments for resistive touch
  - LVGL integration

## Building

To build for the 3.5" resistive screen, use:

```bash
pio run -e esp32-3248S035R
```

## Pin Assignments

### Display Pins
- **TFT_BL**: GPIO 27 (Backlight)
- **TFT_MISO**: GPIO 12
- **TFT_MOSI**: GPIO 13
- **TFT_SCLK**: GPIO 14
- **TFT_CS**: GPIO 15
- **TFT_DC**: GPIO 2
- **TFT_RST**: Not connected (-1)

### Touch Pins
- **XPT2046_IRQ**: GPIO 36 (Interrupt)
- **XPT2046_MOSI**: GPIO 32
- **XPT2046_MISO**: GPIO 39
- **XPT2046_CLK**: GPIO 25
- **XPT2046_CS**: GPIO 33

## UI Configuration

The configuration includes optimized UI settings for 3.5" screens:
- **Screen dimensions**: 480x320 pixels
- **Button size**: 45x45 pixels minimum
- **Font sizes**: Montserrat 16 (normal), Montserrat 12 (small)
- **Sidebar width**: 50 pixels
- **Gap between elements**: 10 pixels

## Differences from Other Configurations

### vs 2.8" Resistive (esp32-2432S028R)
- Larger screen size (480x320 vs 320x240)
- Different display driver (ST7796 vs ILI9341)
- Updated UI scaling for larger screen
- Same resistive touch handling

### vs 3.5" Capacitive (esp32-3248S035C)
- Same screen size and display driver
- Resistive touch instead of capacitive (GT911)
- Different pin assignments for touch interface
- No LED RGB support (resistive screens typically don't have this)

## Troubleshooting

### Touch Not Working
1. Check pin connections for XPT2046
2. Verify SPI bus configuration
3. Ensure interrupt pin is properly connected

### Display Issues
1. Verify ST7796 driver is correct for your display
2. Check SPI frequency settings
3. Ensure backlight pin is connected

### Build Errors
1. Make sure all required libraries are installed
2. Verify board configuration is properly referenced in platformio.ini
3. Check that device driver file is included in the build

## Compatibility

This configuration should work with most ESP32-based 3.5" resistive touchscreens that use:
- ST7796 display controller
- XPT2046 touch controller
- Standard SPI interface

If your hardware uses different controllers, you may need to modify the driver files accordingly. 