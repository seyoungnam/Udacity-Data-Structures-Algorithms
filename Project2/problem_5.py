import hashlib
from datetime import datetime

class Block:
    def __init__(self, data, previous_hash):
      self.timestamp = datetime.now().isoformat()
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash(self.timestamp, self.data, self.previous_hash)
      self.next = None

    def calc_hash(self, timestamp, data, previous_hash):
        sha = hashlib.sha256()
        sha.update(timestamp.encode('utf-8'))
        sha.update(data.encode('utf-8'))
        # print(type(previous_hash))
        sha.update(b'{previous_hash}')
        return sha.hexdigest()


class Blockchain:
    def __init__(self):
        self.head = None

    def add_block(self, data):
        if self.head == None:
            self.head = Block(data, 0)
        else:
            curr = self.head
            while curr.next:
                curr = curr.next

            prev = curr.hash
            curr.next = Block(data, prev)

    def print_blockchain(self):
        if self.head == None:
            print("This blockchain is empty.")
            return
        else:
            curr = self.head
            index = 0
            print("=================================================================================")

            while curr:
                print("Index:", index)
                print("Timestamp:", curr.timestamp)
                print("Message:", curr.data)
                print("Current Hash:", curr.hash)
                print("Previous Hash:", curr.previous_hash)
                print("=================================================================================")

                curr = curr.next
                index += 1

            print("")

if __name__ == "__main__":

    bitcoin = Blockchain()
    bitcoin.print_blockchain()
    bitcoin.add_block("Chancellor on brink of second bailout for banks.")
    bitcoin.add_block("2nd message")
    bitcoin.add_block("3rd message")
    bitcoin.add_block("4th message")
    bitcoin.add_block("5th message")
    bitcoin.print_blockchain()
    