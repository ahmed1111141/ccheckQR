# QR Code Generator

## Overview
The QR Code Generator is a simple and interactive application that allows users to create customizable QR codes. The application is built using Python and features a user-friendly interface designed with `tkinter`.

## Features
- **Real-Time QR Code Generation**: The QR code updates live as the user types.
- **Customizable Colors**: Choose foreground and background colors for the QR code.
- **Save Option**: Save the generated QR code as a PNG file.
- **Clear Input**: Clear the input field and QR code preview with a single click.

## Requirements
To run the application, ensure you have the following installed:
- Python 3.x
- Required Python libraries:
  - `qrcode`
  - `pillow`
  - `tkinter` (usually included with Python)

## Installation
1. Clone this repository or download the source code.
2. Install the required libraries by running:
   ```bash
   pip install qrcode[pil]
   ```

## Usage
1. Run the application:
   ```bash
   python qr_code_generator.py
   ```
2. Enter text or a URL into the input field.
3. Select optional foreground and background colors.
4. Click "Generate QR" to display the QR code.
5. Use the "Save" button to save the QR code as a PNG file.
6. Click "Clear" to reset the input and preview.



## File Structure
```
qr_code_generator/
|-- qr_code_generator.py  # Main application file
|-- README.md             # Readme file
```

## License
This project is licensed under the MIT License. Feel free to use and modify it as needed.

## Contributions
Contributions are welcome! If you have any ideas or improvements, feel free to submit a pull request or open an issue.

