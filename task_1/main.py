import queue
import time
import random
import signal

request_queue = queue.Queue()
request_id_counter = 1
simulation_running = True


def signal_handler(sig, frame):
    """Handles the SIGINT signal (Ctrl+C) to stop the simulation."""
    global simulation_running
    print("\n\n[SYSTEM] Received Ctrl+C. Initiating graceful shutdown...")
    simulation_running = False


try:
    signal.signal(signal.SIGINT, signal_handler)
except ValueError:
    # Handles potential ValueError if running in environments
    # like Jupyter/certain IDEs
    pass


def generate_requests_batch():
    """
    Fills the queue with a random number of new requests (Batch Generation).
    """
    global request_id_counter

    num_to_generate = random.randint(2, 7)

    print(
        f"\n[GENERATOR] --- Starting Batch Generation"
        f" (Count: {num_to_generate}) ---"
    )

    for _ in range(num_to_generate):
        # Determine Complexity (Processing Time in seconds: 1 to 5)
        processing_time = random.randint(1, 5)

        request_data = {
            'id': f"REQ-{request_id_counter: 04d}",
            'complexity': processing_time,
        }
        request_id_counter += 1

        request_queue.put(request_data)

    print(
        f"\n[GENERATOR] --- Batch Generation Complete."
        f" Queue size: {request_queue.qsize()} ---"
    )


def process_all_requests():
    """
    Processes ALL requests in the queue until it is empty.
    """
    print("\n[PROCESSOR] --- Starting Batch Processing ---")

    requests_processed = 0

    while not request_queue.empty():
        try:
            current_request = request_queue.get_nowait()

            req_id = current_request['id']
            processing_time = current_request['complexity']

            print(
                f"\n[PROCESSOR] <<< Retrieving: **{req_id}** (Time: "
                f"{processing_time}s). Remaining: {request_queue.qsize()}"
            )
            print(
                f"[PROCESSOR] ... Processing {req_id} for {processing_time}"
                f" seconds..."
            )

            time.sleep(processing_time)

            request_queue.task_done()

            print(f"[PROCESSOR] === Finished processing: **{req_id}**")
            requests_processed += 1

        except queue.Empty:
            break
        except Exception as e:
            print(f"\n[ERROR] An unexpected error occurred: {e}")

    print(
        f"\n[PROCESSOR] --- Batch Processing Complete."
        f" Total processed: {requests_processed}. Queue is empty. ---"
    )


if __name__ == "__main__":
    print("--- Simple Sequential Batch Processing Simulation ---")
    print("= PRESS Ctrl+C TO STOP THE PROGRAM =")

    while simulation_running:
        generate_requests_batch()
        process_all_requests()

    print("--- Program terminated. ---")
    print(f"Total Requests Handled: {request_id_counter - 1}")
