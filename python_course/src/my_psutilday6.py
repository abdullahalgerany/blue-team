import psutil
import time
from logger import logger

THRESHOLD = 3
SECONDS = 10

def main():
    vals = []
    
    logger.info(f"Live monitoring with limit of {THRESHOLD}% every {SECONDS} seconds")

    try:
        while True:
            # print(f"this is the cpu-time{psutil.cpu_times_percent(interval=1)}")
            # print(f"this is the cpu %{psutil.cpu_percent(interval=1)}")
            cpu_usage = psutil.cpu_percent(interval=1)
            vals.append(cpu_usage)
            
            logger.debug(f"Current CPU: {cpu_usage:.1f}%")

            if len(vals) > SECONDS:
                vals.pop(0)
            
            if len(vals) == SECONDS:
                avg = sum(vals) / SECONDS
                logger.info(f"Average CPU usage ({SECONDS}s): {avg:.1f}%")
                
                if avg >= THRESHOLD:
                    logger.warning(f"[ALERT] CPU {avg:.1f}% ≥ {THRESHOLD}% over {SECONDS}s")
                    vals.clear()
    
    except KeyboardInterrupt:
        logger.info("Monitoring stopped by user")
    except Exception as e:
        logger.error(f"Error occurred: {str(e)}")

if __name__ == "__main__":
    main()