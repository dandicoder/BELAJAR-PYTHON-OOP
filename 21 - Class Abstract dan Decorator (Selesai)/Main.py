from abc import ABC, abstractmethod

class Button(ABC):

    def __init__(self, set_link):
        self.set_link = set_link

    @abstractmethod
    def click(self):
        pass

    @property
    @abstractmethod
    def setLink(self):
        pass

class pushButton(Button):

    def click(self):
        print("Go To Link : {}".format(self.set_link))

    @Button.setLink.getter
    def setLink(self, input):
        self.__set_link = input

    @setLink.setter
    def setLink(self):
        return self.set_link
    
pb = pushButton("www.dandi.com")

pb.click()