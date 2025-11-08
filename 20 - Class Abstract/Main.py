# abc = abstract base class

from abc import ABC, abstractmethod

class Button(ABC):

    @abstractmethod
    def click(self):
        pass

class pushButton(Button):

    def click(self):
        print("Push Button Click")

class radioButton(Button):

    def click(self):
        print("Radio Button Click")


pb = pushButton()
rb = radioButton()

pb.click()
rb.click()