import hamming as hm


def main() -> None:
    """Main function"""
    string = "Hello world"
    block_length = 16

    assert not block_length % 8, "Block length must be a multiple of 8."

    print("Input string:", string)
    print("Block length:", block_length)

    encoded = hm.hamming_encode(string, block_length)
    print(f"Encoded string: {encoded}")

    decoded = hm.hamming_decode(encoded, block_length)
    print(f"Decoded string: {decoded}")


if __name__ == '__main__':
    main()
