# AutoPoker

**AutoPoker** is a semi-automated poker playing bot designed to analyze the game environment, make strategic decisions, and execute actions efficiently. This project leverages advanced multi-modal llm implementation to enhance poker gameplay through screeshots.

![AutoPoker Logo](logo.png)

## Features
- Automated decision-making based on hand strength, betting patterns, and opponent behavior.
- Customizable strategies for different poker scenarios.
- Efficient code structure for fast response times during gameplay.
- Modular design for easy integration and updates.

## Requirements
To run AutoPoker, you'll need the following:
- Python 3.9 or higher
- Required libraries:
  - `numpy`
  - `pandas`
  - `selenium`
  - `opencv`
- **Gemma 3 Model**: Download the **Gemma 3 4B-IT** model from [Hugging Face](https://huggingface.co/google/gemma-3-4b-it) and place it in a directory called `gemma` within the project folder.

Install dependencies with:
```bash
pip install -r requirements.txt
```

## Installation
1. Clone this repository:
```bash
git clone https://github.com/javierchacon262/AutoPoker.git
```
2. Navigate to the project directory:
```bash
cd AutoPoker
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Download the **Gemma 3 4B-IT** model from [Hugging Face](https://huggingface.co/google/gemma-3-4b-it) and place it in a directory called `gemma_local` within the project folder.

## Usage
To run the bot, execute the following command:
```bash
python RunPokerAssistant.py
```

### Configuration
- Update the **`config.json`** file to adjust gameplay settings and strategies.
- Modify the **`strategy.py`** file to implement custom logic for decision-making.

## Roadmap
- [ ] Improve opponent behavior prediction.
- [ ] Add support for multiple poker platforms.
- [ ] Implement a GUI for better visualization and control.

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m "Add new feature"`).
4. Push the branch (`git push origin feature-name`).
5. Open a pull request.

## License
This project is licensed under the **GNU General Public License**. See the [LICENSE](LICENSE) file for more details.

## Contact
For inquiries or support, please contact **javierchacon262@gmail.com, WS +573177301805**.
