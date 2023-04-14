# splitter bits

        train_data = pd.DataFrame()
        test_data = pd.DataFrame()

        test_selections = test_size * self.dataset_size

        split_data = self.data

        index_choices = []        

        while test_selections > 0:
            index = random.randint(0,self.dataset_size-1)
            if index not in index_choices:
                index_choices.append(index)
                test_selections -= 1

        for index in split_data:
            if index in index_choices:
                test_data.append(split_data[index])
            else:
                train_data.append(split_data[index])

        print(train_data)
        print(test_data)

# end splitter bits
