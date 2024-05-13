def fcfs(initial_position, requests):
    total_head_movements = 0
    current_position = initial_position

    for request in requests:
        total_head_movements += abs(request - current_position)
        current_position = request

    return total_head_movements

def scan(initial_position, requests, num_cylinders):
    total_head_movements = 0
    current_position = initial_position
    direction = 'inward'

    requests.sort()

    while requests:
        if direction == 'inward':
            for request in requests[:]:
                if request >= current_position:
                    total_head_movements += abs(request - current_position)
                    current_position = request
                    requests.remove(request)
            direction = 'outward'
        else:
            for request in reversed(requests[:]):
                if request <= current_position:
                    total_head_movements += abs(request - current_position)
                    current_position = request
                    requests.remove(request)
            direction = 'inward'

    return total_head_movements

def cscan(initial_position, requests, num_cylinders):
    total_head_movements = 0
    current_position = initial_position
    requests.sort()

    while requests:
        for request in requests[:]:
            total_head_movements += abs(request - current_position)
            current_position = request
            requests.remove(request)
        total_head_movements += num_cylinders - current_position
        current_position = 0

    return total_head_movements

def read_requests_from_file(file_path):
    with open(file_path, 'r') as file:
        requests = [int(line.strip()) for line in file]
    return requests

def main():
    initial_position = 100
    file_path = 'requests.txt'
    num_cylinders = 5000

    requests = read_requests_from_file(file_path)

    fcfs_head_movements = fcfs(initial_position, requests.copy())
    print("FCFS Total Head Movements:", fcfs_head_movements)

    scan_head_movements = scan(initial_position, requests.copy(), num_cylinders)
    print("SCAN Total Head Movements:", scan_head_movements)

    cscan_head_movements = cscan(initial_position, requests.copy(), num_cylinders)
    print("C-SCAN Total Head Movements:", cscan_head_movements)

if __name__ == "__main__":
    main()
