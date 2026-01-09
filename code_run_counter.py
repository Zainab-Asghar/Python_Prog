import os

COUNT_FILE = 'run_count.txt'

def get_run_count():
    if not os.path.exists(COUNT_FILE):
        return 0
    with open(COUNT_FILE, 'r') as f:
        return int(f.read().strip())

def save_run_count(count):
    with open(COUNT_FILE, 'w') as f:
        f.write(str(count))

def main():
    count = get_run_count() + 1
    save_run_count(count)
    print(f'This script has been run {count} times.')

if __name__ == '__main__':
    main()
