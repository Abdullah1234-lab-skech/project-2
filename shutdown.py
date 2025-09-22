def shutdown_system():
    print("Shutdown system Intitiated.") 
    confirmation=input('Are you sure to shutdown the system ? yes/no:') 
    if confirmation.lower()=='yes':
        print("System is shutting down...") 
        print("Goodbye !") 
    else:
        print("Shutdown cancelled.") 
shutdown_system()