#!/usr/bin/pythoni3
""" UTF-8 Validation """

def validUTF8(data):
    num_bytes = 0

    mask1 = 1 << 7
    mask2 = 1 << 6

    for byte in data:
        byte = byte & 0xFF

        if num_bytes == 0:
            if (byte & mask1) == 0:
                continue
            elif (byte & mask1) != 0:
                count = 0
                mask = mask1
                while (byte & mask) != 0:
                    count += 1
                    mask = mask >> 1
                if count == 1 or count > 4:
                    return False
                num_bytes = count - 1
        else:
            if not (byte & mask1 and not (byte & mask2)):
                return False
            num_bytes -= 1

    return num_bytes == 0
