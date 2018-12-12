score_file = "score.txt"
def print_marks(file_name):
    file = open(file_name, "r")
    for line in file:
        length = len(line)
        start = 0

        for index in range(length):
            if line[index]==',':
                start=index+1

                if index==length-1:
                    mark=float(line[start:index])

                    print(mark)

print_marks(score_file)