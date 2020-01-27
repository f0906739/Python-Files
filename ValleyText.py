from meme import meme_format


class ValleyText():

    # parameter 'letters' refers to the number of letters that will be included in the text
    def buildDown(self, text, letters=None, storage=[]):
        if letters is None:
            letters = len(text)
        if letters > 1:
            storage.append(text[:letters].rstrip(" "))
            letters -= 1
            return self.buildDown(text, letters, storage)
        else:
            storage.append(text[:letters].rstrip(" "))
            self.printBuild(storage)
            return storage

    def buildUp(self, text, letters=2, storage=[]):
        if letters != len(text) - 1:
            storage.append(text[:letters].rstrip(" "))
            letters += 1
            return self.buildUp(text, letters, storage)
        else:
            storage.append(text[:letters].rstrip(" "))
            self.printBuild(storage)
            return storage

    def printBuild(self, text):
        for index, i in enumerate(text):
            if index != 0 and text[index - 1] != i:
                print(i)
            elif index == 0:
                print(i)

    def firstLetter(self, text):
        print(text[0])
        return text[0]

    def run(self, first, second):
        self.firstLetter(first)
        self.buildUp(first, storage=[])
        self.buildDown(first, storage=[])
        self.buildUp(second, storage=[])
        self.buildDown(second, storage=[])


print("\n")
starter = meme_format(
    "\"A surge is not likely\"... Sanders is in second place nationally at 19%"
)
ending = meme_format("And Biden is no longer my cool uncle.")

ValleyText().run(starter, ending)
