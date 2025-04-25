```bash
git clone https://github.com/KorotkovaAnn/TestSoftware.git
cd saucedemo-e2e
python -m venv venv
source venv/bin/activate  # или venv\Scripts\activate на Windows
pip install -r requirements.txt
playwright install
