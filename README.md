# Gambas
Gambas is a config key validator. You can confirm the config file whether its keys all exist or not.

Generally, `default.cfg` would be the standard for your config file. (Of course, you don't need to set `default.cfg` as a standard file name.) And, you has a config file used on your project, but not upload on your git due to `.gitignore`. I'll call it 'target config file'. Because it is a little bothering to sync two files, you sometimes might miss some keys.

Comparing two files' keys with **Gambas**, you can find the keys you missed of the target config file.

## Getting Started
### Built With
- Python >= 3.6.x

### Installation

1. Install Gambas with pip command
    ```sh
    > pip install gambas
    ```

## Usage

1. Prepare your 2 config files, default file and target file. The file extension is limited only on `cfg`, `json`.
    ```
    # cfg file
    PSQL_HOST="127.0.0.1"
    PSQL_PORT="5432"
    PSQL_DBNAME="test_db"
    WEBHOOK_URL="http://webhook.url.com"
    ...
    ```
    ```
    # json file
    {
        "psql_host": "127.0.0.1",
        "psql_port": "5432",
        "psql_dbname": "test_db",
        "webhook_url": "http://webhook.url.com",
    }
    ...
    ```

2. Execute the command with config files path. 

    - `-d`: the default config file
    - `-t`: the target config file
    ```sh
    > gambas -d default_config.cfg -t target_config.cfg
    ```
    You also can compare files with different extensions.
    ```sh
    > gambas -d default_config.cfg -t target_json.json
    ```
3. If you don't want to let an error raise, execute the command with option `--no-error`. In this case, the warnig comes out instead of an error message.
    ```sh
    > gambas -d default_config.cfg -t target_config.cfg --no-error
    ```

## Contact
- Chung Yunyoung - yy.chung@linewalks.com
