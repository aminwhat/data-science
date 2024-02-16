import ast

header1 = b"\x89PNG\r\n\x1a\n"  # PNG header
header2 = b"\xff\xd8\xff"  # JPEG header
header3 = b"\x42\x4d"  # BMP header
header4 = b"\x49\x49\x2a\x00"  # TIFF header
header5 = b"\x47\x49\x46\x38"  # GIF header
header6 = b"\x50\x4b\x03\x04"  # ZIP header
header7 = b"\x7fELF"  # ELF header
header8 = b"\x25\x50\x44\x46"  # PDF header
header9 = b"\x49\x44\x33"  # MP3 header
header10 = b"\xff\xfb"  # MPEG header
header11 = b"\x00\x00\x01\x00"  # PDDF header
header12 = b"\x00\x01\x00\x00"  # ICO header


def data_recovery(data):
    headers = {
        header1: "PNG",
        header2: "JPEG",
        header3: "BMP",
        header4: "TIFF",
        header5: "GIF",
        header6: "ZIP",
        header7: "ELF",
        header8: "PDF",
        header9: "MP3",
        header10: "MPEG",
        header11: "PDDF",
        header12: "ICO",
    }
    found_types = []
    for header, file_type in headers.items():
        if header in data:
            found_types.append(file_type)
    return found_types


data = ast.literal_eval(input())

found_types = data_recovery(data)
print(found_types)
