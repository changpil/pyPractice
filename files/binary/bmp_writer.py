def write_grayscale(filename, pixels):
    height = len(pixels)
    width = len(pixels[0])

    with open(filename, 'wb') as bmp:
        bmp.write(b'BM')

        size_bookmark = bmp.tell() # The next four bytes hold the filesize as a 32-bit
        bmp.write(b'\x00\x00\x00\x00') # little-endian integer

        bmp.write(b'\x00\x00\x00\x00') # should be 4 bytes zeros

        pixel_offset_bookmark = bmp.tell()
        bmp.write(b'\x00\x00\x00\x00')

        #Image Header
        bmp.write(b'\x28\x00\x00\x00')
        bmp.write(_int32_to_bytes(width))
        bmp.write(_int32_to_bytes(height))
        bmp.write(b'\x01\x00')
        bmp.write(b'\x08\x00')
        bmp.write(b'\x00\x00\x00\x00')
        bmp.write(b'\x00\x00\x00\x00')
        bmp.write(b'\x00\x00\x00\x00')
        bmp.write(b'\x00\x00\x00\x00')
        bmp.write(b'\x00\x00\x00\x00')
        bmp.write(b'\x00\x00\x00\x00')

        for c in range(256):
            bmp.write(bytes((c,c,c,0))) # Blue, Green, Red, Zero

        #Pixel data
        pixel_data_bookmark = bmp.tell()
        for row in reversed(pixels):
            row_data = bytes(row)
            bmp.write(row_data)
            padding = b'\x00' *((4-(len(row) %4))%4)
            bmp.write(padding)

        eof_bookmark = bmp.tell()
        bmp.seek(size_bookmark)
        bmp.write(_int32_to_bytes(eof_bookmark))
        bmp.seek(pixel_offset_bookmark)
        bmp.write(_int32_to_bytes(pixel_data_bookmark))


def _int32_to_bytes(i):
    return bytes((i     & 0xff,
                  i>>8  & 0xff,
                  i>>16 & 0xff,
                  i>>24 & 0xff))


import math
def mandel(real, imag):
    x = 0
    y = 0
    for i in range(1,257):
        if x*x + y*y > 4.0:
            break
        xt = real + x*x - y*y
        y = imag + 2.0 *x*y
        x = xt
    return int(math.log(i) *256 / math.log(256)) -1

def mandelbrot(size_x, size_y):
    return [[mandel((3.5*x/size_x)-2.5,
                    (2.0*y/size_y)-1.0)
              for x in range(size_x)]
              for y in range(size_y)]

def main():
    pixels = mandelbrot(448,256)
    import reprlib
    reprlib.repr(pixels)

    write_grayscale("mandel.bmp", pixels)

if __name__ == "__main__":
    main()