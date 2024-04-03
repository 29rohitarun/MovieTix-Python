import datetime

def process_array(arr):
    # rating format
    arr[1] = arr[1].split(',')[0].strip()
    print(arr[1])
    # seats format
    arr[6] = arr[6].split('<')[0].strip()
    print(arr[6])
    # date format
    year = datetime.date.today().year
    arr[7] = arr[7] + ", " + str(year)
    arr[7] = arr[7].strip()
    print(arr[7])

    # tix format
    tix = arr[9].split('span>')[1]
    tix = tix.split('<span')[0]
    arr[9] = tix.strip()
    print(arr[9])

    return arr

def main(unprocessed_arr):
    return process_array(unprocessed_arr)

if __name__ == '__main__':
    main()