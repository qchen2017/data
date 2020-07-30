
import queue
import threading
import operator

class DataPack(object):
    def __init__(self, name='', age=None,  weight=None, description='统计居民'):
        self.name = name
        self.age = age
        self.weight = weight
        self.description = description
        # print('DataPack:',description)


class DataReceiver(object):
  def __init__(self):
      self.queue = list()
      self.receive_data()

  def receive_data(self):
      self.add_to_queue(DataPack("Thor", 10, 60))
      self.add_to_queue(DataPack("Iron man", 20, 130))
      self.add_to_queue(DataPack("Hulk", 16, 100))
      self.add_to_queue(DataPack("Doctor Strange", 23, 140))
      self.add_to_queue(DataPack("Vision", 17, 110))

  def add_to_queue(self, data_pack):
      if data_pack not in self.queue:
          self.queue.insert(0, data_pack)
          return True
      return False


  def get_data(self):
      if len(self.queue) > 0:
          print("get data")
          return self.queue.pop()
      else:
          print("No elements in DataReceiver!")
          return None

  def size(self):
      return len(self.queue)
