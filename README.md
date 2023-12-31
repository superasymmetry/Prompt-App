# Prompt-App

A simple prompt app. This web app uses large language models to understand your prompts and to generate a valid response. Appropriate for any occasion. 

## Description

This is a GPT-based prompt app used for inspiration, ideas, and more. You simply enter the task and prompt, and we provide the rest.
Some example uses are:
  - Translate netween languages
  - Generate ideas
  - Re-format essays

## Getting Started

### Dependencies

* First, install python
  - [Python](https://www.python.org/downloads/)

* Install libraries
* After installing python, go to the command prompt and enter the following commands
  - Json

  ```
    pip install json
  ```

  - Sqlite
  ```
    pip install sqlite3
  ```

### Installing

Download and extract the zip file. Slight modification is needed after downloading the code.
* Open the ```config.json``` file in the main folder. Edit it with notepad.
  ![image](https://github.com/superasymmetry/Prompt-App/assets/64930215/03474182-0b2d-46f8-864c-1418bcea668e)

  ![image](https://github.com/superasymmetry/Prompt-App/assets/64930215/0277e049-919d-43a4-a4d0-0ad31a84b9d6)

* In the following code, change the api to be an API key retrieved from OpenAI. (The website to retrieve an api key is https://platform.openai.com/api-keys. If you do not have an OpenAI account, you will need to create one.)

  ```
  {
    "api_key": "Bearer YOUR_API_KEY"
  }
  ```

### How to use the program

Open the Command Prompt and cd to your downloaded project's folder location.
![image](https://github.com/superasymmetry/Prompt-App/assets/64930215/f2ea9773-6754-487c-b744-9f61fa9eac28)

Run the command 
```
python main.py
```
![image](https://github.com/superasymmetry/Prompt-App/assets/64930215/9d5a43c2-e50a-40cf-adea-a483f92a6d91)

Go to the link [http://127.0.0.1:8080/] in your browser. Voila!

Something similar to this should appear. Note: If it is the first time running your program, the two prompts on this screen will not be there.

![image](https://github.com/superasymmetry/Prompt-App/assets/64930215/4c419d5b-ab5f-43f4-b3cf-a0c3d4c666b2)

Click on the "plus" ion to add a prompt.

![image](https://github.com/superasymmetry/Prompt-App/assets/64930215/ab2c5150-a98f-4795-9812-65667bf612c5)

Type in what you want the prompt to be.

![image](https://github.com/superasymmetry/Prompt-App/assets/64930215/21edee83-6524-4e3b-8d46-3c2bf2a3f02e)

Click add. Now there should be a new prompt on the screen. Click into it and type in any supplemental messages or attach any images to further describe the prompt. After clicking submit, the output will appear on the screen after several seconds.

![image](https://github.com/superasymmetry/Prompt-App/assets/64930215/f1b3e041-de21-428e-b6ec-06b3728ce59d)

![image](https://github.com/superasymmetry/Prompt-App/assets/64930215/4e2510d3-a055-43c9-842f-d458fb5184de)

![image](https://github.com/superasymmetry/Prompt-App/assets/64930215/ccbe18c1-1ee0-43e6-ab4d-5a78109a024c)


## Authors & Development

Made by Siyu Zeng.
[Email](siyuzeng@proton.me)

## Version History

* 0.1
    * Initial Release
* 0.2
    * New image upload and processing feature
    * Bug fixes

## License

This project is licensed under the [Creative Commons] License - see the LICENSE.md file for details

## Acknowledgments

Inspiration
* [Baidu AI Assistant](https://inspiration.baidu.com/app)

If you would like to contribute to Prompt-App. Please message me or submit a pull request.
