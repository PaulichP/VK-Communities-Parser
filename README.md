# VK-Communities-Parser
[English](README.md) | [Русский](README.RU.md)

VK-Communities-Parser is a Python program that allows you to extract and process posts from VKontakte (VK) communities.

## Prerequisites

Before running the program, make sure you have the following:

- Python 3 installed
- `requests` library installed (`pip install requests`)
- `demoji` library installed (`pip install demoji`)

## Getting Started

1. Clone the repository or download the program files.
2. Open the terminal or command prompt and navigate to the program's directory.

## Usage

1. Open the `VK-Communities-Parser.py` file in a text editor or IDE.
2. Replace the `'group_domain'` placeholder with the actual group ID of the VK community you want to parse.
3. Replace the `'access_token'` placeholder with your VKontakte API access token.
4. Run the `VK-Communities-Parser.py` file.

   ```bash
   python VK-Communities-Parser.py
   ```

5. Enter the number of posts you want to process when prompted.
6. The program will fetch the posts from the VK community, save them to a file, and process the file to remove unwanted content.
7. Once the process is complete, the program will display the number of posts processed and the number of valid posts after filtering.

## Customization

You can customize the program according to your needs. Here are some possible modifications:

- Adjust the regular expressions in the `process_posts_file` function to remove or modify specific patterns in the post content.
- Modify the `save_posts_to_file` function to change the file format or naming conventions.
- Extend the program by adding additional functions or features.

## Contributing

Contributions are welcome! If you find any issues or want to enhance the program, feel free to open an issue or submit a pull request.

## License

This program is licensed under the [MIT License](LICENSE).

## Acknowledgments

The program utilizes the VKontakte API for fetching posts from VK communities. Special thanks to the developers of `requests` and `demoji` libraries for their valuable contributions.


---

**Disclaimer**: This program is provided as-is without any warranty. Use it responsibly and respect the terms and conditions of the VKontakte platform.
