import sys, collections

class Node:
    def __init__(self, char, freq, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right
        self.code = ''


# create a tree
def create_tree(data):
    nodes = []
    freq_dict = collections.Counter(data) # Counter({' ': 4, 'h': 2, 'e': 2, 'i': 2, 'r': 2, 'd': 2, 'T': 1, 'b': 1, 's': 1, 't': 1, 'w': 1, 'o': 1})
    for char, freq in freq_dict.items():
        nodes.append(Node(char, freq))

    while len(nodes) > 1:
        nodes_sorted = sorted(nodes, key = lambda node : node.freq)
        
        node_left = nodes_sorted[0]
        node_right = nodes_sorted[1]

        node_left.code = '0'
        node_right.code = '1'

        new_char = node_left.char + node_right.char
        new_freq = node_left.freq + node_right.freq
        
        new_node = Node(new_char, new_freq, node_left, node_right)

        nodes.remove(node_left)
        nodes.remove(node_right)
        nodes.append(new_node)
    return nodes[0]


# create huff code dict
huff_code_dict = {}
def create_huff_code_dict(node, code=''):
    new_code = code + node.code
    if node.left:
        create_huff_code_dict(node.left, new_code)
    if node.right:
        create_huff_code_dict(node.right, new_code)
    if not node.left and not node.right:
        huff_code_dict[node.char] = new_code
    return huff_code_dict



def huffman_encoding(data):
    tree = create_tree(data)
    huff_code_dict = create_huff_code_dict(tree)
    encoded_data = ''
    for char in data:
        encoded_data += huff_code_dict[char]
    
    return encoded_data, tree

def huffman_decoding(data,tree):
    code_to_char = {}
    for char, code in huff_code_dict.items():
        code_to_char[code] = char

    decoded_data = ''
    while data:
        code = ''
        for i, digit in enumerate(data):
            code += digit
            if code in code_to_char:
                decoded_data += code_to_char[code]
                data = data[i+1:]
                break
    return decoded_data
        
        


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence))) # return 69
    print ("The content of the data is: {}\n".format(a_great_sentence)) # return The bird is the word

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2)))) # return 36
    print ("The content of the encoded data is: {}\n".format(encoded_data)) # return 0110111011111100111000001010110000100011010011110111111010101011001010

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data))) # return 69
    print ("The content of the decoded data is: {}\n".format(decoded_data)) # return The bird is the word