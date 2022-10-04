import datetime
import time

separator = "#" * 100

def timer(func):
    def wrapper(*args, **kwargs):
        log_time = time.time()
        datetime_log = datetime.datetime.now
        print(f"{separator}\n\n[{datetime_log()}] Session STARTED!")
        
        fr = func(*args, **kwargs)
        
        print(f"[{datetime_log()}] Session ENDED!")
        print(f"[{datetime_log()}] EXECUTION TIME: {time.time() - log_time}\n\n{separator}\n")
        return fr 
    
    return wrapper


def print_return(func):
    def wrapper(*args, **kwargs):
        log_time = time.time()
        datetime_log = datetime.datetime.now
        print(f"{separator}\n\n[{datetime_log()}] Session STARTED!")
        
        fr = func(*args, **kwargs)
        print(f"{separator}\n\n{fr}\n\n")
        
        
        print(f"[{datetime_log()}] Session ENDED!")
        print(f"[{datetime_log()}] EXECUTION TIME: {time.time() - log_time}\n\n{separator}\n")
        return fr 
    
    return wrapper