def trace_path(my_dict):  # A Map objec
    rl = []

    for start in my_dict:
        tmp = []
        s = set()
        while my_dict.get(start, None):
            tmp.append([start, my_dict[start]])
            s.add(start)
            start = my_dict[start]

            if len(s) == len(my_dict):
                return tmp
    return None

planes = {
  "NewYork": "Chicago",
  "Boston": "Texas",
  "Missouri": "NewYork",
  "Texas": "Missouri"
}

print(trace_path(planes))