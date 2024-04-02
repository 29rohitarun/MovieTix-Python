import datetime

def process_array(arr):
    # rating format
    arr[1] = arr[1].split(',')[0].strip()
    print(arr[1])
    # seats format
    arr[5] = arr[5].split('<')[0].strip()
    print(arr[5])
    # date format
    year = datetime.date.today().year
    arr[6] = arr[6] + ", " + str(year)
    arr[6] = arr[6].strip()
    print(arr[6])

    # tix format
    tix = arr[8].split('span>')[1]
    tix = tix.split('<span')[0]
    arr[8] = tix.strip()
    print(arr[8])

    return arr

def main(unprocessed_arr):
    return process_array(unprocessed_arr)

if __name__ == '__main__':
    main()