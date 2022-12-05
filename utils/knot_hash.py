from functools import reduce

def knot_hash(data):
    ascii_characters = [ord(c) for c in data] + [17, 31, 73, 47, 23]
    knot = [i for i in range(256)]
    current_position, skip_size = 0, 0
    for j in range(64):
        for i in ascii_characters:
            copied_data = knot[:] + knot[:]
            length = int(i)
            copied_data[current_position:current_position + length] = copied_data[current_position:current_position + length][::-1]
            knot = copied_data[0:256]
            if current_position + length > 256:
                knot[:(current_position + length) - 256] = copied_data[256:current_position + length]
            current_position = (current_position + length + skip_size) % 256
            skip_size += 1

    return "".join(["{:02x}".format(reduce(lambda x, y: x ^ y, knot[i:i+16])) for i in range(0,256,16)])