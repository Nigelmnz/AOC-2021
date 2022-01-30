from typing import List

def answer_1(input: List[str]):
    gamma_binary = most_common_bits(input)
    epsilon_binary = invert_bits(gamma_binary)

    return int(gamma_binary,2) * int(epsilon_binary,2)
    
def answer_2(input: List[str]):
    oxygen_bits = get_hidden_bits(input, False)
    co2_bits = get_hidden_bits(input, True)

    return int(oxygen_bits,2) * int(co2_bits,2)

def parse_lines(lines) -> List[str]:
    return lines

def get_hidden_bits(input, inverted):
    remaining = input
    
    for i in range(0, len(remaining[0])):
        if len(remaining) == 1:
            break

        common_bits = most_common_bits(remaining)
        if inverted:
            common_bits = invert_bits(common_bits)
        remaining = [bits for bits in remaining if bits[i] == common_bits[i]]

    return remaining[0]

def most_common_bits(input):
    bit_counts = [0] * len(input[0])
    for binary in input:
        for i, bit in enumerate(binary):
            bit_counts[i] += int(bit)

    return ''.join(['1' if count >= len(input) - count else '0' for count in bit_counts])

def invert_bits(bits):
    return ''.join('1' if b == '0' else '0' for b in bits)