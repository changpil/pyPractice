
"""
<TIMESTAMP> <CATEGORY> <MESSAGE>
2018:01:17:10:34:00 ERROR Something bad happened
                    DEBUG
                    WARN
                    INFO
                    ERROR Something bad happened
                    ERROR Something else crashed
Something bad happened, 2
Something else crashed, Pattern1:knapsack
"""
def encounter_list(_str):
    data_dict = {}
    rt_list = []
    for line in _str.split('\n'):
        message = line.split()[2:]      #missed
        message = " ".join(message)     #missed
        num = data_dict.get(message, 0)
        data_dict[message] = num + 1
    print(data_dict)
    nums = {i for i in data_dict.values()}  # missed in to remove duplicates by set
    nums = list(nums)
    nums.sort(reverse=True)  # [10,8,7,6]

    for i in nums:
        for k, v in data_dict.items():
            if v == i:
                rt_list.append(k)
    return rt_list


_str = """\n
2018:01:17:10:34:00 ERROR Something bad happened\n
2018:01:17:10:34:00 DEBUG  ss                     \n
2018:01:17:10:34:00 WARN   sasa                     \n
2018:01:17:10:34:00 INFO   ss                     \n
2018:01:17:10:34:00 ERROR Something bad happened\n
2018:01:17:10:34:00 ERROR Something else crashed\n
"""
#{"message":encounter}

def get_the_most_messages( file_name):
    data = {}
    with open(file_name, 'rt') as f:
        for line in f:
            status = line.split()[1]
            message = line.split()[2:]
            message = " ".join(message) # forget again
            c =data.get(message, 0)
            data[message] = c+1

    value_set = list({i for i in data.values()})
    value_set.sort(reverse=True)
    rv =[]
    for i in value_set:
        for k, v in data.items():
            if v == i:
                rv.append(k)
    return rv


print(get_the_most_messages("../log_data.txt"))
