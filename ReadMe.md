Instagram cat verifier
---

A bot that checks the `cat` tag and verifies that the pictures posted are of cats!

Powered by [catdetector](http://catdetector.biz)

### Usage

1. Clone repo
2. Register an Instagram [Client](http://instagram.com/developer)
3. Create a file called `credentials.json` containing your client info,
with this format:

    ```
    {
        "client_id": "xxxxxxxxxxxxxxxxxxxxxxxxxx",
        "client_secret": "xxxxxxxxxxxxxxxxxxxx",
        "redirect_uri": "http://website.com"
    }
    ```

4. Run `python verify_cats.py` from the command line!
