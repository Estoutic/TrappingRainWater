class Solution():
    def __init__(self) -> None:
        super().__init__()
        self.array_info =[]
        self.pull_count = []
        self.water_count = 0
        self.used_index = []

    def get_info(self):
        info = input()
        new_info = info[10:][:-1]
        for i in new_info.split(','):
            self.array_info.append(int(i))

    def get_trap(self):
        for i in range(0, len(self.array_info)):
            dict_of_pool = {}
            if i != len(self.array_info) - 1:
                if self.array_info[i] > self.array_info[i + 1] and self.array_info[i]:
                    if self.array_info[i] != max(self.array_info) and i != len(self.array_info) - 1:
                        count = i + 1
                        if count != len(self.array_info) - 1 and i not in self.used_index:
                            while self.array_info[i] > self.array_info[count] and len(self.array_info) >= count:
                                dict_of_pool[i] = str(self.array_info[i]) + ' ' + str(self.array_info[count + 1])
                                self.water_count += self.array_info[i] - self.array_info[count]
                                self.used_index.append(i)
                                self.used_index.append(count)
                                self.pull_count.append(dict_of_pool)
                                count += 1
        print(self.water_count)
