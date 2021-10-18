import hashlib, datetime, time


class Block:
    def __init__(self, data, previous_hash):
      self.timestamp = datetime.datetime.now()
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash(self.timestamp, self.data, self.previous_hash)
      self.next = None

    def calc_hash(self, timestamp, data, previous_hash):
        sha = hashlib.sha256()
        sha.update(timestamp.isoformat().encode('utf-8'))
        sha.update(data.encode('utf-8'))
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
            newB = Block(data,prev)
            elapsed = newB.timestamp - curr.timestamp
            if elapsed > datetime.timedelta(seconds=1):
                curr.next = newB
            else:
                print("Add block failed - A new block is created every 1 second.")

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
                print("Timestamp:", curr.timestamp.isoformat())
                print("Message:", curr.data)
                print("Current Hash:", curr.hash)
                print("Previous Hash:", curr.previous_hash)
                print("=================================================================================")

                curr = curr.next
                index += 1

            print("")

if __name__ == "__main__":
    # test case 1 - edge case - depricate all the new blocks created in less then one second since the birth of the latest block.
    bitcoin = Blockchain()
    bitcoin.add_block("Chancellor on brink of second bailout for banks.")
    bitcoin.add_block("2nd message")                                        # Add block failed - A new block is created every 1 second.
    bitcoin.add_block("3rd message")                                        # Add block failed - A new block is created every 1 second.
    bitcoin.add_block("4th message")                                        # Add block failed - A new block is created every 1 second.
    bitcoin.add_block("5th message")                                        # Add block failed - A new block is created every 1 second.
    bitcoin.print_blockchain()                                              # print out the genesis block only. (index = 0)

    # test case 3 - edge case - empty Blockchain
    bitcoin1 = Blockchain()
    bitcoin1.print_blockchain()                                             # This blockchain is empty.

    # test case 3
    bitcoin2 = Blockchain()
    bitcoin2.add_block("Chancellor on brink of second bailout for banks.")
    time.sleep(1.5)
    bitcoin2.add_block("2nd message")
    time.sleep(1.5)
    bitcoin2.add_block("3rd message")
    time.sleep(1.5)
    bitcoin2.add_block("4th message")
    time.sleep(1.5)
    bitcoin2.add_block("5th message")
    bitcoin2.print_blockchain()                                             # All the new blocks are successfully added to the blockchain because of the 1.5 sec of time sleep.