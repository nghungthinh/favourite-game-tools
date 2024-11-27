import argparse
import threading
import time
from user_registration import register_worker, generate_usernames

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Generate usernames dynamically or manually.")
    
    parser.add_argument("--mode", type=str, required=True, choices=["auto", "manual"],
                        help="Mode of username generation: 'auto' or 'manual'")
    parser.add_argument("--base_username", type=str, default="user",
                        help="Base username for auto-generated accounts (only used in 'auto' mode')")
    parser.add_argument("--count", type=int, default=0,
                        help="Number of usernames to generate (only used in 'auto' mode')")
    parser.add_argument("--manual_usernames", nargs="*", default=[],
                        help="List of manual usernames (only used in 'manual' mode')")
    parser.add_argument("--threads", type=int, default=1,
                        help="Number of threads to use for registration")
    parser.add_argument("--phone", type=str, required=True,
                        help="Phone number for registration")
    parser.add_argument("--password", type=str, required=True,
                        help="Password for registration")

    args = parser.parse_args()

    # Generate usernames based on the mode
    if args.mode == "auto":
        if args.count <= 0:
            raise ValueError("Please specify a positive count for 'auto' mode.")
        usernames = generate_usernames(base_username=args.base_username, count=args.count, mode="auto")
    elif args.mode == "manual":
        if not args.manual_usernames:
            raise ValueError("Please provide manual usernames for 'manual' mode.")
        usernames = generate_usernames(base_username=None, mode="manual", manual_usernames=args.manual_usernames)
    else:
        raise ValueError("Invalid mode specified.")

    # Divide usernames evenly across threads
    chunk_size = len(usernames) // args.threads
    threads = []

    for i in range(args.threads):
        start_idx = i * chunk_size
        end_idx = start_idx + chunk_size if i < args.threads - 1 else len(usernames)
        thread_usernames = usernames[start_idx:end_idx]

        # Start a thread with a chunk of usernames
        t = threading.Thread(target=register_worker, args=(thread_usernames, args.password, args.phone, len(thread_usernames)))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
