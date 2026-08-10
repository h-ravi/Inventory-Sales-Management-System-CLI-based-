**AI Dwara Likha gaya Hai"
**Client:** RetailKart Pvt. Ltd. (Fictional)
**Project:** Inventory & Sales Management System (CLI-based)

**Background:**
Hamara ek chhota retail store hai. Abhi tak hum Excel me manually stock aur sales track karte hain, jisme bahut errors ho rahe hain. Humein ek simple Python-based system chahiye jo hamara data manage kare.

---

**Requirements:**

1. **Product Management**
   - Naya product add karo (ID, name, price, quantity)
   - Existing product update karo (price/quantity)
   - Product delete karo
   - Sabhi products ki list dikhao

2. **Sales Recording**
   - Jab bhi koi product becha jaaye, quantity automatically kam honi chahiye
   - Agar stock kam hai to system error de, sale confirm na ho
   - Har sale ka record alag se save ho (date, time, product, quantity, price)
   - **Bonus (extra banaya):** Net profit/loss bhi track ho, remaining stock value bhi calculate ho

3. **Data Storage**
   - Products ka data `products.json` me save ho
   - Sales history `sales.csv` me save ho

4. **Reports**
   - Total sales aaj ki, is week ki, is month ki dikhani chahiye
   - Low stock products (jinki quantity 5 se kam hai) ka alert dikhana

---

**Conditions (Client ki taraf se):**

- Code modular hona chahiye (OOP use karo — `Product` class, `Sales` class alag-alag hon)
- Agar galat input diya jaaye (jaise negative quantity, wrong ID), system crash nahi hona chahiye — proper error handling ho
- System restart hone ke baad bhi purana data safe rehna chahiye (file se load ho)
- Menu-driven CLI interface ho, sub-menus bhi ho (jaise Product Manager ke andar apna menu, Reports ke andar apna menu)

---

**Deliverables:**
- `main.py` — application start point
- `common.py` — shared/reusable functions (input validation, JSON save-load)
- `product.py` — Product class + product management menu
- `sales.py` — Sales class + selling logic
- `reports.py` — sales report + low stock alert
- Sample data files (`products.json`, `sales.csv`)