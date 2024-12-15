import qrcode

def generate_qr_code(data, filename="qrcode.png", box_size=10, border=4):
    
    qr = qrcode.QRCode(
        version=None,  # Automatically determine size
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=box_size,
        border=border,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color=black, back_color=white)
    img.save(filename)
    print(f"QR code saved as {filename}")

if __name__ == "__main__":
    print("Welcome to the QR Code Generator!")
    data = input("Enter the data to encode in the QR code: ")
    filename = input("Enter the filename to save the QR code (default: qrcode.png): ") or "qrcode.png"

    try:
        box_size = int(input("Enter the box size (default: 10): ") or 10)
        border = int(input("Enter the border size (default: 4): ") or 4)
        
        generate_qr_code(data, filename, box_size, border)
    except ValueError:
        print("Error: Please enter valid numeric values for box size and border.")
