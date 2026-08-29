import time

def main():
    print("Long task started...")
    time.sleep(120)  # simulate a slow job (~2 minutes)
    with open("task-complete.txt", "w") as f:
        f.write("Task completed successfully!")
    print("Long task finished. Marker file written.")

if __name__ == "__main__":
    main()
