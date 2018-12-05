import pickle
def create_graph():
    #graph where key is id and value is a list of their friends ids
    master_dict = dict()
    graph = open("./data/graph.txt", "r")
    lines = graph.readlines()
    for line in lines:
        nums = line.split()
        key = int(nums[0])
        value = int(nums[1])
        if key in master_dict:
            friends = master_dict[key]
            friends.append(value)
            master_dict[key] = friends

        else:
            master_dict[key] = [value]


    pickle_out = open("./data/master_graph_dict.pkl", 'wb')
    desc = "a dictionary of the social graph where the keys are ids and the values are a list of their friends ids"
    pickle.dump((master_dict, desc), pickle_out)
    pickle_out.close()

def create_train_dict():
    train = open("./data/posts_train.txt", "r")
    lines = train.readlines()
    # print(len(lines))
    master_dict = dict()

    for l in range(1, len(lines)):
        line = lines[l]
        nums = line.split(",")
        key = int(nums[0])
        value = []
        for i in range(1, len(nums)):
            value.append(float(nums[i]))

        if key in master_dict:
            print("duplicate")
        else:
            master_dict[key] = value

    pickle_out = open("./data/posts_train_dict.pkl", 'wb')
    desc = "a dictionary of the training points with ids as keys and Hour1,Hour2,Hour3,Lat,Lon,Posts as values"
    pickle.dump((master_dict, desc), pickle_out)
    pickle_out.close()

def create_test_dict():
    test = open("./data/posts_test.txt", "r")
    lines = test.readlines()
    master_dict = dict()

    for l in range(1, len(lines)):
        line = lines[l]
        nums = line.split(",")
        key = int(nums[0])
        value = []
        for i in range(1, len(nums)):
            value.append(float(nums[i]))

        if key in master_dict:
            print("duplicate")
        else:
            master_dict[key] = value


    pickle_out = open("./data/posts_test_dict.pkl", 'wb')
    desc = "a dictionary of the training points with ids as keys and Hour1,Hour2,Hour3,Posts as values"
    pickle.dump((master_dict, desc), pickle_out)
    pickle_out.close()



if __name__ == '__main__':
    create_graph()
    create_train_dict()
    create_test_dict()