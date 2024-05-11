# Importing necessary library
import sys

def generate_dict(N):
    return {number: number ** 2 for number in range(1, N + 1)}

# Main function handling the input/output
def main():
    N = int(sys.stdin.readline().strip())
    result = generate_dict(N)
    print(result)

if __name__ == "__main__":
    main()