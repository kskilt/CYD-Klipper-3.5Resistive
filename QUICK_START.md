# Quick Start Guide: 3.5" Resistive Touchscreen

## What You Need

### Hardware
- ESP32-based 3.5" resistive touchscreen
- ST7796 display controller
- XPT2046 resistive touch controller
- USB cable for programming

### Software
- PlatformIO (for building)
- ESP32 development tools

## Getting Started

### 1. Build the Firmware

```bash
# Navigate to the project directory
cd CYD-Klipper-3.5Resistive/CYD-Klipper

# Build for 3.5" resistive screen
pio run -e esp32-3248S035R

# Upload to your device
pio run -e esp32-3248S035R --target upload
```

### 2. Wire Your Hardware

Connect your 3.5" resistive screen to the ESP32:

```
Display Connections:
ESP32 Pin 27 → Backlight
ESP32 Pin 12 → TFT MISO
ESP32 Pin 13 → TFT MOSI
ESP32 Pin 14 → TFT SCLK
ESP32 Pin 15 → TFT CS
ESP32 Pin  2 → TFT DC
(GND → TFT GND)
(3.3V → TFT VCC)

Touch Connections:
ESP32 Pin 36 → Touch IRQ
ESP32 Pin 32 → Touch MOSI
ESP32 Pin 39 → Touch MISO
ESP32 Pin 25 → Touch CLK
ESP32 Pin 33 → Touch CS
(GND → Touch GND)
(3.3V → Touch VCC)
```

### 3. Configure Your Printer

1. Power on the device
2. Connect to the WiFi network "CYD-Klipper"
3. Navigate to the device's IP address (usually 192.168.4.1)
4. Configure your printer settings
5. Connect to your Klipper instance

## Features

### Display
- **Resolution**: 480x320 pixels
- **Size**: 3.5 inches
- **Type**: Resistive touch
- **Colors**: 16-bit color depth

### Touch
- **Type**: Resistive (works with any pressure)
- **Controller**: XPT2046
- **Calibration**: Automatic
- **Multi-touch**: Single touch only

### UI
- **Buttons**: 45x45 pixels minimum
- **Fonts**: Montserrat 16pt (normal), 12pt (small)
- **Sidebar**: 50 pixels wide
- **Gap**: 10 pixels between elements

## Troubleshooting

### Display Not Working
- Check all display connections
- Verify 3.3V power supply
- Ensure backlight is connected to GPIO 27

### Touch Not Responding
- Verify all touch connections
- Check that IRQ pin (GPIO 36) is connected
- Ensure touch controller has power

### Build Errors
- Make sure PlatformIO is installed
- Verify all required libraries are available
- Check that you're in the correct directory

### WiFi Issues
- Default network: "CYD-Klipper"
- Default IP: 192.168.4.1
- Password: Check device documentation

## Configuration Options

### Screen Rotation
The screen can be rotated by setting the `rotate_screen` option in the configuration.

### Brightness
Brightness can be adjusted through the UI settings or via configuration.

### Touch Sensitivity
The resistive touch is pressure-sensitive and should work with any stylus or finger pressure.

## Support

If you encounter issues:
1. Check the wiring connections
2. Verify your hardware matches the specifications
3. Review the troubleshooting section
4. Check the main documentation in `README_3.5_Resistive.md`

## Next Steps

After successful setup:
1. Configure your printer settings
2. Set up your Klipper instance
3. Customize the UI if needed
4. Enjoy your 3.5" resistive touchscreen interface! 