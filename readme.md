**LYVA Sportswear Warehouse Management System**
Please read this before you proceed to run the application

This Python project was created to fulfill the Capstone Project Module 1, which involves the implementation of fundamental Python learning from the Digital Science course by Purwadhika Digital School. It aims to implement basic CRUD (Create, Read, Update, Delete) functions for managing warehouse inventory of sportswear items.

- Introduction
Efficient inventory management is the backbone of any retail business. In a sportswear warehouse, keeping track of stock levels, organizing items by categories and racks, and knowing when to reorder are critical to ensure smooth operations. Recognizing this need, I developed a warehouse management system tailored for LYVA Sportswear. This application serves as a centralized platform for warehouse staff and administrators to manage inventory data seamlessly.

The application uses dummy data and is not connected to a database, serving purely as a programming exercise to understand the basics of Python. Additionally, it utilizes one Python library:

Tabulate: for displaying data in structured table form with various grid styles.

**Features**
**- User Authentication (Login): ** Secure login with three attempts. Three user roles: admin, staff, and a custom user (madina). Admin has additional privileges for editing and deleting data.

**- Data Display (Read Menu : )** View all items in inventory.

**- Filter items by category** (Top, Bottom, Accessories) or by rack code.

**- Search for a specific item** using its unique item code.

**Data Addition (Create Menu)**

Add new items with validation: unique 5‑digit item code, category selection from predefined list, rack code, name, and initial stock.

**Data Update (Update Stock)**
Increase, decrease, or set new stock levels for any item. Real‑time stock status (HABIS, SANGAT MENIPIS, MENIPIS, AMAN, OVERLOAD) is recalculated.

**Data Editing (Edit Data)**
Admin‑only feature to modify item details (rack code, name, category, stock) based on category or rack filtering.

**Data Deletion (Delete Menu)**
Admin‑only feature to remove items from inventory, either by category or by rack.

**Stock Warning System**
Automatically detects items with stock ≤ 10 (including zero) and displays a warning on the main menu. A dedicated menu shows detailed statistics and recommendations.

**Mini Warehouse Report**

Provides an overview: total items, total stock, distribution per category, top 3 items with highest stock, and counts of items that are out of stock or critically low.

**Implementation**

**Data Display (Read Menu)**

**Login Menu**

<img width="448" height="202" alt="image" src="https://github.com/user-attachments/assets/3e2192d3-51f0-4ffb-baf0-fd43dbfc7635" />

**- Main Menu View**

When the user selects option "1" from the main menu, the application displays a submenu to view data:

<img width="461" height="330" alt="image" src="https://github.com/user-attachments/assets/96f15128-31d7-42f6-afc8-360806d8d5f3" />

**Submenu 2 – Display by Category**
The user is prompted to enter a category (Top, Bottom, or Accessories). The system then shows all items belonging to that category in a formatted table with stock status.

<img width="457" height="258" alt="image" src="https://github.com/user-attachments/assets/f6c8bd63-f5b0-4fe6-9018-7694880257dc" />

<img width="747" height="559" alt="image" src="https://github.com/user-attachments/assets/f9480305-0ba2-4473-9ad5-8435cb3b6523" />

**Submenu 4 – Search by Item Code**
The user enters a 5‑digit item code and receives detailed information about that item, including its current stock status.

<img width="401" height="240" alt="image" src="https://github.com/user-attachments/assets/9668239e-a3c9-4325-879d-c22a6ed2d5fe" />

**Data Addition (Create Menu)**
Adding a New Item
Users are guided through a step‑by‑step process. Input validation ensures the item code is exactly 5 digits and unique. Category is chosen from a numbered menu. A summary is shown before confirmation.

<img width="444" height="143" alt="image" src="https://github.com/user-attachments/assets/3b28b3fc-88af-4aff-b2fd-a80bed071a0d" />

<img width="438" height="515" alt="image" src="https://github.com/user-attachments/assets/bfdba836-7b7c-4d95-8761-b4c62954f4f2" />

**Data Update (Update Stock)**
**Modifying Stock Levels**
The user enters the item code of the product they wish to update. The current data is displayed, and then they choose an operation: add, subtract, or set new stock. After the change, the new stock and its status are shown.

<img width="539" height="583" alt="image" src="https://github.com/user-attachments/assets/80682511-75a4-4929-93b5-8806f7b88450" />

**Data Editing (Edit Data)**
**Admin‑Only Feature**
Only users logged in as admin can access this menu. They can edit items by first filtering by category or rack, then selecting the item and the field to modify (rack code, name, category, stock). Confirmation is required before saving changes.

**Data Deletion (Delete Menu)**
**Admin‑Only Feature**
Items can be removed by first filtering by category or rack. After selecting the item, the system asks for confirmation. A success message shows the remaining item count.

<img width="445" height="391" alt="image" src="https://github.com/user-attachments/assets/9b022d36-4290-43cf-bccf-b3ef38522fbc" />

**Stock Warning System**
**Automatic Alert on Main Menu**
If any item has stock ≤ 10, the main menu displays a warning:

<img width="431" height="102" alt="image" src="https://github.com/user-attachments/assets/053dedb5-072f-4b5f-ab59-955af835cf2b" />

**Detailed Warning Menu**
Selecting option "5" shows a complete list of items with low or zero stock, along with statistics and recommendations.

<img width="642" height="472" alt="image" src="https://github.com/user-attachments/assets/224991cd-7841-4fa7-8613-c3775f72dc01" />


**Mini Warehouse Report
Option 6 – Laporan Statistik**
Provides a comprehensive overview of the warehouse:
Total number of item types and total stock.

- Breakdown of stock status (habis, menipis, aman).
- Distribution per category with item counts and total stock.
- Top 3 items with the highest stock.

<img width="442" height="376" alt="image" src="https://github.com/user-attachments/assets/f410381d-d2bb-4324-8b1f-4e0fc30cb093" />

The development of this sportswear warehouse management system is an important step in improving inventory control and operational efficiency at LYVA Sportswear. By providing user‑friendly tools to manage stock, filter items by various criteria, and receive automatic low‑stock warnings, this application empowers warehouse staff and administrators to maintain optimal inventory levels and ensure product availability. The system demonstrates fundamental CRUD operations, input validation, role‑based access control, and data presentation using the Tabulate library – all essential skills in Python programming.

Created by:
Madina Febriani
