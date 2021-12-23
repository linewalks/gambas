# Gambas
Gambas is a config key validator. You can confirmed the config file whether its keys all exist or not.

Generally, `default.cfg` would be the standard for your config file. (Of course, you don't need to set `default.cfg` as a standard file name.) And, you has a config file used on your project, but not upload on your git due to `.gitignore`. I'll call it 'target config file'. Because it is a little bothering to sync two files, you sometimes might miss some keys.

Comparing two files' keys with **Gambas**, you can find the keys you missed of the target config file.

## Getting Started
### Built With
- Python >= 3.8.x

### Installation

1. Install Gambas with pip command
    ```sh
    > pip install gambas
    ```

## Usage

1. Prepare your 2 config files, default config file and target config file.
    ```
    # default config file
    PSQL_HOST=
    PSQL_HOST=
    PSQL_DBNAME=
    WEBHOOK_URL=
    ...
    ```
    ```
    # target config file
    PSQL_HOST="127.0.0.1"
    PSQL_HOST="5432"
    PSQL_DBNAME="test_db"
    WEBHOOK_URL="http://webhook.url.com"
    ...
    ```

2. Execute the command with config files path. The option `-d`. Another option `-t`.
    ```sh
    > gambas -f default_config.cfg -t target_config.cfg
    ```

3. If you don't want to let an error raise, execute the command with option `--no-error`. In this case, the warnig comes out instead of an error message.
    ```sh
    > gambas -f default_config.cfg -t target_config.cfg --no-error
    ```

## Contact
- Chung Yunyoung - yy.chung@linewalks.com
