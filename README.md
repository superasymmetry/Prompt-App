# Prompt-App

A simple prompt app.

## Description

This is a GPT-based prompt app used for inspiration, ideas, and more. You simply enter the task and prompt, and we provide the rest.
Some example uses:
  - Translate netween languages
  - Generate ideas
  - Re-format essays

## Getting Started

### Dependencies

* Any operating system
* Pre-installed packages
  - [Python](https://www.python.org/downloads/)
  - Json

  ```
    pip install json
  ```

  - Sqlite
  ```
    pip install sqlite3
  ```

### Installing

Slight modification is needed after downloading the code.
* Download the project
* Add a file in the main folder called ```config.json```
* Add in the following code. Use an API key retrieved from OpenAI
  ```
  {
    "api_key": "YOUR API KEY HERE"
  }
  ```
- Modify the file called ```views.py```. Change the following code to include your ```config.json``` file location
  ```
  url = "https://api.openai.com/v1/chat/completions"
  with open(r'YOUR CONFIG FILE LOCATION') as config_file:
    config = json.load(config_file)

  api_key = config['api_key']
  ```

### Executing program

Go to the ```main.py``` file and run. Then go to the localhost link in the terminal. It should be [http://127.0.0.1:8080/](http://127.0.0.1:8080/).


## Authors & Development

Made by Siyu Zeng.
[Email](siyuzeng@proton.me)

## Version History

* 0.1
    * Initial Release

## License

This project is licensed under the [Creative Commons] License - see the LICENSE.md file for details

## Acknowledgments

Inspiration
* [Baidu AI Assistant](https://inspiration.baidu.com/app)
