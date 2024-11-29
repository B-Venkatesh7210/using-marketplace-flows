# Using Marketplace Flows

This repository demonstrates how to use the **Mira SDK** to execute flows from the Mira Marketplace. It includes an example implementation of a  number of flows named **Clothing Suggestion Generator**, **Blog Post Generator**, **AI related answer Generator** where user-provided data is sent to the flow, and the result is fetched and printed.

---

## **Features**
- Initialize the Mira SDK client with an API key.
- Execute a specific flow version or the latest version dynamically.
- Fetch details of a specific flow from the Mira Marketplace.
- Modular and secure approach using environment variables for sensitive data.

---

## **Prerequisites**
1. **Mira Account**: Make sure you have made an account at [Mira Marketplace](https://console.mira.network/).
2. **API Key**: Generate an API Key from your [Mira Account Dashboard](https://console.mira.network/account/api-keys). 
3. **Python**: Ensure you have Python 3.10.0 installed. Currently mira-sdk@0.1.8 is compatible with Python 3.10.0 version.
4. **Dependencies**: Install the required libraries using the steps in the **Setup** section.

---

## **Setup**

### 1. Clone the Repository
```bash
git clone https://github.com/B-Venkatesh7210/using-marketplace-flows.git
cd using-marketplace-flows
```

### 2. Install Dependencies
```bash
pip install mira-sdk python-dotenv
```

### 3. Configure the API Key
- Create a `.env` file in the root of the project:
  ```bash
  touch .env
  ```
- Add your Mira Marketplace API key to the `.env` file:
  ```plaintext
  API_KEY=your_api_key_here
  ```

### 4. Run the Script
```bash
python clothing-test.py
```

---

## **Usage**

### Example Input
The script uses the **Clothing Suggestion Generator** flow to provide personalized clothing suggestions based on user data. You can modify the input data in the script as needed:
```python
input_data = {
    "age": "24",
    "height": "172cm",
    "skin_tone": "Fair",
    "color_preferences": "Green & Beige"
}
```
You can also see the example in the flow section of a particular [flow](https://console.mira.network/flows/anand/clothing-suggestion-generator/1.0.0).

### Example Output
The output of the flow execution will be printed in the terminal:
```plaintext
{'result': 'string'}
```

---

## **Project Structure**
```plaintext
.
├── clothing-test.py   # script to run clothing suggestiong generator flow
├── blogPost-test.py   # script to run blog post generator flow
├── flameKaiser-test.py   # script to run AI related answer Generatorr flow
├── .env            # Environment variables file (not tracked in Git)
├── .env.example       # Example Environment variables file
├── README.md       # Project documentation
```

---

## **How It Works**
1. The `MiraClient` is initialized with an API key from the `.env` file.
2. Get the flow details and code from the marketplace.
3. User input data is passed to the flow using the `execute` method.
4. The flow result is fetched and displayed in the terminal.
5. Additionally, you can retrieve metadata for the flow using the `get` method.

---

## **Dependencies**
- **[mira-sdk](https://pypi.org/project/mira-sdk/)**: To interact with the Mira Marketplace.
- **[python-dotenv](https://pypi.org/project/python-dotenv/)**: To securely load environment variables.

Install all dependencies with:
```bash
pip install mira-sdk python-dotenv
```

---

## **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## **Contributing**
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`feature/your-feature`).
3. Commit your changes.
4. Push the branch and open a pull request.

---

## **Contact**
If you have any questions or feedback, feel free to open an issue or contact [B-Venkatesh7210](https://github.com/B-Venkatesh7210).
