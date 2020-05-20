from celery_app_task import cel

if __name__ == '__main__':
    cel.worker_main()
    # cel.worker_main(argv=['--loglevel=info')