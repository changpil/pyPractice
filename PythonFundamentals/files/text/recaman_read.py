import sys

def read_series(filename):
    with open(filename, mode="rt", encoding="utf-8") as f:
        series = []
        for line in f:
            a = int(line.strip())
            series.append(a)
    return series

def main(filename):
    series = read_series(filename)
    print(series)

if __name__ == "__main__":
    main(sys.argv[1])