# python3

def parallel_processing(n, m, data):
    output = []
    n_operators = [0] * n
    time = 0; data_element = 0
    while data_element<m:
        for i in range(len(n_operators)):
            if n_operators[i] == 0:
                output.append((i,time))
                n_operators[i]=data[data_element]
                data_element+=1
                n_operators[i] = n_operators[i] - 1 
            else :
                n_operators[i] = n_operators[i] - 1
        time+=1
    return output

def main():
    input_str = input()
    input_list = input_str.split()
    n = int(input_list[0])
    m = int(input_list[1])
    data = list(map(int,input().strip().split()))[:m]
    result = parallel_processing(n,m,data)
    print(n,m)
    for x in result:
        print(*x)

if __name__ == "__main__":
    main()
