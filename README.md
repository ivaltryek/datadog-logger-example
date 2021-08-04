# datadog-logger-example
Datadog Custom Logger example

## How to run this example

- Create Virtual environment
  
  ```shell
  # For Linux
  python3 -m venv .venv

  # For Windows
  python -m .venv venv
  ```
- Enable Virtual environment
  
  ```shell
  # For Linux
  source .venv/bin/activate

  # For Windows
  .venv\Scripts\Activate
  ```

- Install required packages
  
  ```shell
  pip3 install -r requirements.txt
  ```
- Run the main script
  
  ```shell
  # Linux
  python3 runtests.py

  #Windows
  python runtests.py
  ```
> 💡 Please add your datadog API key in set_envs.py to connect with datadog and only then your logs will be sent to datadogs
