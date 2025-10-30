# Pokémon GO QR Code PDF Generator

This is a simple Python script that creates a PDF containing **10 QR codes per page**.  
Each QR code card includes:
- The **group name** on top  
- The **QR code** in the middle  
- The **actual code** at the bottom  

It’s simple, not perfect, but it gets the job done.

---

## 🧩 How It Works

1. The program looks for a file named **`codes.txt`** in the same folder.  
   - You can change this filename by editing the `INPUT_FILE` variable at the top of the script.

2. The input file can contain codes separated by **spaces** or **new lines**.  
   - The script will automatically parse all codes.

3. For each code, the program:
   - Generates a QR code that links directly to the **Pokémon GO Web Store redemption page**,  
     with the code pre-filled so users only need to click **Claim**.

4. The script then formats these QR codes into a **printable PDF** — 10 codes per page default.

5. Each "card" includes:
   - A **black border** (for cutting along)
   - The **group name** (customizable with the `GROUP_NAME_TEXT` variable)
   - The **QR code**
   - The **actual code** printed below (for manual entry)

---

## 📝 Notes

- You can experiment with the layout settings in the script.  
- Keep in mind: **making the QR codes too small will make them hard to scan.**

---

## ⚙️ Example Usage

```bash
python3 generate_qr_pdf.py
```

---

## Example Output
![Example Output](example_output.png)